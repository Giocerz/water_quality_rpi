from src.logic.Constants import Constants

class ParametersCalculate():
    DO_TABLE = [
        14460, 14220, 13820, 13440, 13090, 12740, 12420, 12110, 11810, 11530,
        11260, 11010, 10770, 10530, 10300, 10080, 9860, 9660, 9460, 9270,
        9080, 8900, 8730, 8570, 8410, 8250, 8110, 7960, 7820, 7690,
        7560, 7430, 7300, 7180, 7070, 6950, 6840, 6730, 6630, 6530, 6410
    ]

    RES2 = 820.0
    ECREF = 200.0

    def __init__(self):
        super(ParametersCalculate, self).__init__()

        self.kValue = None
        self.phOffset = None
        self.phSlopeA = None
        self.phSlopeB = None
        self.oxygenTempCal = None
        self.oxygenVoltCal = None
        self.turb_coef_a = None
        self.turb_coef_b = None
        self.turb_coef_c = None
        self.tds_sensor_code = Constants.TDS_EC_SENSOR

        self.set_calibration_values()

    def set_calibration_values(self):
        import pandas as pd
        df = pd.read_csv('src/config/calibrationSettings.txt')
        lista = df['calibration_values'].tolist()
        self.kValue = float(lista[0])
        self.phOffset = float(lista[1])
        self.phSlopeA = float(lista[2])
        self.phSlopeB = float(lista[3])
        self.oxygenTempCal = float(lista[4])
        self.oxygenVoltCal = float(lista[5]) * 1000
        self.turb_coef_a = float(lista[6])
        self.turb_coef_b = float(lista[7])
        self.turb_coef_c = float(lista[8])

    def calculateTds(self, temperature: float, voltage: float) -> float:
        print(f'TDS VOLTAGE: {voltage}')
        if self.tds_sensor_code == Constants.SEN0244:
            return self.__calculate_tds_with_sen0244(temperature, voltage)
        else:
            return self.__calculate_tds_with_dfr0300(temperature, voltage)

    def tds_calibration(self, temperature: float, voltage: float) -> float:
        if self.tds_sensor_code == Constants.SEN0244:
            return self.__tds_calibration_with_sen0244(temperature, voltage)
        else:
            return self.__tds_calibration_with_df0300(temperature, voltage)

    def calculatePh(self, voltage: float) -> float:
        if(voltage < self.phOffset):
            return (voltage - self.phOffset)/self.phSlopeA + 7
        else:
            return (voltage - self.phOffset)/self.phSlopeB + 7

    def calculateDo(self, voltage: float, temperature:float) -> float:
        if(temperature > 40.0):
            temperature = 40.0
        elif(temperature < 0.0):
            temperature = 0.0
        voltage *= 1000
        voltageSaturation = int(self.oxygenVoltCal) + int(temperature * 35) - int(self.oxygenTempCal * 35)
        return float(voltage * self.DO_TABLE[int(self.oxygenTempCal)] / voltageSaturation) * 0.001

    def calculateTurb(self, voltage: float) -> float:
        turb = self.turb_coef_a * voltage ** 2 + self.turb_coef_b * voltage + self.turb_coef_c
        if(turb >= 500.0):
            turb = 500.0
        elif(turb < 0.0):
            turb = 0.0
        return turb
    

    def __calculate_tds_with_sen0244(self, temperature: float, voltage: float) -> float:
        kValue = self.kValue
        if (voltage > 0.05):
            tdsFactor = 0.5
            ecValue = (133.42 * voltage * voltage * voltage - 255.86 *
                       voltage * voltage + 857.39 * voltage) * kValue
            ecValue25 = ecValue / (1.0 + 0.02 * (temperature - 25.0))
            tdsValue = ecValue25 * tdsFactor
            return tdsValue
        return 0.0

    def __calculate_tds_with_dfr0300(self, temperature: float, voltage: float) -> float:
        if (voltage > 0.01):
            kValue = self.kValue
            tdsFactor = 0.5
            rawEC = 1000*voltage/self.RES2/self.ECREF
            value = rawEC * kValue
            value = value / (1.0+0.0185*(temperature-25.0))
            tdsValue = value * tdsFactor
            return tdsValue
        else:
            return 0.0

    def __tds_calibration_with_sen0244(self, temperature: float, voltage: float) -> float:
        solution = 1413
        rawECsolution = solution * (1.0 + 0.02 * (temperature - 25.0))
        kValueTemp = rawECsolution /(133.42 * voltage * voltage * voltage -
             255.86 * voltage * voltage + 857.39 * voltage)
        if (kValueTemp > 10.0):
            return 0.0
        else:
            return kValueTemp
    
    def __tds_calibration_with_df0300(self, temperature: float, voltage: float) -> float:
        solution = 1413.0 / 1000.0
        compECsolution = solution*(1.0+0.0185*(temperature-25.0))
        kValueTemp = self.RES2*self.ECREF*compECsolution/voltage; 
        if (kValueTemp > 10.0):
            return 0.0
        else:
            return kValueTemp