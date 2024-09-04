from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QSize, QThread, Signal, Slot, QTimer
from PySide2.QtGui import QIcon
from src.views.ui_Monitoring import Ui_Monitoring
import time
from w1thermsensor import W1ThermSensor
from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import *
from src.views.SaveDataView.SaveDataView import SaveDataView
from src.logic.INA219 import INA219

class ParametersMeasuredWorker(QThread):
    parameters_result = Signal(list)

    def __init__(self):
        super(ParametersMeasuredWorker, self).__init__()

    def run(self):
        self.running_state = True

        temperature_sensor = W1ThermSensor()
        parameters = ParametersVoltages()
        parameters_calc = ParametersCalculate()
        ina219 = INA219(addr=0x42)

        while self.running_state:
            try:
                '''
                temp = round(random.uniform(29, 33), 2)
                ph = round(random.uniform(6.1, 7.32), 2)
                do = round(random.uniform(4.55, 5.89), 2)
                tds = round(random.uniform(724.23, 892.23), 2)
                turb = round(random.uniform(56.23, 203.23), 2)
                '''
                temp = round(temperature_sensor.get_temperature(), 2)
                ph = round(parameters_calc.calculatePh(
                    parameters.ph_volt()), 2)
                do = round(parameters_calc.calculateDo(
                    parameters.oxygen_volt(), temp), 2)
                tds = round(parameters_calc.calculateTds(
                    temp, parameters.tds_volt()), 2)
                turb = round(parameters_calc.calculateTurb(
                    parameters.turbidity_volt()), 2)
                
                bus_voltage = ina219.getBusVoltage_V()             # voltage on V- (load side)                # power in W
                p = (bus_voltage - 6)/2.4*100
                if(p > 100):p = 100
                if(p < 0):p = 0

                self.parameters_result.emit([ph, do, tds, temp, turb, p])
                time.sleep(1)
            except Exception as e:
                print(e)

    def stop(self):
        self.running_state = False
        self.wait()
    

class MonitoringView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_Monitoring()
        self.ui.setupUi(self)
        self.ui_components()

        self.parameters_worker = ParametersMeasuredWorker()
        if not self.parameters_worker.isRunning():
            self.parameters_worker.start()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.saveBtn.clicked.connect(self.on_save_clicked)

        self.parameters_worker.parameters_result.connect(
            self.handle_parameters_result)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/save.png')
        self.ui.saveBtn.setIcon(icon)
        self.ui.saveBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        if self.parameters_worker.isRunning():
            self.parameters_worker.stop()
        self.context.removeWidget(self)

    def on_save_clicked(self):
        view = SaveDataView(context= self.context)
        self.context.addWidget(view)
        self.context.setCurrentIndex(self.context.currentIndex() + 1)
        self.context.removeWidget(self)

    def handle_parameters_result(self, parameters):
        self.ui.phLbl.setText(str(parameters[0]))
        self.ui.phLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.odLbl.setText(str(parameters[1]))
        self.ui.odLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.tdsLbl.setText(str(parameters[2]))
        self.ui.tdsLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.tempLbl.setText(str(parameters[3]))
        self.ui.tempLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.ecLbl.setText(str(parameters[2] * 2))
        self.ui.ecLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.turbLbl.setText(str(parameters[4]))
        self.ui.turbLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.batLbl.setText(f"{str(parameters[5])} %")
        self.ui.batLbl.setAlignment(QtCore.Qt.AlignCenter)
