from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize, QThread, Signal
from PySide2.QtGui import QIcon
from src.views.ui_Monitoring3 import Ui_MainWindow
import time
from w1thermsensor import W1ThermSensor
from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import *
from src.views.SaveDataView.SaveDataView import SaveDataView
from src.package.Navigator import Navigator
from src.logic.batteryLevel import BatteryProvider
from src.logic.filters import MovingAverageFilter

class ParametersMeasuredWorker(QThread):
    parameters_result = Signal(list)

    def __init__(self):
        super(ParametersMeasuredWorker, self).__init__()

    def run(self):
        self.running_state = True

        temperature_sensor = W1ThermSensor()
        parameters = ParametersVoltages()
        parameters_calc = ParametersCalculate()
        battery_provider = BatteryProvider()
        turb_filter = MovingAverageFilter(10)

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
                turb_voltage = turb_filter.add_value(parameters.turbidity_volt())
                turb = round(parameters_calc.calculateTurb(turb_voltage), 2)
                battery = battery_provider.getBatteryLevel()
                

                self.parameters_result.emit([ph, do, tds, temp, turb, battery])
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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.oxygen = None
        self.ph = None
        self.temperature = None
        self.tds = None
        self.turbidity = None
        self.battery = None

        self.receive_parameters = False
        
        self.isPause = False

        self.parameters_worker = ParametersMeasuredWorker()
        if not self.parameters_worker.isRunning():
            self.parameters_worker.start()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.saveBtn.clicked.connect(self.on_save_clicked)
        self.ui.pauseBtn.clicked.connect(self.on_pause_clicked)

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
        Navigator.pop(context=self.context, view= self)
    
    def on_pause_clicked(self):
        if(self.isPause):
            if not self.parameters_worker.isRunning():
                self.parameters_worker.start()
                self.ui.pauseBtn.setText('Pausar')
                self.isPause = False
        else:
            if self.parameters_worker.isRunning():
                self.parameters_worker.stop()
                self.ui.pauseBtn.setText('Reanudar')
                self.isPause = True

    def on_save_clicked(self):
        if(not self.receive_parameters):
            return
        self.parameters_worker.stop()
        view = SaveDataView(context= self.context, oxygen=self.oxygen, ph=self.ph, temperature=self.temperature, tds=self.tds, turbidity=self.turbidity, battery_level=self.battery)
        Navigator.pushReplacement(context=self.context, view=view)

    def handle_parameters_result(self, parameters):
        self.receive_parameters = True

        self.ph = parameters[0]
        self.ui.phLbl.setText(str(self.ph))
        self.ui.phLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.oxygen = parameters[1]
        self.ui.odLbl.setText(str(self.oxygen))
        self.ui.odLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.tds = parameters[2]
        self.ui.tdsLbl.setText(str(self.tds))
        self.ui.tdsLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.temperature = parameters[3]
        self.ui.tempLbl.setText(str(self.temperature))
        self.ui.tempLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.ui.ecLbl.setText(str(self.tds * 2))
        self.ui.ecLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.turbidity = parameters[4]
        self.ui.turbLbl.setText(str(self.turbidity))
        self.ui.turbLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.battery = parameters[5]