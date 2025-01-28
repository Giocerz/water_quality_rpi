from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize, Qt, QThread, Signal, QTimer
from PySide2.QtGui import QIcon, QStandardItemModel, QStandardItem
from src.views.ui_WifiList import Ui_MainWindow
from src.widgets.PopupWidget import LoadingPopupWidget
from src.widgets.ConnectWifiWidget import ConnectWifiWidget
from src.services.wifiService import WifiService
from src.package.Navigator import Navigator


class WifiView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.verticalSlider.valueChanged.connect(self.slider_value_changed)
        self.ui.networkList.clicked.connect(self.select_network)

        self.scrollBar.rangeChanged.connect(self.adjust_slider_range)
        self.scrollBar.valueChanged.connect(self.scroll_value_changed)

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
        WifiService.scan()
        QTimer.singleShot(3000, self.update_networks)


    def on_back_clicked(self):
        Navigator.pop(context= self.context, view=self)

    def update_networks(self):
        self.ui.infoLbl.hide()
        self.items = WifiService.scan_results()
        if self.items != []:
            self.model = QStandardItemModel()
            for item in self.items:
                if (item['security'] != ''):
                    seguridad = 1
                else:
                    seguridad = 0

                if (100 + item['signal'] > 75):
                    signal_quality = 4
                elif (100 + item['signal'] > 50):
                    signal_quality = 3
                elif (100 + item['signal'] > 25):
                    signal_quality = 2
                else:
                    signal_quality = 1

                if (item['frequency'] > 5000):
                    frec = 1
                else:
                    frec = 0

                if item["connect"]:
                    cadenaElemento = item['ssid'] + "-Conectada"
                else:
                    cadenaElemento = item['ssid']
                standard_item = QStandardItem(cadenaElemento)
                standard_item.setFlags(standard_item.flags() & ~Qt.ItemIsEditable)

                # Combinacion del icono
                # wifi_### Primer valor: seguridad, segundo: Frec, tercero: señal
                icon_path_name = "./src/resources/icons/wifi_icons/wifi_{}{}".format(
                    seguridad, signal_quality)
                icon = QIcon(icon_path_name)
                standard_item.setIcon(icon)
                self.model.appendRow(standard_item)
            self.ui.networkList.setModel(self.model)
            self.ui.networkList.setIconSize(QSize(26, 26))
            numRedes = len(self.items)
        else:
            self.ui.infoLbl.show()
        self.loading_popup.close_and_delete()

    def slider_value_changed(self, value):
        self.scrollBar.setValue(value)

    def adjust_slider_range(self, min, max):
        self.ui.verticalSlider.show()
        self.ui.verticalSlider.setRange(min, max)

    def scroll_value_changed(self, value):
        self.ui.verticalSlider.setValue(value)
    
    def select_network(self):
        indexes = self.ui.networkList.selectedIndexes()
        index = indexes[0].row()
        ssid = self.items[index]["ssid"]
        security = self.items[index]["security"]
        is_connect = self.items[index]["connect"]
        self.connect_popup = ConnectWifiWidget(context=self.context, ssid=ssid, security=security, is_connect=is_connect)
        self.connect_popup.show()


# Hilo wifi

class WifiWorkerFind(QThread):
    networks_result = Signal(list)

    def __init__(self):
        super(WifiWorkerFind, self).__init__()

    def run(self):
        networks_list = WifiService.list_wifi_networks()
        self.networks_result.emit(networks_list)

# Objeto wifiControl


    """
    
    def list_wifi_networks(self) -> dict:
        time.sleep(1)
        return [
            {
                'ssid': "WIFI DE SUS",
                'security': "WPA",
                'signal': -56,
                'frequency': 5463,
                'connect': True
            },
            {
                'ssid': "VECINO",
                'security': "WPA",
                'signal': -76,
                'frequency': 5463,
                'connect': False
            },
            {
                'ssid': "Xsudhw",
                'security': "",
                'signal': -26,
                'frequency': 5463,
                'connect': False
            },
        ]
"""


