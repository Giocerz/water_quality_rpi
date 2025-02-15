import os
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from src.views.ui_MainMenu import Ui_MainWindow
from src.views.MonitoringView.MonitoringView import MonitoringView
from src.views.CalibrationView.CalibrationView import CalibrationView
from src.views.FoldersView.FoldersView import FoldersView
from src.views.BluetoothView.BluetoothView import BluetoothView
from src.views.UpdateView.UpdateView import UpdateView
from src.views.WifiView.WifiView import WifiView
from src.views.EditCalibrationValuesView.EditCalibrationValuesView import EditCalibrationValuesView
from src.package.Navigator import Navigator

class MainMenuView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.monitoringBtn.clicked.connect(self.on_monitoring_clicked)
        self.ui.calibrationBtn.clicked.connect(self.on_calibration_clicked)
        self.ui.dataBtn.clicked.connect(self.on_datos_clicked)
        self.ui.bluetoothBtn.clicked.connect(self.on_bluetooth_clicked)
        self.ui.editVauesBtn.clicked.connect(self.on_edit_clicked)
        self.ui.updateBtn.clicked.connect(self.on_update_clicked)
        self.ui.wifiBtn.clicked.connect(self.on_wifi_clicked)
        self.ui.powerBtn.clicked.connect(self.on_power_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/power_settings.png')
        self.ui.powerBtn.setIcon(icon)
        self.ui.powerBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/wifi.png')
        self.ui.wifiBtn.setIcon(icon)
        self.ui.wifiBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/update.png')
        self.ui.updateBtn.setIcon(icon)
        self.ui.updateBtn.setIconSize(QSize(30, 30))

    def on_monitoring_clicked(self):
        Navigator.push(context= self.context, view= MonitoringView(context= self.context))

    def on_calibration_clicked(self):
        Navigator.push(context= self.context, view= CalibrationView(context= self.context))

    def on_datos_clicked(self):
        Navigator.push(context= self.context, view= FoldersView(context= self.context))

    def on_bluetooth_clicked(self):
        Navigator.push(context= self.context, view= BluetoothView(context= self.context))
    
    def on_wifi_clicked(self):
        Navigator.push(context= self.context, view= WifiView(context= self.context))
    
    def on_update_clicked(self):
        Navigator.push(context= self.context, view= UpdateView(context= self.context))
    
    def on_edit_clicked(self):
        Navigator.push(context= self.context, view= EditCalibrationValuesView(context= self.context))

    def on_power_clicked(self):
        os.system("sudo poweroff")   