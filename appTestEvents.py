import sys
# import struct
import time
import random
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QSize, QThread, Signal, Slot, QTimer, Qt, QEvent
from PySide2.QtGui import QIcon, QPixmap
from src.views.ui_Main import Ui_MainWindow
from src.views.ui_Bluetooth import Ui_Bluetooth
from src.views.ui_Datos import Ui_Datos
from src.views.ui_Calibration import Ui_Calibration
from src.views.ui_Save import Ui_Save
from src.widgets.DialogWidget import DialogWidget, DialogWidgetInfo
#from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import *
#from src.services.bluetoothLE import BluetoothWorker
from src.views.MonitoringView.MonitoringView import MonitoringView
from src.views.CalibrationView.CalibrationView import CalibrationView

class KeyEventFilter(QtCore.QObject):
    def __init__(self, app, parent=None):
        super(KeyEventFilter, self).__init__(parent)
        self.app = app
    
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_P:
                self.handle_key_p()
                return True
        return super(KeyEventFilter, self).eventFilter(obj, event)

    def handle_key_p(self):
        # Aquí defines qué hacer cuando se presiona la tecla P
        print("P key pressed globally")
        # Llama a la función en tu aplicación principal para cambiar la vista
        if hasattr(self.app, 'switch_to_bluetooth_view'):
            self.app.switch_to_bluetooth_view()

class ParametersMeasuredWorker(QThread):
    parameters_result = Signal(list)

    def __init__(self):
        super(ParametersMeasuredWorker, self).__init__()

    def run(self):
        self.running_state = True
        paraamCalc = ParametersCalculate()

        while self.running_state:
            try:
                temp = round(random.uniform(29, 33), 2)
                ph = round(random.uniform(6.1, 7.32), 2)
                do = round(random.uniform(4.55, 5.89), 2)
                tds = round(random.uniform(724.23, 892.23), 2)
                turb = round(random.uniform(56.23, 203.23), 2)

                self.parameters_result.emit([ph, do, tds, temp, turb])
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
        self.open_view(MonitoringView(widget))

    def on_calibration_clicked(self):
        self.open_view(CalibrationView(widget))

    def on_datos_clicked(self):
        self.open_view(DatosView())

    def on_bluetooth_clicked(self):
        self.open_view(BluetoothView())

    def open_view(self, view):
        widget.addWidget(view)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.setFocus()

    def switch_to_bluetooth_view(self):
        if widget.currentIndex() > 0:
            current_widget = widget.currentWidget()
            widget.removeWidget(current_widget)
            current_widget.deleteLater()  # Liberar memoria si es necesario

        self.on_bluetooth_clicked()


########### VISTA DE GUARDADO#################
class SaveDataView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Save()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        widget.removeWidget(self)

##### VISTA DE LA TABLA DE DATOS###############
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
        # self.bluetooth_worker = BluetoothWorker()
        # self.bluetooth_worker.start()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        # self.bluetooth_worker.stop()
        widget.removeWidget(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    welcome = MyApp()
    key_event_filter = KeyEventFilter(welcome)
    app.installEventFilter(key_event_filter)
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
