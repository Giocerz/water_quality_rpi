from ..tools.service import Characteristic, Descriptor
from w1thermsensor import W1ThermSensor
from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import ParametersCalculate
from src.logic.batteryLevel import BatteryProvider
from ..BLEConstants import BLEConstants
import dbus


class MonitoringCharacteristic(Characteristic):
    def __init__(self, service):
        self.notifying = False
        Characteristic.__init__(
            self, BLEConstants.MONITORING_UUID,
            ["read"], service)
        self.add_descriptor(MonitoringDescriptor(self))
        self.sensors_init()

    def sensors_init(self):
        self.temperature_sensor = W1ThermSensor()
        self.parameters = ParametersVoltages()
        self.parameters_calc = ParametersCalculate()
        self.battery_provider = BatteryProvider()

    def get_parameters(self):
        try:
            temp = round(self.temperature_sensor.get_temperature(), 2)
            ph = round(self.parameters_calc.calculatePh(
                self.parameters.ph_volt()), 2)
            do = round(self.parameters_calc.calculateDo(
                self.parameters.oxygen_volt(), temp), 2)
            tds = round(self.parameters_calc.calculateTds(
                temp, self.parameters.tds_volt()), 2)
            turb = round(self.parameters_calc.calculateTurb(
                self.parameters.turbidity_volt()), 2)

            battery = self.battery_provider.getBatteryLevel()

        except Exception as e:
            print(e)

        strtemp = f"dt,{temp},{do},{tds},{ph},{turb},{battery},pg"
        return strtemp.encode()

    def ReadValue(self, options):
        value = self.get_parameters()
        return value


class MonitoringDescriptor(Descriptor):
    WQ_DESCRIPTOR_UUID = "2901"
    WQ_DESCRIPTOR_VALUE = "WQ Monitoring"

    def __init__(self, characteristic):
        Descriptor.__init__(
            self, self.WQ_DESCRIPTOR_UUID,
            ["read"],
            characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.WQ_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value