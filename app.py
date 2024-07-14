import sys
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, QPixmap
from src.views.ui_Main import Ui_MainWindow
from src.views.ui_Monitoring import Ui_Monitoring
from src.views.ui_Bluetooth import Ui_Bluetooth
from src.views.ui_Datos import Ui_Datos
from src.views.ui_Calibration import Ui_Calibration

class MyApp(QMainWindow):
    def __init__(self):
        QMainWindow. __init__(self)
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
        QMainWindow. __init__(self)
        self.ui = Ui_Monitoring()
        self.ui.setupUi(self)
        self.ui_components()
    
        self.ui.backBtn.clicked.connect(self.on_back_clicked)
    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/save.png')
        self.ui.saveBtn.setIcon(icon)
        self.ui.saveBtn.setIconSize(QSize(30, 30))
    
    def on_back_clicked(self):
        widget.removeWidget(self)

class CalibrationView(QMainWindow):
    def __init__(self):
        QMainWindow. __init__(self)
        self.ui = Ui_Calibration()
        self.ui.setupUi(self)
        self.ui_components()
    
        self.ui.backBtn.clicked.connect(self.on_back_clicked)
    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        pixmap = QPixmap('./src/resources/images/lab_glass.jpg').scaled(150, 150)
        self.ui.imgLbl.setPixmap(pixmap)
        self.ui.instLbl.setText('Sumerja la sonda en una solución\ncon una CE de 1473uS/cm')
        self.ui.instLbl.setAlignment(QtCore.Qt.AlignHCenter)
    
    def on_back_clicked(self):
        widget.removeWidget(self)

class DatosView(QMainWindow):
    def __init__(self):
        QMainWindow. __init__(self)
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
        QMainWindow. __init__(self)
        self.ui = Ui_Bluetooth()
        self.ui.setupUi(self)
        self.ui_components()
    
        self.ui.backBtn.clicked.connect(self.on_back_clicked)
    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
    
    def on_back_clicked(self):
        widget.removeWidget(self)

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