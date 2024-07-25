import sys
import struct
import time
import random
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QSize, QThread, Signal, Slot
from PySide2.QtGui import QIcon, QPixmap
from src.views.ui_Main import Ui_MainWindow
from src.views.ui_Monitoring import Ui_Monitoring
from src.views.ui_Bluetooth import Ui_Bluetooth
from src.views.ui_Datos import Ui_Datos
from src.views.ui_Calibration import Ui_Calibration
from bluepy.btle import Peripheral, UUID, Service, Characteristic, DefaultDelegate, Advertisement

class QualityService(Service):
    QUALITY_UUID = UUID("12345678-1234-5678-1234-56789abcdef0")
    CHAR_UUID = UUID("12345678-1234-5678-1234-56789abcdef1")

    def __init__(self, conn):
        Service.__init__(self, conn, self.QUALITY_UUID)
        self.addCharacteristic(QualityCharacteristic(conn, self.CHAR_UUID))

class QualityCharacteristic(Characteristic):
    def __init__(self, conn, uuid):
        Characteristic.__init__(self, uuid, props=Characteristic.propRead | Characteristic.propNotify, val=b'\x00\x00\x00\x00')
        self.conn = conn

    def getQualityData(self):
        tds = round(random.uniform(500.0, 601.0), 2)
        temp = round(random.uniform(28.9, 29.9), 2)
        ph = round(random.uniform(4.0, 7.0), 2)
        data = struct.pack('fff', tds, temp, ph)
        self.setValue(data)

    def Read(self, maxLen):
        self.getQualityData()
        return self.value

class BLEServiceThread(QThread):
    notification_received = Signal(bytes)
    connection_status = Signal(str)

    def __init__(self):
        super().__init__()
        self.running = False
        self.peripheral = None
        self.advertisement = CustomAdvertisement(name="WATER_QUALITY_B")

    def run(self):
        self.running = True
        self.peripheral = Peripheral()
        self.peripheral.addService(QualityService(self.peripheral))
        self.peripheral.setDelegate(ConnectionDelegate(self))

        print("BLE service started. Waiting for connections...")
        while self.running:
            if self.peripheral.waitForNotifications(1.0):
                continue
        if self.peripheral:
            self.peripheral.disconnect()

    def stop(self):
        self.running = False
        if self.peripheral:
            self.peripheral.disconnect()

class ConnectionDelegate(DefaultDelegate):
    def __init__(self, params):
        DefaultDelegate.__init__(self)
        self.params = params

    def handleNotification(self, cHandle, data):
        self.params.notification_received.emit(data)
        print(f"Notification from handle: {cHandle} with data: {data}")

    def handleConnected(self, dev):
        self.params.connection_status.emit(f"Device {dev.addr} connected")

    def handleDisconnected(self, dev):
        self.params.connection_status.emit(f"Device {dev.addr} disconnected")

class ParametersMeasuredWorker(QThread):
    parameters_result = Signal(list)

    def __init__(self):
        super(ParametersMeasuredWorker, self).__init__()

    def run(self):
        self.running_state = True
        while self.running_state:
            try:
                ph = round(random.uniform(4.0, 7.0), 2)
                do = round(random.uniform(6.0, 7.0), 2)
                tds = round(random.uniform(500.0, 601.0), 2)
                temp = round(random.uniform(28.9, 29.9), 2)
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

        self.ble_service_thread = BLEServiceThread()
        self.ble_service_thread.notification_received.connect(self.handle_notification_received)
        self.ble_service_thread.connection_status.connect(self.handle_connection_status)
        self.ble_service_thread.start()

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
