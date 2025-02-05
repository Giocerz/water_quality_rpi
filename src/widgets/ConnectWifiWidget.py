from PySide2.QtWidgets import QDialog, QApplication, QGraphicsOpacityEffect, QStackedLayout, QWidget
from PySide2 import QtCore
from src.views.ui_WifiConnect import Ui_Form
from src.widgets.KeyboardWidget import KeyboardWidget
from src.services.wifiService import WifiService
from src.widgets.PopupWidget import PopupWidgetInfo

class ConnectWifiWidget(QWidget):
    def __init__(self, context, ssid:str, security:str, is_connect:bool, connect_callback):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.context = context
        self.ssid:str = ssid
        self.security:str = security
        self.is_connect:bool = is_connect
        self.connect_callback = connect_callback
        self.init_ui_components()

        self.ui.lblOpacity.mousePressEvent = self.close_and_delete
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
        self.ui.widgetKeyboard.hide()
        self.ui.Widget1.hide()
        self.ui.Widget2.hide()
        self.ui.ssidLbl.setText(self.ssid)
        self.ui.ssidLbl2.setText(self.ssid)

        if self.is_connect:
            self.ui.Widget2.show()
            self.ui.ssidLbl2.setText(self.ssid)
            self.ui.ssidLbl2.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.firstBtn.setText("Desconectar")
        else:
            is_saved = WifiService.is_network_saved(self.ssid)
            if is_saved:
                self.ui.Widget2.show()
                self.ui.ssidLbl2.setText(self.ssid)
                self.ui.ssidLbl2.setAlignment(QtCore.Qt.AlignCenter)
                self.ui.firstBtn.setText("Conectar")
            else:
                self.ui.widgetKeyboard.show()
                self.ui.Widget1.show()
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
        
        

    def close_and_delete(self, event):
        self.setParent(None)
        self.deleteLater()