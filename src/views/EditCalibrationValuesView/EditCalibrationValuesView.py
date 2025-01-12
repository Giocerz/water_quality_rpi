from PySide2.QtWidgets import QMainWindow, QStackedLayout
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from src.views.ui_Cal_Value_Edit import Ui_MainWindow
from src.widgets.PopupWidget import PopupWidget, PopupWidgetInfo
from src.logic.saveCalibration import CalibrationTurbidityValues
from src.widgets.KeyboardWidget import KeyboardWidget

class EditCalibrationValuesView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_values()
        self.ui_components()

        #self.keyboard = KeyboardWidget(self.ui.doubleSPinVal1)
        #layout = QStackedLayout(self.ui.widgetKeyboard)
        #layout.addWidget(self.keyboard)
        #self.ui.widgetKeyboard.setLayout(layout)

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.saveBtn.clicked.connect(self.on_save_clicked)
        """
        self.ui.doubleSPinVal1.mousePressEvent = self.select_focus_spin_1
        self.ui.doubleSPinVal2.mousePressEvent = self.select_focus_spin_2
        self.ui.doubleSPinVal3.mousePressEvent = self.select_focus_spin_3
        self.ui.doubleSPinVal4.mousePressEvent = self.select_focus_spin_4
        """
    
    def init_values(self):
        self.calibration_turb_values:CalibrationTurbidityValues = CalibrationTurbidityValues() 
        self.cal_turb_values = self.calibration_turb_values.read_values()

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        self.ui.doubleSPinVal1.setValue(self.cal_turb_values[0])
        self.ui.doubleSPinVal2.setValue(self.cal_turb_values[1])
        self.ui.doubleSPinVal3.setValue(self.cal_turb_values[2])
        self.ui.doubleSPinVal4.setValue(self.cal_turb_values[3])
        
    def on_back_clicked(self):
        self.context.removeWidget(self)

    def on_save_clicked(self):
        value1 = self.ui.doubleSPinVal1.value()
        value2 = self.ui.doubleSPinVal2.value()
        value3 = self.ui.doubleSPinVal3.value()
        value4 = self.ui.doubleSPinVal4.value()
        if(value4 > value3 and value3 > value2 and value2 > value1):
            self.calibration_turb_values.save_values([value1, value2, value3, value4])
            self.on_back_clicked()
        else:
            self.inf_popup = PopupWidgetInfo(context= self.context, text='Error en los valores, deben ir de menor a mayor')
            self.inf_popup.show()

    """
    def select_focus_spin_1(self, event):
        self.keyboard.changeFocusKeyboard(self.LineComando) 
    
    def select_focus_spin_2(self, event):
        self.keyboard.changeFocusKeyboard(self.LineComando) 
    
    def select_focus_spin_3(self, event):
        self.keyboard.changeFocusKeyboard(self.LineComando) 
    
    def select_focus_spin_4(self, event):
        self.keyboard.changeFocusKeyboard(self.LineComando) 
        """