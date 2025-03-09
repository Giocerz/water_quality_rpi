from ..tools.service import Characteristic, Descriptor
from ..BLEConstants import BLEConstants
from src.model.WaterQualityDB import WaterDataBase, LoteModel
import dbus

class ExportDataCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, BLEConstants.EXPORT_DATA_UUID,
            ["read", "write"], service)
        self.add_descriptor(ExportDataDescriptor(self))
        self.reset_flags()

    def WriteValue(self, value, options):
        data = bytes(value).decode("utf-8")
        if data == "START":
            self.reset_flags()
            self.set_total_lotes()
            return
        elif data == "GET_L":
            self.get_lotes()
            return
        elif data == "NEXT":
            if self.sends_counter >= len(self.data_chunks):
                return
            self.data_to_send = self.data_chunks[self.sends_counter]
            self.sends_counter += 1
        
    
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
        lotes_list:list[LoteModel] = WaterDataBase.get_lotes()
        result:str = ''
        for lote in lotes_list:
            total_samples:int = WaterDataBase.count_samples_by_lote(lote.id)
            result += f'{lote.id},{lote.name},{total_samples};'
        self.data_chunks = [result[i:i+20] for i in range(0, len(result), 20)]


    


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