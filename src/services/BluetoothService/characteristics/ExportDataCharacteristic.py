from ..tools.service import Characteristic, Descriptor
from ..BLEConstants import BLEConstants
from src.model.WaterQualityDB import WaterDataBase, LoteModel, WaterQualityParams
import dbus

class ExportDataCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, BLEConstants.EXPORT_DATA_UUID,
            ["read", "write"], service)
        self.add_descriptor(ExportDataDescriptor(self))
        self.reset_flags()
        self.data_is_ready_provider = DataIsReadyProvider()

    def WriteValue(self, value, options):
        data = bytes(value).decode("utf-8")
        if data == "START_L":
            self.data_is_ready_provider.set_data_is_ready(False)
            self.reset_flags()
            self.set_total_lotes()
            self.data_is_ready_provider.set_data_is_ready(True)
            return
        elif data == "GET_L":
            self.data_is_ready_provider.set_data_is_ready(False)
            self.get_lotes()
            self.data_is_ready_provider.set_data_is_ready(True)
            return
        elif data == "NEXT":
            self.data_is_ready_provider.set_data_is_ready(False)
            if self.sends_counter >= len(self.data_chunks):
                self.data_to_send = "SEND_COMPLETE"
                self.data_is_ready_provider.set_data_is_ready(True)
                return
            self.data_to_send = self.data_chunks[self.sends_counter]
            self.sends_counter += 1
            self.data_is_ready_provider.set_data_is_ready(True)
        elif "GET_S" in data:
            self.data_is_ready_provider.set_data_is_ready(False)
            command = data.split(':')
            if command == "ALL":
                #TO DO GET ALL SAMPLES
                self.get_all_samples()
            else:
                try:
                    lote_id = int(command)
                    self.get_lote_samples(lote_id)
                except:
                    self.data_to_send = "SEND_ERROR"
            self.data_is_ready_provider.set_data_is_ready(True)
            

        
    
    def ReadValue(self, options):
        value = self.data_to_send.encode()
        return value
    
    def reset_flags(self):
        self.data_to_send:str = ''
        self.data_chunks:list[str] = []
        self.sends_counter:int = 0
    
    def set_total_lotes(self):
        total_lotes:int = WaterDataBase.count_total_lotes()
        self.data_to_send = f'TOT_L:{total_lotes}'
    
    def get_lotes(self):
        self.reset_flags()
        lotes_list: list[LoteModel] = WaterDataBase.get_lotes()
        result: str = ''
        
        for lote in lotes_list:
            total_samples: int = WaterDataBase.count_samples_by_lote(lote.id)
            lote_name_hex = lote.name.encode().hex()  # Codificar en HEX
            result += f'{lote.id},{lote_name_hex},{total_samples};'
        
        self.data_chunks = [result[i:i+30] for i in range(0, len(result), 30)]

    def get_all_samples(self):
        self.reset_flags()
        samples_list: list[WaterQualityParams] = WaterDataBase.get_water_quality_params()
        result: str = ''
        
        for sample in samples_list:
            sample_name_hex = sample.name.encode().hex()
            sample_origin_hex = sample.sample_origin.encode().hex()
            sample_it_rainded_hex = sample.it_rained.encode().hex()
            sample_temp = sample.temperature if sample.temperature is not None else "nu"
            sample_od = sample.oxygen if sample.oxygen is not None else "nu"
            sample_tds = sample.tds if sample.tds is not None else "nu"
            sample_ph = sample.ph if sample.ph is not None else "nu"
            sample_turb = sample.turbidity if sample.turbidity is not None else "nu"
            sample_battery = sample.battery if sample.battery is not None else "nu"
            result += f'{sample_name_hex},{sample.latitude},{sample.longitude},{sample.latitude},{sample.longitude},{sample.date},{sample.hour},{sample_temp},{sample_od},{sample_tds},{sample_ph},{sample_turb},{sample_battery},{sample_origin_hex},{sample_it_rainded_hex},{sample.lote_id};'
        
        self.data_chunks = [result[i:i+30] for i in range(0, len(result), 30)]

    def get_lote_samples(self, lote_id:int):
        self.reset_flags()
        samples_list: list[WaterQualityParams] = WaterDataBase.get_water_quality_params_by_lote(lote_id)
        result: str = ''
        
        for sample in samples_list:
            sample_name_hex = sample.name.encode().hex()
            sample_origin_hex = sample.sample_origin.encode().hex()
            sample_it_rainded_hex = sample.it_rained.encode().hex()
            sample_temp = sample.temperature if sample.temperature is not None else "nu"
            sample_od = sample.oxygen if sample.oxygen is not None else "nu"
            sample_tds = sample.tds if sample.tds is not None else "nu"
            sample_ph = sample.ph if sample.ph is not None else "nu"
            sample_turb = sample.turbidity if sample.turbidity is not None else "nu"
            sample_battery = sample.battery if sample.battery is not None else "nu"
            result += f'{sample_name_hex},{sample.latitude},{sample.longitude},{sample.latitude},{sample.longitude},{sample.date},{sample.hour},{sample_temp},{sample_od},{sample_tds},{sample_ph},{sample_turb},{sample_battery},{sample_origin_hex},{sample_it_rainded_hex},{sample.lote_id};'
        
        self.data_chunks = [result[i:i+30] for i in range(0, len(result), 30)]

class ExportDataDescriptor(Descriptor):
    ID_DESCRIPTOR_UUID = "2904"
    ID_DESCRIPTOR_VALUE = "Export data"

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
    
class DataIsReadyProvider:
    _instance = None  # Singleton

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DataIsReadyProvider, cls).__new__(cls)
            cls._instance._is_data_ready = False
        return cls._instance

    def get_data_is_ready(self):
        return self._is_data_ready

    def set_data_is_ready(self, value:bool):
        self._is_data_ready =  value