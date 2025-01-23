from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QTimer, QSize
from PySide2.QtGui import QPixmap
from src.views.ui_Top_Bar import Ui_Form
from src.widgets.PopupWidget import PopupWidgetInfo
from src.logic.INA219 import INA219
from datetime import datetime


class TopBarView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.low_battery_flag = False

        pixmap = QPixmap('./src/resources/icons/electric_bolt_b.png')
        scaled_pixmap = pixmap.scaled(26, 26, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.chargeIndicator.setPixmap(scaled_pixmap)

        self.ui.chargeIndicator.hide()

        self.ina219 = INA219(addr=0x42)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_battery_level)
        self.timer.start(1000)

    def update_top_bar(self):
        self.get_battery_level()
        self.update_time()
        self.update_wifi_state()

    def update_wifi_state(self):
        pixmap = QPixmap('./src/resources/icons/wifi_icons/wifi_off.png')
        scaled_pixmap = pixmap.scaled(QSize(31, 31))
        self.ui.networkLbl.setPixmap(scaled_pixmap)
    
    def update_time(self):
        hour = datetime.now().strftime("%H:%M")
        self.ui.timeLbl.setText(hour)

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
        if(current > 0):
            self.ui.chargeIndicator.show()
        else:
            self.ui.chargeIndicator.hide()


    def update_battery(self, battery_level):
        self.ui.batteryLbl.setText(f'{round(battery_level)}%')
        self.ui.batteryLbl.setAlignment(QtCore.Qt.AlignLeft)

        if(battery_level < 25 and battery_level >= 10):
            color = '252, 163, 17'
            if(not self.low_battery_flag):
                self.open_battery_popup()
                self.low_battery_flag = True
        elif(battery_level < 10):
            color = '230, 57, 70'
        else:
            color = '0, 0, 127'
            self.low_battery_flag = False

        if(battery_level == 100):
            percent = 0
        elif(battery_level == 0):
            percent =0.95
        else:
            percent = round((-0.81633 * battery_level + 90.81633)/100.0, 2)

        self.ui.baterryLevel.setStyleSheet(f'background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,stop:0 rgba(255, 255, 255, 255),stop:{percent} rgba(255, 255, 255, 255), stop:{percent + 0.01} rgba({color}, 255), stop:1 rgba({color}, 255));border-radius: 12px;')

    def open_battery_popup(self):
        popup = PopupWidgetInfo(context=self.context,text='Batería baja, conecte el cargador')
        popup.show()