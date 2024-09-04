import sys
import time
import RPi.GPIO as GPIO
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QThread, Signal
from src.views.ui_Main import Ui_MainWindow
from src.views.MonitoringView.MonitoringView import MonitoringView
from src.views.CalibrationView.CalibrationView import CalibrationView
from src.views.DatosView.DatosView import DatosView
from src.views.BluetoothView.BluetoothView import BluetoothView


class ButtonListener(QThread):
    button_pressed = Signal()

    def __init__(self, button_pin):
        super(ButtonListener, self).__init__()
        self.button_pin = button_pin
        self.app = app
        self.running = True

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN)

    def run(self):
            try:
                while self.running:
                    if GPIO.input(self.button_pin) == GPIO.LOW:
                        time.sleep(0.3) 
                        if GPIO.input(self.button_pin) == GPIO.LOW:
                            print('SE PRESIONO EL BOTON')
                            self.button_pressed.emit()
                    time.sleep(0.01)
            except GPIO.error as e:
                print(f"Error con GPIO: {e}")
            finally:
                self.running = False
                GPIO.cleanup()

    def stop(self):
        self.running = False
        GPIO.cleanup()


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
        self.open_view(MonitoringView(context=widget))

    def on_calibration_clicked(self):
        self.open_view(CalibrationView(context=widget))

    def on_datos_clicked(self):
        self.open_view(DatosView(context=widget))

    def on_bluetooth_clicked(self):
        self.open_view(BluetoothView(context=widget))

    def open_view(self, view):
        widget.addWidget(view)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def switch_to_bluetooth_view(self):
        if widget.currentIndex() > 0:
            current_widget = widget.currentWidget()
            widget.removeWidget(current_widget)
            current_widget.deleteLater()
        self.on_bluetooth_clicked()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome = MyApp()
    button_pin = 17
    button_listener = ButtonListener(button_pin)
    button_listener.button_pressed.connect(welcome.switch_to_bluetooth_view)
    button_listener.start()
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
    finally:
        button_listener.stop()
