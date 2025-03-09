from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon
from src.views.ui_Bluetooth_Connected import Ui_MainWindow
from src.services.BluetoothService.BluetoothService import BluetoothService
from src.package.Navigator import Navigator
from src.config.Constants import Constants

class BluetoothView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.bluetooth_worker = BluetoothService()
        self.bluetooth_worker.start()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

        self.ui.label.setText(f'Conectarse a {Constants.BLE_ID}')
        self.ui.label.setAlignment(Qt.AlignCenter)

    def on_back_clicked(self):
        self.bluetooth_worker.stop()
        Navigator.pop(context= self.context, view= self)