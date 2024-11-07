import dbus
import random
from .advertisement import Advertisement
from .service import Application, Service, Characteristic, Descriptor
from PySide2.QtCore import QSize, QThread, Signal, Slot
from w1thermsensor import W1ThermSensor
from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import *
from src.logic.INA219 import INA219

GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
NOTIFY_TIMEOUT = 3000
DEVICE_ID = "CAP0003-FC"

class WaterQualityAdvertisement(Advertisement):
    def __init__(self, index):
        Advertisement.__init__(self, index, "peripheral")
        self.add_local_name("CitizenAP0003")
        self.include_tx_power = True


class WaterParametersService(Service):
    WQ_SVC_UUID = "00000001-b149-430d-8d97-e2ed464102df"

    def __init__(self, index):

        Service.__init__(self, index, self.WQ_SVC_UUID, True)
        self.add_characteristic(WQCharacteristic(self))
        self.add_characteristic(IDCharacteristic(self))

    """
    def is_farenheit(self):
        return self.farenheit

    def set_farenheit(self, farenheit):
        self.farenheit = farenheit
    """


class WQCharacteristic(Characteristic):
    WQ_CHARACTERISTIC_UUID = "00000002-710e-4a5b-8d75-3e5b444bc3cf"

    def __init__(self, service):
        self.notifying = False
        Characteristic.__init__(
            self, self.WQ_CHARACTERISTIC_UUID,
            ["notify", "read"], service)
        self.add_descriptor(ParamDescriptor(self))

    def sensors_init(self):
        self.temperature_sensor = W1ThermSensor()
        self.parameters = ParametersVoltages()
        self.parameters_calc = ParametersCalculate()
        self.ina219 = INA219(addr=0x42)

    def get_parameters(self):
        temp = round(self.temperature_sensor.get_temperature(), 2)
        ph = round(self.parameters_calc.calculatePh(
                    self.parameters.ph_volt()), 2)
        do = round(self.parameters_calc.calculateDo(
                    self.parameters.oxygen_volt(), temp), 2)
        tds = round(self.parameters_calc.calculateTds(
        temp = self.parameters.tds_volt()), 2)
        turb = round(self.parameters_calc.calculateTurb(
                    self.parameters.turbidity_volt()), 2)
                
        bus_voltage = self.ina219.getBusVoltage_V()

        p = int((bus_voltage - 6)/2.4*100)
        if(p > 100):
            p = 100
        if(p < 0):
            p = 0

        self.parameters_result.emit([ph, do, tds, temp, turb, p])

        strtemp = f"dt,{temp},{do},{tds},{ph},{turb},{p},pg"
        return strtemp.encode()

    def set_params_callback(self):
        if self.notifying:
            value = self.get_parameters()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return

        self.notifying = True
        value = self.get_parameters()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_params_callback)

    def StopNotify(self):
        self.notifying = False

    def ReadValue(self, options):
        value = self.get_parameters()
        return value


class ParamDescriptor(Descriptor):
    WQ_DESCRIPTOR_UUID = "2901"
    WQ_DESCRIPTOR_VALUE = "WQ Parameters"

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


class IDCharacteristic(Characteristic):
    ID_CHARACTERISTIC_UUID = "00000002-b149-430d-8d97-e2ed464102df"

    def __init__(self, service):
        self.notifying = False
        Characteristic.__init__(
            self, self.ID_CHARACTERISTIC_UUID,
            ["read"], service)

    def get_id(self):
        strtemp = DEVICE_ID
        return strtemp.encode()
    
    def ReadValue(self, options):
        value = self.get_id()
        return value



app_blue = None
adv_blue = None
class BluetoothWorker(QThread):
    def __init__(self):
        super().__init__()
        global app_blue, adv_blue
        if app_blue == None:
            app_blue = Application()
            app_blue.add_service(WaterParametersService(0))
            app_blue.register()
            adv_blue = WaterQualityAdvertisement(0)

    def run(self):
        global app_blue, adv_blue
        adv_blue.register()
        app_blue.run()

    def stop(self):
        global app_blue, adv_blue
        adv_blue.unregister()
        app_blue.quit()
        self.wait()
