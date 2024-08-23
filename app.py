import sys
# import struct
import time
import random
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QSize, QThread, Signal, Slot, QTimer
from PySide2.QtGui import QIcon, QPixmap
from src.views.ui_Main import Ui_MainWindow
from src.views.ui_Monitoring import Ui_Monitoring
from src.views.ui_Bluetooth import Ui_Bluetooth
from src.views.ui_Datos import Ui_Datos
from src.views.ui_Calibration import Ui_Calibration
from src.widgets.DialogWidget import DialogWidget, DialogWidgetInfo
from w1thermsensor import W1ThermSensor
from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import *
from src.services.bluetoothLE import BluetoothWorker


class ParametersMeasuredWorker(QThread):
    parameters_result = Signal(list)

    def __init__(self):
        super(ParametersMeasuredWorker, self).__init__()

    def run(self):
        self.running_state = True

        temperature_sensor = W1ThermSensor()
        parameters = ParametersVoltages()
        parameters_calc = ParametersCalculate()

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
                ph = round(parameters_calc.calculatePh(parameters.ph_volt()), 2)
                do = round(parameters_calc.calculateDo(parameters.oxygen_volt(), temp), 2)
                tds = round(parameters_calc.calculateTds(temp, parameters.tds_volt()), 2)
                turb = round(parameters_calc.calculateTurb(parameters.turbidity_volt()), 2)

                self.parameters_result.emit([ph, do, tds, temp, turb])
                time.sleep(1)
            except Exception as e:
                print(e)

    def stop(self):
        self.running_state = False
        self.wait()


class MyApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
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
        QMainWindow.__init__(self)
        self.ui = Ui_Monitoring()
        self.ui.setupUi(self)
        self.ui_components()

        self.parameters_worker = ParametersMeasuredWorker()
        if not self.parameters_worker.isRunning():
            self.parameters_worker.start()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

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
        widget.removeWidget(self)

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


