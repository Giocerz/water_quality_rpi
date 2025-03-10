import os
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from src.views.ui_MainMenu import Ui_MainWindow
from src.views.MonitoringView.MonitoringSelect import MonitoringSelectView
from src.views.CalibrationView.CalibrationView import CalibrationView
from src.views.FoldersView.FoldersView import FoldersView
from src.views.BluetoothView.BluetoothView import BluetoothView
from src.views.HelpView.HelpView import HelpView
from src.views.WifiView.WifiView import WifiView
from src.widgets.PopupWidget import PopupWidget
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
        self.ui.helpBtn.clicked.connect(self.on_help_clicked)
        self.ui.wifiBtn.clicked.connect(self.on_wifi_clicked)
        self.ui.powerBtn.clicked.connect(self.on_power_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/power_settings.png')
        self.ui.powerBtn.setIcon(icon)
        self.ui.powerBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/wifi.png')
        self.ui.wifiBtn.setIcon(icon)
        self.ui.wifiBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/help.png')
        self.ui.helpBtn.setIcon(icon)
        self.ui.helpBtn.setIconSize(QSize(30, 30))

    def on_monitoring_clicked(self):
        Navigator.push(context= self.context, view= MonitoringSelectView(context= self.context))

    def on_calibration_clicked(self):
        Navigator.push(context= self.context, view= CalibrationView(context= self.context))

    def on_datos_clicked(self):
        Navigator.push(context= self.context, view= FoldersView(context= self.context))

    def on_bluetooth_clicked(self):
        Navigator.push(context= self.context, view= BluetoothView(context= self.context))
    
    def on_wifi_clicked(self):
        Navigator.push(context= self.context, view= WifiView(context= self.context))
    
    def on_help_clicked(self):
        Navigator.push(context= self.context, view= HelpView(context= self.context))

    def on_power_clicked(self):
        def yes_callback():
            os.system("sudo poweroff")
        def no_callback():
            pass
        popup = PopupWidget(context=self.context, text="¿Quieres apagar el dispositivo?", yes_callback=yes_callback, no_callback=no_callback)