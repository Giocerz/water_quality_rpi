from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize, Qt, QThread, Signal, QTimer
from PySide2.QtGui import QIcon, QStandardItemModel, QStandardItem
from src.views.ui_WifiList import Ui_MainWindow
from src.widgets.PopupWidget import LoadingPopupWidget, PopupWidgetInfo
from src.widgets.ConnectWifiWidget import ConnectWifiWidget, SavedWifiWidget
from src.services.wifiService import WifiService
from src.package.Navigator import Navigator
from src.package.Timer import Timer


class WifiView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.connected_item_id:int = None #Saber que item de la lista esta conectado
        self.timer:Timer = None
        self.current_index:int = 0 #Saber que item se selecciono
        self.current_ssid: str = None
        self.try_connect_id:int = 0

        self.check_count = 0  # Contador de intentos
        self.max_checks = 30 // 2 

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
        self.timer = Timer(3000, self.update_networks)
        self.timer.start()

    def on_back_clicked(self):
        if self.timer:
            self.timer.cancel()
        Navigator.pop(context= self.context, view=self)

    def update_networks(self):
        self.ui.infoLbl.hide()
        self.items = WifiService.scan_results()
        self.update_wifi_list(self.items)
    
    def update_wifi_list(self, items:list):
        if items != []:
            self.model = QStandardItemModel()
            for index, item in enumerate(items):
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
                    self.connected_item_id = index
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
            numRedes = len(items)
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
        self.current_index = indexes[0].row()
        self.open_connection_widget()
    
    #ABRIR EL WIDGET DE CONEXION
    def open_connection_widget(self):
        ssid = self.items[self.current_index]["ssid"]
        self.current_ssid = ssid
        security = self.items[self.current_index]["security"]
        is_connected = self.items[self.current_index]["connect"]
        is_saved = WifiService.is_network_saved(ssid)
        if is_saved:
            self.connect_popup = SavedWifiWidget(context= self.context, ssid=ssid, is_connected=is_connected, 
                                                 forget_callback=self.forget_network, connect_callback=self.connect_saved_network,
                                                 disconnect_callback=self.disconnect_network)
            self.connect_popup.show()
        else:
            self.connect_popup = ConnectWifiWidget(context=self.context, ssid=ssid, security=security, connect_callback=self.connect_network)
            self.connect_popup.show()
        
    
    #FUNCIONES PARA NUEVA CONEXION
    def connect_network_result(self):
        """Verifica si la conexión fue exitosa y detiene el timer si es necesario."""
        result = WifiService.verify_network(self.current_ssid)
        if result:
            self.timer.cancel()  # Detener el timer si se conectó
            if self.connected_item_id:
                self.items[self.connected_item_id]["connect"] = False
            self.items[self.current_index]["connect"] = True
            self.connected_item_id = self.current_index
            self.update_wifi_list(self.items)
            self.loading_popup.close_and_delete()
        else:
            self.check_count += 1
            if self.check_count >= self.max_checks:
                # Si se agotaron los intentos, cancelar e intentar otra red
                self.check_count = 0
                self.timer.cancel()
                WifiService.delete_network_by_id(self.try_connect_id)
                self.loading_popup.close_and_delete()
                self.open_connection_widget()
                popup = PopupWidgetInfo(context=self.context, text="No se pudo conectar")
                popup.show()

    def connect_network(self, ssid:str, psk:str):
        self.loading_popup = LoadingPopupWidget(context=self.context, text="Conectando")
        self.loading_popup.show()
        self.try_connect_id = WifiService.add_network(ssid, psk)
        if self.try_connect_id != -1:
            self.timer = Timer.periodic(duration=2000, callback= self.connect_network_result)
            self.timer.start()
        else:
            self.loading_popup.close_and_delete()
            self.open_connection_widget()
            popup = PopupWidgetInfo(context=self.context, text="Error de conexión")
            popup.show()
    
    #FUNCIONES SI LA RED ESTA GUARDADA
    #Olvidar red
    def forget_network(self, ssid:str):
        result = WifiService.delete_network(ssid)
        if result:
            popup = PopupWidgetInfo(context=self.context, text="Red eliminada")
        else:
            popup = PopupWidgetInfo(context=self.context, text="Error al eliminar")
        popup.show()
    
    def disconnect_network(self, ssid:str):
        result = WifiService.disconnect_network(ssid)
        if result:
            popup = PopupWidgetInfo(context=self.context, text="Red desconectada")
        else:
            popup = PopupWidgetInfo(context=self.context, text="Error al desconectar")
        popup.show()
    
    def connect_saved_network(self, ssid:str):
        self.loading_popup = LoadingPopupWidget(context=self.context, text="Conectando")
        self.loading_popup.show()
        result = WifiService.connect_network(ssid)
        if result:
            self.timer = Timer.periodic(duration=2000, callback= self.connect_saved_network_result)
            self.timer.start()
        else:
            self.loading_popup.close_and_delete()
            self.open_connection_widget()
            popup = PopupWidgetInfo(context=self.context, text="Error de conexión")
            popup.show()

    def connect_saved_network_result(self):
        """Verifica si la conexión fue exitosa y detiene el timer si es necesario."""
        result = WifiService.verify_network(self.current_ssid)
        if result:
            self.timer.cancel()  # Detener el timer si se conectó
            if self.connected_item_id:
                self.items[self.connected_item_id]["connect"] = False
            self.items[self.current_index]["connect"] = True
            self.connected_item_id = self.current_index
            self.update_wifi_list(self.items)
            self.loading_popup.close_and_delete()
        else:
            self.check_count += 1
            if self.check_count >= self.max_checks:
                # Si se agotaron los intentos, cancelar e intentar otra red
                self.check_count = 0
                self.timer.cancel()
                WifiService.disconnect_network(self.current_ssid)
                self.loading_popup.close_and_delete()
                self.open_connection_widget()
                popup = PopupWidgetInfo(context=self.context, text="No se pudo conectar")
                popup.show()