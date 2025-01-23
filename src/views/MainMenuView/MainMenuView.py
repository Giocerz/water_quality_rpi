from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from src.views.ui_MainMenu import Ui_MainWindow
from src.views.MonitoringView.MonitoringView import MonitoringView
from src.views.CalibrationView.CalibrationView import CalibrationView
from src.views.FoldersView.FoldersView import FoldersView
from src.views.BluetoothView.BluetoothView import BluetoothView
from src.views.WifiView.WifiView import WifiView
from src.views.EditCalibrationValuesView.EditCalibrationValuesView import EditCalibrationValuesView

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
        self.ui.wifiBtn.clicked.connect(self.on_wifi_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/power_settings.png')
        self.ui.powerBtn.setIcon(icon)
        self.ui.powerBtn.setIconSize(QSize(30, 30))

    def on_monitoring_clicked(self):
        self.open_view(MonitoringView(context= self.context))

    def on_calibration_clicked(self):
        self.open_view(CalibrationView(context= self.context))

    def on_datos_clicked(self):
        self.open_view(FoldersView(context= self.context))

    def on_bluetooth_clicked(self):
        self.open_view(BluetoothView(context= self.context))
    
    def on_wifi_clicked(self):
        self.open_view(WifiView(context=self.context))
    
    def on_edit_clicked(self):
        self.open_view(EditCalibrationValuesView(context= self.context))

    def open_view(self, view):
        self.context.addWidget(view)
        self.context.setCurrentIndex(self.context.currentIndex() + 1)
    
    def switch_to_bluetooth_view(self):
        if self.context.currentIndex() > 0:
            current_widget = self.context.currentWidget()
            self.context.removeWidget(current_widget)
            current_widget.deleteLater()
        self.on_bluetooth_clicked()