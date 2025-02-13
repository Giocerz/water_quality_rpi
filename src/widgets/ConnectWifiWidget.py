from PySide2.QtWidgets import QDialog, QApplication, QGraphicsOpacityEffect, QStackedLayout, QWidget
from PySide2 import QtCore
from src.views.ui_WifiConnect import Ui_Form
import src.views.ui_WifiConnected as Ui_Saved_Wifi
from src.widgets.KeyboardWidget import KeyboardWidget
from src.services.wifiService import WifiService
from src.widgets.PopupWidget import PopupWidgetInfo

class ConnectWifiWidget(QWidget):
    def __init__(self, context, ssid:str, security:str, connect_callback:callable):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.context = context
        self.ssid:str = ssid
        self.security:str = security
        self.connect_callback:callable = connect_callback
        self.init_ui_components()

        self.ui.lblOpacity.mousePressEvent = self.background_clicked
        self.ui.connectBtn.clicked.connect(self.connect_is_clicked)

    def init_ui_components(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.keyboard = KeyboardWidget(self.ui.inputPlace)
        layout = QStackedLayout(self.ui.widgetKeyboard)
        layout.addWidget(self.keyboard)
        self.ui.widgetKeyboard.setLayout(layout)
        self.ui.ssidLbl.setText(self.ssid)
        self.ui.ssidLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.setParent(self.context)

    def connect_is_clicked(self):
        pwd = self.ui.inputPlace.text()
        if len(pwd) < 8:
            popup = PopupWidgetInfo(context=self.context, text="Ingrese una contraseña válida")
            popup.show()
            self.ui.inputPlace.setText("")
            return
        self.connect_callback(self.ssid, pwd)
        self.close_and_delete()
        
    def background_clicked(self, event):
        self.close_and_delete()  

    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()

class SavedWifiWidget(QWidget):
    def __init__(self, context, ssid:str, is_connected:bool, forget_callback:callable, connect_callback:callable = None, disconnect_callback:callable = None):
        super().__init__()
        self.ui = Ui_Saved_Wifi.Ui_Form()
        self.ui.setupUi(self)
        self.context = context
        self.ssid:str = ssid
        self.is_connected:str = is_connected
        self.forget_callback:callable = forget_callback
        self.connect_callback:callable = connect_callback
        self.disconnect_callback:callable = disconnect_callback
        self.init_ui_components()

        self.ui.lblOpacity.mousePressEvent = self.background_clicked
        self.ui.connectBtn.clicked.connect(self.connect_is_clicked)
        self.ui.disconnectBtn.clicked.connect(self.disconnect_is_clicked)
        self.ui.forgetBtn.clicked.connect(self.forget_is_clicked)

    def init_ui_components(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.ui.ssidLbl.setText(self.ssid)
        self.ui.ssidLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.connectBtn.hide()
        self.ui.disconnectBtn.hide()

        if self.is_connected:
            self.ui.disconnectBtn.show()
        else:
            self.ui.connectBtn.show()

        self.setParent(self.context)

    def connect_is_clicked(self):
        if not self.connect_callback:
            return
        self.connect_callback(self.ssid)
        self.close_and_delete()
    
    def disconnect_is_clicked(self):
        if not self.disconnect_callback:
            return
        self.disconnect_callback(self.ssid)
        self.close_and_delete()

    def forget_is_clicked(self):
        self.forget_callback(self.ssid)
        self.close_and_delete()
        
    def background_clicked(self, event):
        self.close_and_delete()  

    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()