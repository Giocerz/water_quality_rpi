class ParametersCalculate():
    DO_TABLE = [
        14460, 14220, 13820, 13440, 13090, 12740, 12420, 12110, 11810, 11530,
        11260, 11010, 10770, 10530, 10300, 10080, 9860, 9660, 9460, 9270,
        9080, 8900, 8730, 8570, 8410, 8250, 8110, 7960, 7820, 7690,
        7560, 7430, 7300, 7180, 7070, 6950, 6840, 6730, 6630, 6530, 6410
    ]

    def __init__(self):
        super(ParametersCalculate, self).__init__()

        self.kValue = None
        self.phOffset = None
        self.phSlope = None
        self.oxygenTempCal = None
        self.oxygenVoltCal = None

        self.set_calibration_values()

    def set_calibration_values(self):
        import pandas as pd
        df = pd.read_csv('src/config/calibrationSettings.txt')
        lista = df['calibration_values'].tolist()
        print(lista)
        self.kValue = float(lista[0])
        self.phOffset = float(lista[1])
        self.phSlope = float(lista[2])
        self.oxygenTempCal = float(lista[3])
        self.oxygenVoltCal = float(lista[4])

    def calculateTds(self, temperature: float, voltage: float) -> float:
        kValue = self.kValue
        if (voltage > 0.05):
            tdsFactor = 0.5
            ecValue = (133.42 * voltage * voltage * voltage - 255.86 *
                       voltage * voltage + 857.39 * voltage) * kValue
            ecValue25 = ecValue / (1.0 + 0.02 * (temperature - 25.0))
            tdsValue = ecValue25 * tdsFactor
            return tdsValue
        else:
            return 0.0

    def tds_calibration(self, temperature: float, voltage: float) -> float:
        solution = 1413
        rawECsolution = solution * (1.0 + 0.02 * (temperature - 25.0))
        kValueTemp = rawECsolution / \
            (133.42 * voltage * voltage * voltage -
             255.86 * voltage * voltage + 857.39 * voltage)
        if (kValueTemp > 10.0):
            return 0.0
        else:
            return kValueTemp

    def calculatePh(self, voltage: float) -> float:
        return (voltage - self.phOffset)/self.phSlope + 7

    def calculateDo(self, voltage: float, temperature:float) -> float:
      voltage *= 1000
      self.oxygenVoltCal *= 1000
      voltageSaturation = int(self.oxygenVoltCal) + int(temperature * 35) - int(self.oxygenVoltCal * 35)
      return float(voltage * self.DO_TABLE[int(self.oxygenTempCal)] / voltageSaturation)

    def calculateTurb(self, voltage: float) -> float:
        return voltage
