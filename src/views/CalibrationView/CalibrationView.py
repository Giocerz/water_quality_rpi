from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize, QTimer
from PySide2.QtGui import QIcon, QPixmap
from src.views.ui_Calibration import Ui_Calibration
from src.widgets.DialogWidget import DialogWidget, DialogWidgetInfo
from w1thermsensor import W1ThermSensor
from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import *

########### VISTA DE CALIBRACION Y FUNCIONES#################
class CalibrationView(QMainWindow):
    STABILIZATION_TIME = 5  # secs
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
            'text': 'Sumerja la sonda en una solución<br>con una <b>turbidez</b> de <b>0.28 NTU</b>',
            'skipButton': True
        },
        'turb2': {
            'img': './src/resources/images/lab_glass',
            'text': 'Sumerja la sonda en una solución<br>con una <b>turbidez</b> de <b>98.1 NTU</b>',
            'skipButton': False
        },
        'turb3': {
            'img': './src/resources/images/lab_glass',
            'text': 'Sumerja la sonda en una solución<br>con una <b>turbidez</b> de <b>287 NTU</b>',
            'skipButton': False
        },
        'turb4': {
            'img': './src/resources/images/lab_glass',
            'text': 'Sumerja la sonda en una solución<br>con una <b>turbidez</b> de <b>475 NTU</b>',
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

    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
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
        self.turb_coef_a = None
        self.turb_coef_b = None
        self.turb_coef_c = None

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
            self.context.removeWidget(self)
        else:
            self.show_dialog()

    def show_dialog(self):
        def on_yes():
            self.context.removeWidget(self)

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
        try:
            temperature_sensor = W1ThermSensor()
            temp = temperature_sensor.get_temperature()
            self.tds_voltage = self.parameters_volt.tds_volt()
            kValue_temp = self.parameters_calc.tds_calibration(temp, self.tds_voltage)
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
        offset_temp = self.parameters_volt.ph_volt()
        if (offset_temp <= 0.0 or offset_temp >= 4):
            self.show_dialog_error('Error: Offset fuera de rango')
            return False
        else:
            self.ph_offset = offset_temp
            return True

    def handle_ph4(self):
        ph4_voltage = self.parameters_volt.ph_volt()
        self.ph4 = ph4_voltage
        return True

    def handle_ph10(self):
        ph10_voltage = self.parameters_volt.ph_volt()
        try:
            slopeA = abs((self.ph_offset - self.ph4)/3)
            slopeB = abs((ph10_voltage - self.ph_offset)/3)

            slope_temp = (slopeA + slopeB)/2

            if (slope_temp <= 0.01 or slope_temp >= 2.0):
                self.ph_offset = None
                self.calibration_step = 2
                self.show_dialog_error('Error: pendiente fuera de rango')
                return False
            else:
                self.phSlope = slope_temp
                return True
        except:
            self.ph_offset = None
            self.calibration_step = 2
            self.show_dialog_error('Error: pendiente fuera de rango')
            return False

    def handle_turb1(self):
        self.turb1 = self.parameters_volt.turbidity_volt()
        if(self.turb1 <= 0.0 or self.turb1 >= 5.0):
            self.show_dialog_error('Error: Valor de turbidez fuera de rango')
            return False
        else: 
            return True

    def handle_turb2(self):
        self.turb2 = self.parameters_volt.turbidity_volt()
        if(self.turb2 <= 0.0 or self.turb2 >= 5.0):
            self.show_dialog_error('Error: Valor de turbidez fuera de rango')
            return False
        else: 
            return True

    def handle_turb3(self):
        self.turb3 = self.parameters_volt.turbidity_volt()
        if(self.turb3 <= 0.0 or self.turb3 >= 5.0):
            self.show_dialog_error('Error: Valor de turbidez fuera de rango')
            return False
        else: 
            return True

    def handle_turb4(self):
        self.turb4 = self.parameters_volt.turbidity_volt()
        if(self.turb4 <= 0.0 or self.turb4 >= 5.0):
            self.show_dialog_error('Error: Valor de turbidez fuera de rango')
            return False
        try:
            import numpy as np
            voltages = np.array([self.turb1, self.turb2, self.turb3, self.turb4])
            ntu_values = np.array([0.28, 98.1, 287, 475])
            coefficients = np.polyfit(voltages, ntu_values, 2)
            self.turb_coef_a, self.turb_coef_b, self.turb_coef_c = coefficients
        except:
            self.show_dialog_error('Error: Calibracion de turbidez fallida')
            return False

    def handle_do(self):
        vCal = self.parameters_volt.oxygen_volt()
        temperature_sensor = W1ThermSensor()
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
        if (self.kValue != None):
            df.loc[0, 'calibration_values'] = self.kValue
            params_save_flag = True
        if (self.ph_offset != None):
            df.loc[1, 'calibration_values'] = self.ph_offset
            df.loc[2, 'calibration_values'] = self.phSlope
            params_save_flag = True
        if(self.oxygenOffset != None):
            df.loc[3, 'calibration_values'] = self.oxygenTemperature
            df.loc[4, 'calibration_values'] = self.oxygenOffset
            params_save_flag = True
        if(self.turb_coef_a != None):
            df.loc[5, 'calibration_values'] = self.turb_coef_a
            df.loc[6, 'calibration_values'] = self.turb_coef_b
            df.loc[7, 'calibration_values'] = self.turb_coef_c
            params_save_flag = True
        df.to_csv('./src/config/calibrationSettings.txt', index=False)

        if (not params_save_flag):
            self.show_dialog_error('No realizo ninguna calibración')
        else:
            self.show_dialog_error('Calibración exitosa')
