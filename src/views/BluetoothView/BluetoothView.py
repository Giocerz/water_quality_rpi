from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from src.views.ui_Bluetooth import Ui_Bluetooth
from src.services.bluetoothLE import BluetoothWorker

class BluetoothView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_Bluetooth()
        self.ui.setupUi(self)
        self.ui_components()
        self.bluetooth_worker = BluetoothWorker()
        self.bluetooth_worker.start()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        self.bluetooth_worker.stop()
        self.context.removeWidget(self)