from PySide2.QtCore import QThread, Signal
import socket

class InternetChecker(QThread):
    connection_status = Signal(bool)

    def run(self):
        try:
            # Intenta conectar al servidor de Google
            with socket.create_connection(("www.google.com", 80), timeout=3) as sock:
                self.connection_status.emit(True)  # Conexión exitosa
                # Aquí puedes realizar operaciones adicionales si es necesario
        except OSError:
            self.connection_status.emit(False)  # Sin conexión