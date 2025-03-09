from ..tools.service import Characteristic, Descriptor
from w1thermsensor import W1ThermSensor
from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import ParametersCalculate
from src.logic.saveCalibration import SaveCalibration
from ..BLEConstants import BLEConstants
import dbus

class CalibrationCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, BLEConstants.CALIBRATION_UUID,
            ["read", "write"], service)
        self.add_descriptor(CalibrationDescriptor(self))
        self.calibration_state = ''
        self.calibration_finish = False
        self.sensors_init()

    def sensors_init(self):
        self.temperature_sensor = W1ThermSensor()
        self.parameters = ParametersVoltages()
        self.parameters_calc = ParametersCalculate()

    def WriteValue(self, value, options):
        self.calibration_state = ''
        val = str(value[0])
        if val == "w":
            for i in range(len(value)):
                self.calibration_state += str(value[i])
        else:
            l = len(value)
            init = str(value[0]) + str(value[1])
            finish = str(value[l - 2]) + str(value[l - 1])
            if (init == 'ca' and finish == 'ac'):
                result = ''
                for i in range(l):
                    result += str(value[i])
                self.calibration_state = 'ca'
                self.save_values(result)

    def save_values(self, value: str):
        try:
            save = SaveCalibration()
            values = value.split(',')
            if (values[1] != 'nu'):
                save.add_kvalue(float(values[1]))
            if (values[2] != 'nu'):
                save.add_ph_offset(float(values[2]))
                if (values[3] != 'nu'):
                    save.add_ph_slopes([float(values[3]), float(values[4])])
            if (values[5] != 'nu'):
                save.add_turbidity([float(values[5]), float(values[6]), float(values[7])])
            if (values[8] != 'nu'):
                save.add_oxygen(float(values[8]), float(values[9]))
            save.save()
            self.calibration_finish = True
        except Exception as e:
            self.calibration_finish = False

    def get_parameters(self):
        if (self.calibration_state == 'ca'):
            if (self.calibration_finish):
                strtemp = f"OK"
            else:
                strtemp = f"ERROR"
        else:
            try:
                result = ''
                if (self.calibration_state == 'wq_c_t'):
                    temp = round(self.temperature_sensor.get_temperature(), 2)
                    volt_tds = round(self.parameters.tds_volt(), 2)
                    result = f'{temp},{volt_tds}'
                elif (self.calibration_state == 'wq_c_p'):
                    volt_ph = round(self.parameters.ph_volt(), 2)
                    result = f'-,{volt_ph}'
                elif (self.calibration_state == 'wq_c_o'):
                    temp = round(self.temperature_sensor.get_temperature(), 2)
                    volt_do = round(self.parameters.oxygen_volt(), 2)
                    result = f'{temp},{volt_do}'
                elif (self.calibration_state == 'wq_c_q'):
                    temp = round(self.temperature_sensor.get_temperature(), 2)
                    volt_tds = round(self.parameters.tds_volt(), 2)
                    volt_ph = round(self.parameters.ph_volt(), 2)
                    result = f'{temp},{volt_tds},{volt_ph}'
                else:
                    volt_turb = round(self.parameters.turbidity_volt(), 2)
                    result = f'-,{volt_turb}'
            except Exception as e:
                print(e)
            strtemp = f"dt,{result},pg"
        self.calibration_finish = False
        return strtemp.encode()

    def ReadValue(self, options):
        value = self.get_parameters()
        return value


class CalibrationDescriptor(Descriptor):
    ID_DESCRIPTOR_UUID = "2903"
    ID_DESCRIPTOR_VALUE = "Calibration save"

    def __init__(self, characteristic):
        Descriptor.__init__(
            self, self.ID_DESCRIPTOR_UUID,
            ["read"],
            characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.ID_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value