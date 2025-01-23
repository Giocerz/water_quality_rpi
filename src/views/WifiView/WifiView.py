import subprocess
import time
import random
from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QTimer, QSize, Qt, QThread, Signal
from PySide2.QtGui import QPixmap, QIcon, QStandardItemModel, QStandardItem
from src.views.ui_Top_Bar import Ui_Form
from src.views.ui_WifiList import Ui_MainWindow
from src.widgets.PopupWidget import LoadingPopupWidget


class WifiView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        # Inicializacion del hilo del wifi
        self.wifi_thread_find = WifiWorkerFind()

        self.wifi_thread_find.networks_result.connect(self.actualizar_redes)
        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.verticalSlider.valueChanged.connect(self.slider_value_changed)

        self.scrollBar.rangeChanged.connect(self.adjust_slider_range)
        self.scrollBar.valueChanged.connect(self.scroll_value_changed)
        self.wifi_thread_find_start()

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        self.scrollBar = self.ui.networkList.verticalScrollBar()
        self.ui.verticalSlider.setRange(
            self.scrollBar.minimum(), self.scrollBar.maximum())
        self.ui.verticalSlider.hide()
        self.ui.infoLbl.hide()

    def showEvent(self, event):
        """Muestra el popup de carga después de que la ventana principal sea visible."""
        super(WifiView, self).showEvent(event)
        self.loading_popup = LoadingPopupWidget(
            context=self.context, text='Buscando redes...')
        self.loading_popup.show()
        self.wifi_thread_find_start()

    def on_back_clicked(self):
        self.context.removeWidget(self)

    def wifi_thread_find_start(self):
        if not self.wifi_thread_find.isRunning():
            self.wifi_thread_find.start()

    def actualizar_redes(self, new_result):
        self.ui.infoLbl.hide()
        self.elementos = new_result
        if self.elementos != []:
            self.model = QStandardItemModel()
            for elemento in self.elementos:
                if (elemento['security'] != ''):
                    seguridad = 1
                else:
                    seguridad = 0

                if (100 + elemento['signal'] > 75):
                    signal_quality = 4
                elif (100 + elemento['signal'] > 50):
                    signal_quality = 3
                elif (100 + elemento['signal'] > 25):
                    signal_quality = 2
                else:
                    signal_quality = 1

                if (elemento['frequency'] > 5000):
                    frec = 1
                else:
                    frec = 0

                if elemento["connect"]:
                    cadenaElemento = elemento['ssid'] + " - Conectada"
                else:
                    cadenaElemento = elemento['ssid']
                item = QStandardItem(cadenaElemento)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

                # Combinacion del icono
                # wifi_### Primer valor: seguridad, segundo: Frec, tercero: señal
                icon_path_name = "./src/resources/icons/wifi_icons/wifi_{}{}".format(
                    seguridad, signal_quality)
                icon = QIcon(icon_path_name)
                item.setIcon(icon)
                self.model.appendRow(item)
            self.ui.networkList.setModel(self.model)
            self.ui.networkList.setIconSize(QSize(26, 26))
            numRedes = len(self.elementos)
        else:
            self.ui.infoLbl.show()
        self.loading_popup.close_and_delete()

    def slider_value_changed(self, value):
        self.scrollBar.setValue(value)

    def adjust_slider_range(self, min, max):
        print(f'MAX: {max} MIN: {min}')
        self.ui.verticalSlider.show()
        self.ui.verticalSlider.setRange(min, max)

    def scroll_value_changed(self, value):
        self.ui.verticalSlider.setValue(value)


# Hilo wifi

class WifiWorkerFind(QThread):
    networks_result = Signal(list)

    def __init__(self):
        super(WifiWorkerFind, self).__init__()
        self.wifi = WifiControl()

    def run(self):
        networks_list = self.wifi.list_wifi_networks()
        self.networks_result.emit(networks_list)


class WifiWorkerConnect(QThread):
    wifi_connected = Signal(bool)

    def __init__(self, ssid="", password=""):
        super(WifiWorkerConnect, self).__init__()
        self.wifi = WifiControl()
        self.ssid = ssid
        self.password = password

    def run(self):
        result = self.wifi.connect_wifi(self.ssid, self.password)
        self.wifi_connected.emit(result)


# Objeto wifiControl
class WifiControl:
    def __init__(self):
        pass

    def list_wifi_networks(self) -> dict:
        time.sleep(1)
        ok = subprocess.check_output(
            "sudo wpa_cli scan", shell=True).decode("utf-8")
        if 'OK' not in ok:
            return []
        lines = subprocess.check_output(
            "sudo wpa_cli scan_results", shell=True).decode("utf-8")
        current_network = subprocess.check_output(
            "sudo iwgetid -r", shell=True).decode("utf-8").strip()
        lines: list = lines.split("\n")[2:]
        if len(lines) == 0:
            return []
        networks_dict = {}
        for line in lines:
            columns = line.split("\t")
            if len(columns) >= 5:
                bssid = columns[0]
                frequency = int(columns[1])
                signal_level = int(columns[2])
                flags = columns[3]
                ssid = columns[4]
                
                if ssid not in networks_dict or signal_level > networks_dict[ssid]["signal"]:
                    networks_dict[ssid] = {
                        "BSSID": bssid,
                        "frequency": frequency,
                        "signal": signal_level,
                        "security": flags,
                        "ssid": ssid,
                        "connect": ssid == current_network
                    }
        return list(networks_dict.values())

    def connect_wifi(self, ssid, password=""):
        time.sleep(2)
        if password == "@WATCH_DRIVE Proj" or password == "":
            return True
        else:
            return False


"""
import random
import time

#Hilo wifi
class WifiWorkerFind(QThread):
    networks_result = Signal(list)

    def __init__(self):
        super(WifiWorkerFind, self).__init__()
        self.wifi = WifiControl()

    def run(self):
        networks_list = self.wifi.list_wifi_networks()
        self.networks_result.emit(networks_list)
            

class WifiWorkerConnect(QThread):
    wifi_connected = Signal(bool)

    def __init__(self, ssid = "", password = ""):
        super(WifiWorkerConnect, self).__init__()
        self.wifi = WifiControl()
        self.ssid = ssid
        self.password = password

    def run(self):
        result = self.wifi.connect_wifi(self.ssid, self.password)
        self.wifi_connected.emit(result)           
        

#Objeto wifiControl
class WifiControl:
    def __init__(self):
        pass

    def list_wifi_networks(self):
        time.sleep(1)
        proveedores_internet = ['Estudiantes', 'Unicesar_docentes', 'DSP-ASIC-BUILDER', 'ERES POBRE', 'Iphone de Marie Curie', 'Wifi_Del_vecino']
        arreglo_diccionarios = []
        rango = random.randint(0,15)
        for i in range(rango):
            ssid = random.choice(proveedores_internet)
            proveedores_internet.remove(ssid)
            signal = random.randint(1, 100)
            security = random.choice(['wp2', ''])
            frequency = random.choice(['5400 MHz', '2400 MHz'])
            diccionario = {'ssid': ssid, 'signal': signal, 'security': security, 'frequency': frequency}
            arreglo_diccionarios.append(diccionario)
        
        return arreglo_diccionarios

    def connect_wifi(self, ssid, password=""):
        time.sleep(2)
        if password == "@WATCH_DRIVE Proj" or password == "":
            return True
        else:
            return False
"""
