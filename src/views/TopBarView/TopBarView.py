from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QTimer
from PySide2.QtGui import QPixmap
from src.views.ui_Top_Bar import Ui_Form
from src.logic.INA219 import INA219


class TopBarView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        pixmap = QPixmap('./src/resources/icons/batteryIcon.png')
        self.ui.batLblPng.setPixmap(pixmap)

        pixmap = QPixmap('./src/resources/icons/electric_bolt.png')
        scaled_pixmap = pixmap.scaled(28, 28, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.chargeLbl.setPixmap(scaled_pixmap)

        self.ui.chargeLbl.hide()

        self.ina219 = INA219(addr=0x42)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_battery_level)
        self.timer.start(1000)


    def get_battery_level(self):
        bus_voltage = self.ina219.getBusVoltage_V()
        current = self.ina219.getCurrent_mA()
        p = int((bus_voltage - 6)/2.4*100)
        if (p > 100):
            p = 100
        if (p < 0):
            p = 0
        self.update_battery(battery_level= p)
        self.charge_indicator(current= current)
    
    def charge_indicator(self, current):
        if(current < 0):
            self.ui.chargeLbl.show()
        else:
            self.ui.chargeLbl.hide()


    def update_battery(self, battery_level):
        self.ui.batLbl.setText(f'{round(battery_level)}%')
        self.ui.batLbl.setAlignment(QtCore.Qt.AlignCenter)
        if (battery_level < 20):
            self.ui.batLblBg.setStyleSheet('background-color: #fb8b24;')
        move_level = round(-0.39 * battery_level + 47)
        self.ui.batLblBg.move(367 + move_level, 10)
