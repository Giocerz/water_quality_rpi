import dbus
import random
from .advertisement import Advertisement
from .service import Application, Service, Characteristic, Descriptor
from PySide2.QtCore import QSize, QThread, Signal, Slot

GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
NOTIFY_TIMEOUT = 3000


class WaterQualityAdvertisement(Advertisement):
    def __init__(self, index):
        Advertisement.__init__(self, index, "peripheral")
        self.add_local_name("WaterQualityBL")
        self.include_tx_power = True


class WaterParametersService(Service):
    WQ_SVC_UUID = "00000001-710e-4a5b-8d75-3e5b444bc3cf"

    def __init__(self, index):
        self.farenheit = True

        Service.__init__(self, index, self.WQ_SVC_UUID, True)
        self.add_characteristic(WQCharacteristic(self))
        self.add_characteristic(UnitCharacteristic(self))

    def is_farenheit(self):
        return self.farenheit

    def set_farenheit(self, farenheit):
        self.farenheit = farenheit


class WQCharacteristic(Characteristic):
    WQ_CHARACTERISTIC_UUID = "00000002-710e-4a5b-8d75-3e5b444bc3cf"

    def __init__(self, service):
        self.notifying = False
        Characteristic.__init__(
            self, self.WQ_CHARACTERISTIC_UUID,
            ["notify", "read"], service)
        self.add_descriptor(ParamDescriptor(self))

    def get_parameters(self):
        temp = round(random.uniform(29.1, 31.22), 2)
        ph = round(random.uniform(6.0, 7.0), 2)
        do = round(random.uniform(3.12, 5.0), 2)
        tds = round(random.uniform(434.23, 678.23), 2)

        strtemp = f"dt,{temp},{ph},{do},{tds},pg"
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


class UnitCharacteristic(Characteristic):
    UNIT_CHARACTERISTIC_UUID = "00000003-710e-4a5b-8d75-3e5b444bc3cf"

    def __init__(self, service):
        Characteristic.__init__(
            self, self.UNIT_CHARACTERISTIC_UUID,
            ["read", "write"], service)
        self.add_descriptor(UnitDescriptor(self))

    def WriteValue(self, value, options):
        val = str(value[0]).upper()
        if val == "C":
            self.service.set_farenheit(False)
        elif val == "F":
            self.service.set_farenheit(True)

    def ReadValue(self, options):
        value = []

        if self.service.is_farenheit():
            val = "F"
        else:
            val = "C"
        value.append(dbus.Byte(val.encode()))

        return value


class UnitDescriptor(Descriptor):
    UNIT_DESCRIPTOR_UUID = "2901"
    UNIT_DESCRIPTOR_VALUE = "C, ph, mg/L, "

    def __init__(self, characteristic):
        Descriptor.__init__(
            self, self.UNIT_DESCRIPTOR_UUID,
            ["read"],
            characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.UNIT_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

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
