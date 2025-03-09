import dbus
from .tools.advertisement import Advertisement
from .tools.service import Application, Service
from PySide2.QtCore import QThread
from src.config.Constants import Constants
from .characteristics.MonitoringCharacteristic import MonitoringCharacteristic
from .characteristics.CalibrationCharacteristics import CalibrationCharacteristic
from .characteristics.GetIdCharacteristic import GetIDCharacteristic
from .BLEConstants import BLEConstants

GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"

class WaterQualityAdvertisement(Advertisement):
    def __init__(self, index):
        Advertisement.__init__(self, index, "peripheral")
        self.add_local_name(Constants.BLE_ID)
        self.include_tx_power = True


class WaterParametersService(Service):
    def __init__(self, index):

        Service.__init__(self, index, BLEConstants.SERVICE_UUID, True)
        self.add_characteristic(MonitoringCharacteristic(self))
        self.add_characteristic(GetIDCharacteristic(self))
        self.add_characteristic(CalibrationCharacteristic(self))

app_blue = None
adv_blue = None


class BluetoothService(QThread):
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
