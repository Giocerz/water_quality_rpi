import sys
import struct
import time
import random
import board
import busio
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QSize, QThread, Signal, Slot
from PySide2.QtGui import QIcon, QPixmap
from src.views.ui_Main import Ui_MainWindow
from src.views.ui_Monitoring import Ui_Monitoring
from src.views.ui_Bluetooth import Ui_Bluetooth
from src.views.ui_Datos import Ui_Datos
from src.views.ui_Calibration import Ui_Calibration
from w1thermsensor import W1ThermSensor
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from src.modules.parametersCalc import *

class ParametersMeasuredWorker(QThread):
    parameters_result = Signal(list)

    def __init__(self):
        super(ParametersMeasuredWorker, self).__init__()

    def run(self):
        self.running_state = True
        temperature_sensor = W1ThermSensor()
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
        ads.gain = 2/3
        tds_channel = AnalogIn(ads, ADS.P0)
        ph_channel = AnalogIn(ads, ADS.P1)
        while self.running_state:
            try:
                temp = round(temperature_sensor.get_temperature(), 2)
                ph = round(calculatePh(ph_channel.voltage), 2)
                do = round(random.uniform(6.0, 7.0), 2)
                tds = round(calculateTds(temp, tds_channel.voltage), 2)
                self.parameters_result.emit([ph, do, tds, temp])
                time.sleep(1)
            except Exception as e:
                print(e)

    def stop(self):
        self.running_state = False
        self.wait()

class MyApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.monitoringBtn.clicked.connect(self.on_monitoring_clicked)
        self.ui.calibrationBtn.clicked.connect(self.on_calibration_clicked)
        self.ui.dataBtn.clicked.connect(self.on_datos_clicked)
        self.ui.bluetoothBtn.clicked.connect(self.on_bluetooth_clicked)

    def on_monitoring_clicked(self):
        self.open_view(MonitoringView())

    def on_calibration_clicked(self):
        self.open_view(CalibrationView())

    def on_datos_clicked(self):
        self.open_view(DatosView())

    def on_bluetooth_clicked(self):
        self.open_view(BluetoothView())

    def open_view(self, view):
        widget.addWidget(view)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class MonitoringView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Monitoring()
        self.ui.setupUi(self)
        self.ui_components()

        self.parameters_worker = ParametersMeasuredWorker()
        if not self.parameters_worker.isRunning():
            self.parameters_worker.start()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

        self.parameters_worker.parameters_result.connect(self.handle_parameters_result)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/save.png')
        self.ui.saveBtn.setIcon(icon)
        self.ui.saveBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        if self.parameters_worker.isRunning():
            self.parameters_worker.stop()
        widget.removeWidget(self)

    def handle_parameters_result(self, parameters):
        self.ui.phLbl.setText(str(parameters[0]))
        self.ui.phLbl.setAlignment(QtCore.Qt.AlignHCenter)
        self.ui.odLbl.setText(str(parameters[1]))
        self.ui.odLbl.setAlignment(QtCore.Qt.AlignHCenter)
        self.ui.tdsLbl.setText(str(parameters[2]))
        self.ui.tdsLbl.setAlignment(QtCore.Qt.AlignHCenter)
        self.ui.tempLbl.setText(str(parameters[3]))
        self.ui.tempLbl.setAlignment(QtCore.Qt.AlignHCenter)
        self.ui.ecLbl.setText(str(parameters[2] * 2))
        self.ui.ecLbl.setAlignment(QtCore.Qt.AlignHCenter)

class CalibrationView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Calibration()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        widget.removeWidget(self)

class DatosView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Datos()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        widget.removeWidget(self)

class BluetoothView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Bluetooth()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        self.ble_service_thread.stop()
        widget.removeWidget(self)

    @Slot(bytes)
    def handle_notification_received(self, data):
        print(f"Received data: {data}")

    @Slot(str)
    def handle_connection_status(self, status):
        print(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome = MyApp()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(320)
    widget.setFixedWidth(480)
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exit")
