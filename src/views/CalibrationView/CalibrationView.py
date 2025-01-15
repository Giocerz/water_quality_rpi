from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize, QTimer
from PySide2.QtGui import QIcon, QPixmap
from src.views.ui_Calibration import Ui_MainWindow
from src.widgets.DialogWidget import DialogWidget, DialogWidgetInfo
from w1thermsensor import W1ThermSensor
from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import *
from src.widgets.PopupWidget import PopupWidget, PopupWidgetInfo
from src.logic.saveCalibration import SaveCalibration, CalibrationTurbidityValues

########### VISTA DE CALIBRACION Y FUNCIONES#################


class CalibrationView(QMainWindow):
    STABILIZATION_TIME = 35  # secs
    TIMEOUT_STABILIZATION_TIMER = 1000  # ms
    LOADING_TEXT = 'Espera mientras se estabiliza el valor medido',

    CALIBRATION_STEPS = ['tds', 'wash', 'ph7', 'wash', 'ph4',
                         'wash', 'ph10', 'wash', 'turb1', 'wash', 'turb2', 'wash', 'turb3', 'wash', 'turb4', 'wash', 'do', 'final']

    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.calibration_step = 0
        self.timer_counter = 0
        #Valores NTU turb
        self.cal_turb_values = []
        # Parametros de calibracion
        self.kValue = None
        self.ph_offset = None
        self.ph4 = None
        self.ph10 = None
        self.ph_slopeA = None
        self.ph_slopeB = None
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

        self.show_volt = {
            'tds': self.show_tds_volt,
            'ph7': self.show_ph_volt,
            'ph4': self.show_ph_volt,
            'ph10': self.show_ph_volt,
            'turb1': self.show_turb_volt,
            'turb2': self.show_turb_volt,
            'turb3': self.show_turb_volt,
            'turb4': self.show_turb_volt,
            'do': self.show_do_volt,
        }

        self.init_step_views()
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
    
    def init_step_views(self):
        calibration_turbidity_values:CalibrationTurbidityValues = CalibrationTurbidityValues()
        self.cal_turb_values = calibration_turbidity_values.read_values()
        self.STEPS_DESCRIPTION = {
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
            'text': f'Sumerja la sonda en una solución<br>con una <b>turbidez</b> de <b>{self.cal_turb_values[0]} NTU</b>',
            'skipButton': True
        },
        'turb2': {
            'img': './src/resources/images/lab_glass',
            'text': f'Sumerja la sonda en una solución<br>con una <b>turbidez</b> de <b>{self.cal_turb_values[1]} NTU</b>',
            'skipButton': False
        },
        'turb3': {
            'img': './src/resources/images/lab_glass',
            'text': f'Sumerja la sonda en una solución<br>con una <b>turbidez</b> de <b>{self.cal_turb_values[2]} NTU</b>',
            'skipButton': False
        },
        'turb4': {
            'img': './src/resources/images/lab_glass',
            'text': f'Sumerja la sonda en una solución<br>con una <b>turbidez</b> de <b>{self.cal_turb_values[3]} NTU</b>',
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

    def update_state(self):
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
        self.ui.showVoltLbl.hide()
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
        self.ui.showVoltLbl.show()
        self.ui.loadingBar.show()
        self.ui.skipBtn.hide()
        self.ui.nextBtn.hide()
        self.stabilization_timer.start(self.TIMEOUT_STABILIZATION_TIMER)

    def update_time(self):
        self.timer_counter += 1
        progress = int(self.timer_counter/self.STABILIZATION_TIME * 100)
        self.ui.loadingBar.setValue(progress)
        self.show_volt[self.CALIBRATION_STEPS[self.calibration_step]]()
        if self.timer_counter > self.STABILIZATION_TIME:
            success = self.step_actions[self.CALIBRATION_STEPS[self.calibration_step]](
            )
            self.ui.loadingBar.setValue(0)
            self.stabilization_timer.stop()
            self.timer_counter = 0
            if (success):
                self.calibration_step += 1
            self.update_state()

    def on_back_clicked(self):
        if self.calibration_step == len(self.CALIBRATION_STEPS) - 1:
            self.context.removeWidget(self)
        else:
            self.show_dialog()

    def show_dialog(self):
        def on_yes():
            self.stabilization_timer.stop()
            self.context.removeWidget(self)

        def on_no():
            pass

        dialog = PopupWidget(context=self.context, yes_callback=on_yes, no_callback=on_no,
                             text='No se ha completado la calibración<br>¿Desea salir?')
        dialog.show()

    def show_dialog_error(self, error: str):
        dialog = PopupWidgetInfo(context=self.context, text=error)
        dialog.show()

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

    ######### MOSTRAR VOLTAJES ########################
    def show_tds_volt(self):
        try:
            temperature = self.temperature_sensor.get_temperature()
            tds_volt = self.parameters_volt.tds_volt()
            text = f"Temp: {temperature:.2f} °C Volt: {tds_volt:.2f} V"
        except (TypeError, ValueError):
            text = "Temp: N/A °C Volt: N/A V"

        self.ui.showVoltLbl.setText(text)
        self.ui.showVoltLbl.setAlignment(QtCore.Qt.AlignCenter)


    def show_ph_volt(self):
        try:
            ph_volt = self.parameters_volt.ph_volt()
            text = f"Volt: {ph_volt:.2f} V"
        except (TypeError, ValueError):
            text = "Volt: N/A V"

        self.ui.showVoltLbl.setText(text)
        self.ui.showVoltLbl.setAlignment(QtCore.Qt.AlignCenter)


    def show_turb_volt(self):
        try:
            turbidity_volt = self.parameters_volt.turbidity_volt()
            text = f"Volt: {turbidity_volt:.2f} V"
        except (TypeError, ValueError):
            text = "Volt: N/A V"

        self.ui.showVoltLbl.setText(text)
        self.ui.showVoltLbl.setAlignment(QtCore.Qt.AlignCenter)


    def show_do_volt(self):
        try:
            temperature = self.temperature_sensor.get_temperature()
            oxygen_volt = self.parameters_volt.oxygen_volt()
            text = f"Temp: {temperature:.2f} °C Volt: {oxygen_volt:.2f} V"
        except (TypeError, ValueError):
            text = "Temp: N/A °C Volt: N/A V"

        self.ui.showVoltLbl.setText(text)
        self.ui.showVoltLbl.setAlignment(QtCore.Qt.AlignCenter)

    ######### FUNCIONES PARA CADA PASO#################
    def handle_tds(self) -> bool:
        try:
            temp = self.temperature_sensor.get_temperature()
            self.tds_voltage = self.parameters_volt.tds_volt()
            kValue_temp = self.parameters_calc.tds_calibration(
                temp, self.tds_voltage)
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
            slopeA = abs(3/(self.ph_offset - self.ph4))
            slopeB = abs(3/(ph10_voltage - self.ph_offset))

            if (slopeA <= 1 or slopeA >= 100 or slopeB <= 1 or slopeB >= 100):
                self.ph_offset = None
                self.calibration_step = 2
                self.show_dialog_error('Error: pendiente fuera de rango')
                return False
            else:
                self.ph_slopeA = slopeA
                self.ph_slopeB = slopeB
                return True
        except:
            self.ph_offset = None
            self.calibration_step = 2
            self.show_dialog_error('Error: pendiente fuera de rango')
            return False

    def handle_turb1(self):
        self.turb1 = self.parameters_volt.turbidity_volt()
        if (self.turb1 <= 0.0 or self.turb1 >= 5.0):
            self.show_dialog_error('Error: Valor de turbidez fuera de rango')
            return False
        else:
            return True
        
    def handle_turb2(self):
        self.turb2 = self.parameters_volt.turbidity_volt()
        if (self.turb2 <= 0.0 or self.turb2 >= 5.0):
            self.show_dialog_error('Error: Valor de turbidez fuera de rango')
            return False
        else:
            return True

    def handle_turb3(self):
        self.turb3 = self.parameters_volt.turbidity_volt()
        if (self.turb3 <= 0.0 or self.turb3 >= 5.0):
            self.show_dialog_error('Error: Valor de turbidez fuera de rango')
            return False
        else:
            return True

    def handle_turb4(self):
        self.turb4 = self.parameters_volt.turbidity_volt()
        if (self.turb4 <= 0.0 or self.turb4 >= 5.0):
            self.show_dialog_error('Error: Valor de turbidez fuera de rango')
            return False
        try:
            import numpy as np
            voltages = np.array(
                [self.turb1, self.turb2, self.turb3, self.turb4])
            ntu_values = np.array(self.cal_turb_values)
            coefficients = np.polyfit(voltages, ntu_values, 2)
            self.turb_coef_a, self.turb_coef_b, self.turb_coef_c = coefficients
            return True
        except Exception as e:
            print(e)
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
        save = SaveCalibration()
        if (self.kValue != None):
            save.add_kvalue(self.kValue)
            params_save_flag = True
        if (self.ph_offset != None):
            save.add_ph_offset(self.ph_offset)
            save.add_ph_slopes([self.ph_slopeA, self.ph_slopeB])
            params_save_flag = True
        if (self.oxygenOffset != None):
            save.add_oxygen(self.oxygenTemperature, self.oxygenOffset)
            params_save_flag = True
        if (self.turb_coef_a != None):
            save.add_turbidity([self.turb_coef_a, self.turb_coef_b, self.turb_coef_c])
            params_save_flag = True
        save.save()

        if (not params_save_flag):
            self.show_dialog_error('No realizo ninguna calibración')
        else:
            self.show_dialog_error('Calibración exitosa')
