from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon
from src.views.ui_MonitoringSelect import Ui_MainWindow
from src.package.Navigator import Navigator
from src.views.MonitoringView.MonitoringView import MonitoringView

class MonitoringSelectView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.is_all_checked = False

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.initBtn.clicked.connect(self.on_start_clicked)
        self.ui.allCheckBox.clicked.connect(self.on_all_checkbox_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
    
    def on_back_clicked(self):
        Navigator.pop(context=self.context, view=self)
    
    def on_start_clicked(self):
        tds_check = self.ui.tdsCheckBox.checkState() == QtCore.Qt.Checked
        ph_check = self.ui.phCheckBox.checkState() == QtCore.Qt.Checked
        oxygen_check = self.ui.oxygenCheckBox.checkState() == QtCore.Qt.Checked
        turbidity_check = self.ui.turbidityCheckBox.checkState() == QtCore.Qt.Checked

        Navigator.pushReplacement(
            context=self.context,
            view=MonitoringView(
                context=self.context,
                tds_check=tds_check,
                ph_check=ph_check,
                oxygen_check=oxygen_check,
                turbidity_check=turbidity_check
            )
        )

    def on_all_checkbox_clicked(self):
        qt_check_state:Qt.CheckState = None
        if self.is_all_checked:
            qt_check_state = Qt.Unchecked
        else:
            qt_check_state = Qt.Checked
        
        self.is_all_checked = not self.is_all_checked

        self.ui.tdsCheckBox.setCheckState(qt_check_state)
        self.ui.phCheckBox.setCheckState(qt_check_state)
        self.ui.oxygenCheckBox.setCheckState(qt_check_state)
        self.ui.turbidityCheckBox.setCheckState(qt_check_state)