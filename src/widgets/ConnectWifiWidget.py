from PySide2.QtWidgets import QDialog, QApplication, QGraphicsOpacityEffect, QStackedLayout, QWidget
from PySide2 import QtCore
from src.views.ui_WifiConnect import Ui_Form
from src.widgets.KeyboardWidget import KeyboardWidget

class ConnectWifiWidget(QWidget):
    def __init__(self, context, ssid:str, security:str, is_connect:bool):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.context = context
        self.ssid:str = ssid
        self.security:str = security
        self.is_connect:bool = is_connect
        self.init_ui_components()

        self.adjust_size_and_center()
        self.ui.lblOpacity.mousePressEvent = self.close_and_delete

    def init_ui_components(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.keyboard = KeyboardWidget(self.ui.inputPlace)
        layout = QStackedLayout(self.ui.widgetKeyboard)
        layout.addWidget(self.keyboard)
        self.ui.widgetKeyboard.setLayout(layout)
        self.ui.Widget1.hide()
        self.ui.Widget2.hide()
        self.ui.ssidLbl.setText(self.ssid)
        self.ui.ssidLbl2.setText(self.ssid)

        if self.is_connect:
            self.ui.Widget2.show()
            self.ui.ssidLbl2.setText(self.ssid)
            self.ui.ssidLbl2.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.firstBtn.setText("Desconectar")
            self.ui.widgetKeyboard.hide()
        else:
            self.ui.Widget1.show()
            self.ui.ssidLbl.setText(self.ssid)
            self.ui.ssidLbl.setAlignment(QtCore.Qt.AlignCenter)

    def adjust_size_and_center(self):
        screen_rect = QApplication.desktop().availableGeometry()
        screen_width = screen_rect.width()
        screen_height = screen_rect.height()
        dialog_width = 480
        dialog_height = 320
        x = (screen_width - dialog_width) / 2
        y = (screen_height - dialog_height) / 2
        self.move(int(x), int(y))

    def close_and_delete(self, event):
        self.setParent(None)
        self.deleteLater()