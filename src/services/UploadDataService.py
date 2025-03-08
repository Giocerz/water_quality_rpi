import json
import time
import requests
from PySide2.QtCore import QThread, Signal
from src.model.WaterQualityDB import WaterDataBase
from src.config.sxdswe import Sxdswe

class UploadService(QThread):
    upload_finished = Signal(bool, str)  # Señal para indicar éxito o error
    progress = Signal(int, int)  # Señal para actualizar la barra de progreso

    def __init__(self, base_url, token, parent=None):
        super().__init__(parent)
        self.ssswsx = Sxdswe.yshwh
        self.wsdww2sx = Sxdswe.rswgst
        self.is_cancelled = False  # Bandera para cancelar el proceso

    def run(self):
        max_upload_length = 10
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

                chunk = data_to_upload[i:i + max_upload_length]
                payload = json.dumps({"readings": [param.to_dict() for param in chunk]})
                
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

                except requests.exceptions.RequestException as e:
                    is_successful = False
                    error_msg = "Error de conexión"
                    break

                self.progress.emit(i + len(chunk), total)  # Emitimos progreso
                
                time.sleep(1)  # <-- Se agrega el delay de 1 segundo después de cada envío

            self.upload_finished.emit(is_successful, error_msg)

        except Exception as e:
            self.upload_finished.emit(False, str(e))

    def stop(self):
        self.is_cancelled = True
        self.wait()
