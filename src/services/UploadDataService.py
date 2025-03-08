import json
import time
import requests
from PySide2.QtCore import QThread, Signal
from src.model.WaterQualityDB import WaterDataBase
from src.config.sxdswe import Sxdswe

class UploadService(QThread):
    upload_finished = Signal(bool, str)  
    progress = Signal(int, int)  

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ssswsx = Sxdswe.yshwh
        self.wsdww2sx = Sxdswe.rswgst
        self.is_cancelled = False  

    def run(self):
        max_upload_length = 10
        max_request_per_minute = 10  
        requests_count = 0
        start_time = time.time()  # Marca de tiempo inicial
        is_successful = True
        error_msg = ""

        try:
            data_to_upload = WaterDataBase.get_water_quality_params_no_sync()
            total = len(data_to_upload)

            for i in range(0, total, max_upload_length):
                if self.is_cancelled:
                    is_successful = False
                    error_msg = "Subida cancelada"
                    break

                # Verificar si ya pasaron 60 segundos desde la primera solicitud
                elapsed_time = time.time() - start_time
                if requests_count >= max_request_per_minute and elapsed_time < 60:
                    wait_time = 60 - elapsed_time
                    for _ in range(int(wait_time)):  
                        if self.is_cancelled:
                            self.upload_finished.emit(False, "Subida cancelada")
                            return
                        time.sleep(1)
                    requests_count = 0  # Reiniciar contador
                    start_time = time.time()  # Reiniciar tiempo

                chunk = data_to_upload[i:i + max_upload_length]
                payload = json.dumps({"readings": [self.convert_keys(param.to_dict()) for param in chunk]})


                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {self.wsdww2sx}'
                }

                try:
                    response = requests.post(self.ssswsx, data=payload, headers=headers, timeout=15)

                    if response.status_code == 200:
                        for param in chunk:
                            WaterDataBase.update_upload_state(param.id, 1)
                    else:
                        is_successful = False
                        error_msg = f"Error {response.status_code}"
                        break

                except requests.exceptions.RequestException:
                    is_successful = False
                    error_msg = "Error de conexión"
                    break

                self.progress.emit(i + len(chunk), total)  
                requests_count += 1
                time.sleep(1)  

            self.upload_finished.emit(is_successful, error_msg)

        except Exception as e:
            self.upload_finished.emit(False, str(e))
    
    def convert_keys(self, param_dict: dict) -> dict:
        return {
            "id": param_dict["id"],
            "name": param_dict["name"],
            "deviceId": param_dict["device_id"],  
            "latitude": param_dict["latitude"],
            "longitude": param_dict["longitude"],
            "date": param_dict["date"],
            "hour": param_dict["hour"],
            "conductivity": param_dict["conductivity"],
            "oxygen": param_dict["oxygen"],
            "ph": param_dict["ph"],
            "tds": param_dict["tds"],
            "temperature": param_dict["temperature"],
            "turbidity": param_dict["turbidity"],
            "battery": param_dict["battery"],
            "sampleOrigin": param_dict["sample_origin"],  
            "itRained": param_dict["it_rained"],  
            "uploadState": param_dict["upload_state"],  
            "loteId": param_dict["lote_id"]  
        }

