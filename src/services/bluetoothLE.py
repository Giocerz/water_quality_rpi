import dbus
import random
from .advertisement import Advertisement
from .service import Application, Service, Characteristic, Descriptor
from PySide2.QtCore import QSize, QThread, Signal, Slot
from src.logic.saveCalibration import SaveCalibration
from w1thermsensor import W1ThermSensor
from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import *
from src.logic.INA219 import INA219

GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
NOTIFY_TIMEOUT = 3000
DEVICE_ID = "CAP0003-FC"
SERVICE_UUID = "00000001-b149-430d-8d97-e2ed464102df"
DEVICE_ID_UUID = "00000002-b149-430d-8d97-e2ed464102df"
CALIBRATION_SAVE_UUID = "00000009-b149-430d-8d97-e2ed464102df"
CALIBRATION_UUID = "00000003-b149-430d-8d97-e2ed464102df"
MONITORING_UUID = "00000005-b149-430d-8d97-e2ed464102df"


class WaterQualityAdvertisement(Advertisement):
    def __init__(self, index):
        Advertisement.__init__(self, index, "peripheral")
        self.add_local_name("CitizenAP0003")
        self.include_tx_power = True


class WaterParametersService(Service):
    def __init__(self, index):

        Service.__init__(self, index, SERVICE_UUID, True)
        self.add_characteristic(WQCharacteristic(self))
        self.add_characteristic(IDCharacteristic(self))
        self.add_characteristic(CalibrationCharacteristic(self))


class WQCharacteristic(Characteristic):
    def __init__(self, service):
        self.notifying = False
        Characteristic.__init__(
            self, MONITORING_UUID,
            ["read"], service)
        self.add_descriptor(ParamDescriptor(self))
        self.sensors_init()

    def sensors_init(self):
        self.temperature_sensor = W1ThermSensor()
        self.parameters = ParametersVoltages()
        self.parameters_calc = ParametersCalculate()
        self.ina219 = INA219(addr=0x42)

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

            bus_voltage = self.ina219.getBusVoltage_V()

            p = int((bus_voltage - 6)/2.4*100)
            if (p > 100):
                p = 100
            if (p < 0):
                p = 0

        except Exception as e:
            print(e)

        strtemp = f"dt,{temp},{do},{tds},{ph},{turb},{p},pg"
        return strtemp.encode()

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
    def __init__(self, service):
        Characteristic.__init__(
            self, DEVICE_ID_UUID,
            ["read"], service)
        self.add_descriptor(IDDescriptor(self))

    def get_id(self):
        strtemp = DEVICE_ID
        return strtemp.encode()

    def ReadValue(self, options):
        value = self.get_id()
        return value


class IDDescriptor(Descriptor):
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


class CalibrationCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, CALIBRATION_UUID,
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
                save.add_kvalue(self.kValue)
            if (values[2] != 'nu'):
                save.add_ph_offset(self.ph_offset)
                if (values[3] != 'nu'):
                    save.add_ph_slopes([self.ph_slopeA, self.ph_slopeB])
            if (values[5] != 'nu'):
                save.add_oxygen(self.oxygenTemperature, self.oxygenOffset)
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
                    result = f'{volt_ph}'
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
                    result = f'{volt_turb}'
            except Exception as e:
                print(e)
            strtemp = f"dt,{result},pg"
        self.calibration_finish = False
        print('***********************************')
        print(f'ESTADO: {self.calibration_state}')
        print(f'DATOS: {strtemp}')
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


class CalibrationSaveCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, CALIBRATION_SAVE_UUID,
            ["read", "write"], service)
        self.add_descriptor(CalibrationSaveDescriptor(self))
        self.calibration_state = False

    def WriteValue(self, value, options):
        val = str(value[0])
        if val == "C":
            self.calibration_state = True

    def ReadValue(self, options):
        value = ''

        if self.calibration_state:
            value = 'CALIBRADO'.encode()
        else:
            value = 'NO CALIBRADO'.encode()

        return value


class CalibrationSaveDescriptor(Descriptor):
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