########### VISTA DE CALIBRACION Y FUNCIONES#################
class CalibrationView(QMainWindow):
    STABILIZATION_TIME = 2  # secs
    TIMEOUT_STABILIZATION_TIMER = 1000  # ms
    LOADING_TEXT = 'Espera mientras se estabiliza el valor medido',

    CALIBRATION_STEPS = ['tds', 'wash', 'ph7', 'wash', 'ph4',
                         'wash', 'ph10', 'wash', 'turb1', 'wash', 'turb2', 'wash', 'turb3', 'wash', 'turb4', 'wash', 'do', 'final']
    STEPS_DESCRIPTION = {
        'tds': {
            'img': './src/resources/images/lab_glass',
            'text': 'Sumerja la sonda en una solución con una<br><b>conductividad eléctrica</b> de <b>1413μS/cm</b>',
            'skipButton': True
        },
        'ph7': {
            'img': './src/resources/images/ph_glass',
            'text': 'Sumerja la sonda en una solución<br>con un <b>ph</b> de <b>7.0</b>',
            'skipButton': True
        },
        'ph4': {
            'img': './src/resources/images/ph_glass',
            'text': 'Sumerja la sonda en una solución<br>con un <b>ph</b> de <b/>4.0<b>',
            'skipButton': False
        },
        'ph10': {
            'img': './src/resources/images/ph_glass',
            'text': 'Sumerja la sonda en una solución<br>con un <b>ph</b> de <b>10.0</b>',
            'skipButton': False
        },
        'turb1': {
            'img': './src/resources/images/lab_glass',
            'text': 'Sumerja la sonda en una solución<br>con una <b>turbidez</b> de <b>0.02 NTU</b>',
            'skipButton': True
        },
        'turb2': {
            'img': './src/resources/images/lab_glass',
            'text': 'Sumerja la sonda en una solución<br>con una <b>turbidez</b> de <b>20 NTU</b>',
            'skipButton': False
        },
        'turb3': {
            'img': './src/resources/images/lab_glass',
            'text': 'Sumerja la sonda en una solución<br>con una <b>turbidez</b> de <b>100 NTU</b>',
            'skipButton': False
        },
        'turb4': {
            'img': './src/resources/images/lab_glass',
            'text': 'Sumerja la sonda en una solución<br>con una <b>turbidez</b> de <b>800 NTU</b>',
            'skipButton': False
        },
        'do': {
            'img': './src/resources/images/oxygen_sensor',
            'text': 'Mantenga la sonda en el <b>aire</b>',
            'skipButton': True
        },
        'wash': {
            'img': './src/resources/images/wash',
            'text': 'Enjuague la sonda con agua<br>destilada y agite suavemente',
            'skipButton': False
        },
        'final': {
            'img': './src/resources/images/wash',
            'text': 'Finalizó la calibración',
            'skipButton': False
        }
    }

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Calibration()
        self.ui.setupUi(self)
        self.calibration_step = 0
        self.timer_counter = 0
        # Parametros de calibracion
        self.kValue = None
        self.ph_offset = None
        self.ph4 = None
        self.ph10 = None
        self.phSlope = None
        self.turb1 = None
        self.turb2 = None
        self.turb3 = None
        self.turb4 = None
        self.oxygenOffset = None
        self.oxygenTemperature = None

        self.parameters_volt = ParametersVoltages()
        self.temperature_sensor = W1ThermSensor()
        self.parameters_calc = ParametersCalculate()

        self.step_actions = {
            'tds': self.handle_tds,
            'ph7': self.handle_ph7,
            'ph4': self.handle_ph4,
            'ph10': self.handle_ph10,
            'turb1': self.handle_turb1,
            'turb2': self.handle_turb2,
            'turb3': self.handle_turb3,
            'turb4': self.handle_turb4,
            'do': self.handle_do,
        }

        self.ui_components()

        self.stabilization_timer = QTimer()
        self.stabilization_timer.timeout.connect(self.update_time)

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.nextBtn.clicked.connect(self.next_btn_clicked)
        self.ui.skipBtn.clicked.connect(self.skip_btn_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        self.update_state()

    def update_state(self):
        print(self.calibration_step)
        self.ui.nextBtn.show()
        if (self.STEPS_DESCRIPTION[self.CALIBRATION_STEPS[self.calibration_step]]['skipButton']):
            self.ui.skipBtn.show()
        else:
            self.ui.skipBtn.hide()

        if (self.CALIBRATION_STEPS[self.calibration_step] == 'final'):
            self.save_calibration()
            self.ui.nextBtn.setText('Salir')

        self.set_image(
            self.STEPS_DESCRIPTION[self.CALIBRATION_STEPS[self.calibration_step]]['img'])
        self.ui.loadingBar.hide()
        self.set_text_label(
            self.STEPS_DESCRIPTION[self.CALIBRATION_STEPS[self.calibration_step]]['text'])
        self.ui.instLbl.setAlignment(QtCore.Qt.AlignCenter)

    def set_image(self, url):
        pixmap = QPixmap(url)
        pixmap = pixmap.scaled(130, 130)
        self.ui.imgLbl.setPixmap(pixmap)

    def set_text_label(self, text):
        self.ui.instLbl.setText(text)
        self.ui.instLbl.setAlignment(QtCore.Qt.AlignCenter)

    def show_loading(self):
        self.ui.loadingBar.show()
        self.ui.skipBtn.hide()
        self.ui.nextBtn.hide()
        self.stabilization_timer.start(self.TIMEOUT_STABILIZATION_TIMER)

    def update_time(self):
        self.timer_counter += 1
        progress = int(self.timer_counter/self.STABILIZATION_TIME * 100)
        self.ui.loadingBar.setValue(progress)
        if self.timer_counter > self.STABILIZATION_TIME:
            succes = self.step_actions[self.CALIBRATION_STEPS[self.calibration_step]](
            )
            self.ui.loadingBar.setValue(0)
            self.stabilization_timer.stop()
            self.timer_counter = 0
            if (succes):
                self.calibration_step += 1
            self.update_state()

    def on_back_clicked(self):
        if self.calibration_step == len(self.CALIBRATION_STEPS) - 1:
            widget.removeWidget(self)
        else:
            self.show_dialog()

    def show_dialog(self):
        def on_yes():
            widget.removeWidget(self)

        def on_no():
            pass

        dialog = DialogWidget(yes_callback=on_yes, no_callback=on_no,
                              text='No se ha completado la calibración<br>¿Desea salir?')
        dialog.exec_()

    def show_dialog_error(self, error: str):
        dialog = DialogWidgetInfo(text=error)
        dialog.exec_()

    def next_btn_clicked(self):
        if self.CALIBRATION_STEPS[self.calibration_step] == 'wash':
            self.skip_btn_clicked()
        elif self.CALIBRATION_STEPS[self.calibration_step] == 'final':
            self.on_back_clicked()
        else:
            self.show_loading()

    def skip_btn_clicked(self):
        if self.CALIBRATION_STEPS[self.calibration_step] == 'ph7':
            self.calibration_step += 6
        elif self.CALIBRATION_STEPS[self.calibration_step] == 'turb1':
            self.calibration_step += 8
        elif self.CALIBRATION_STEPS[self.calibration_step] == 'do' or self.CALIBRATION_STEPS[self.calibration_step] == 'wash':
            self.calibration_step += 1
        else:
            self.calibration_step += 2
        self.update_state()

    ######### FUNCIONES PARA CADA PASO#################
    def handle_tds(self) -> bool:
        # temp = temperature_sensor.get_temperature()
        # self.tds_voltage = self.parameters_volt.tds_volt()
        # kValue = self.parameters_calc.tds_calibration(temp, tds_voltage)
        try:
            kValue_temp = 0
            if (kValue_temp <= 0.0 or kValue_temp >= 10.0):
                self.show_dialog_error('Error: kValue fuera de rango')
                return False
            else:
                self.kValue = kValue_temp
                return True
        except:
            self.show_dialog_error('Error: kValue fuera de rango')
            return False

    def handle_ph7(self):
        # self.tds_voltage = self.parameters_volt.tds_volt()
        # offset_temp = self.parameters_volt.ph_volt()
        offset_temp = 0
        if (offset_temp <= 0.0 or offset_temp >= 4):
            self.show_dialog_error('Error: Offset fuera de rango')
            return False
        else:
            self.ph_offset = offset_temp
            return True

    def handle_ph4(self):
        ph4_voltage = self.parameters_volt.ph_volt()
        self.ph4 = ph4_voltage

    def handle_ph10(self):
        ph10_voltage = self.parameters_volt.ph_volt()
        try:
            slopeA = abs(3/(self.ph_offset - self.ph4))
            slopeB = abs(3/(ph10_voltage - self.ph_offset))

            slope_temp = (slopeA + slopeB)/2

            if (slope_temp <= 0.025 or slope_temp >= 1.0):
                self.ph_offset - None
                self.calibration_step = 2
                self.show_dialog_error('Error: pendiente fuera de rango')
                return False
            else:
                self.phSlope = slope_temp
                return True
        except:
            self.ph_offset - None
            self.calibration_step = 2
            self.show_dialog_error('Error: pendiente fuera de rango')
            return False

    def handle_turb1(self):
        #self.ph_offset = self.parameters_volt.turbidity_volt()
        return True

    def handle_turb2(self):
        #self.ph_offset = self.parameters_volt.turbidity_volt()
        return True

    def handle_turb3(self):
        #self.ph_offset = self.parameters_volt.turbidity_volt()
        return True

    def handle_turb4(self):
        #self.ph_offset = self.parameters_volt.turbidity_volt()
        return True

    def handle_do(self):
        vCal = self.parameters_volt.oxygen_volt()
        tempCal = temperature_sensor.get_temperature()
        if ((tempCal <= 0.0 or tempCal >= 40.0) or (vCal <= 0.0 or vCal >= 3.0)):
            self.show_dialog_error('Error: Valores de oxigeno fuera de rango')
            return False
        else:
            self.oxygenTemperature = tempCal
            self.oxygenOffset = vCal
            return True

    def save_calibration(self):
        params_save_flag = False
        import pandas as pd
        df = pd.read_csv('./src/config/calibrationSettings.txt')
        if(self.kValue != None):
            df.loc[0, 'calibration_values'] = self.kValue
            params_save_flag = True
        if(self.ph_offset != None):
            df.loc[1, 'calibration_values'] = self.ph_offset
            df.loc[2, 'calibration_values'] = self.phSlope
            params_save_flag = True
        if(self.oxygenOffset!= None):
            df.loc[3, 'calibration_values'] = self.oxygenTemperature
            df.loc[4, 'calibration_values'] = self.oxygenOffset
            params_save_flag = True
        df.to_csv('./src/config/calibrationSettings.txt', index=False)

        if(params_save_flag):
            self.show_dialog_error('No realizo ninguna calibración')
        else:
            self.show_dialog_error('Calibración exitosa')
        

##### VISTA DE LA TABLA DE DATOS###############
class DatosView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
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
        QMainWindow.__init__(self)
        self.ui = Ui_Bluetooth()
        self.ui.setupUi(self)
        self.ui_components()
        # self.bluetooth_worker = BluetoothWorker()
        # self.bluetooth_worker.start()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        # self.bluetooth_worker.stop()
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
