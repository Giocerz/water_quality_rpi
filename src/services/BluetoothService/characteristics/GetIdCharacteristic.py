from ..tools.service import Characteristic, Descriptor
from src.config.Constants import Constants
from ..BLEConstants import BLEConstants
import dbus

class GetIDCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, BLEConstants.DEVICE_ID_UUID,
            ["read"], service)
        self.add_descriptor(GetIDDescriptor(self))

    def get_id(self):
        strtemp = Constants.DEVICE_ID
        return strtemp.encode()

    def ReadValue(self, options):
        value = self.get_id()
        return value


class GetIDDescriptor(Descriptor):
    ID_DESCRIPTOR_UUID = "2902"
    ID_DESCRIPTOR_VALUE = "Device ID"

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