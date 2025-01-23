import sys
# import struct
import time
from datetime import datetime
import random
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedLayout, QTableWidgetItem, QVBoxLayout, QWidget, QGridLayout, QSizePolicy
from PySide2.QtCore import QSize, QThread, Signal, Slot, QTimer
from PySide2.QtGui import QIcon, QPixmap
from src.views.ui_MainLayout import Ui_MainLayout
import src.views.ui_MainMenu as MainMenu
import src.views.ui_Monitoring3 as Monitoring3
import src.views.ui_Top_Bar as TopBar
import src.views.ui_Save as Save_View
import src.views.ui_Calibration as Calibration_View
from src.views.DatosView.DatosView import DatosView
import src.views.ui_Graphics_view as Graph_View
from src.widgets.DialogWidget import DialogWidget, DialogWidgetInfo
from src.views.FoldersView.FoldersView import FoldersView
from src.widgets.FolderWidget import FolderWidget
from src.logic.saveCalibration import SaveCalibration
from src.views.EditCalibrationValuesView.EditCalibrationValuesView import EditCalibrationValuesView
from src.views.WifiView.WifiView import WifiView
# from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import *
# from src.services.bluetoothLE import BluetoothWorker
from src.widgets.KeyboardWidget import KeyboardWidget
from src.widgets.PopupWidget import PopupWidget, PopupWidgetInfo, LoadingPopupWidget
from src.model.WaterQualityParams import WaterQualityParams
from src.model.LoteModel import LoteModel
from src.model.WaterQualityDB import WaterDataBase
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class ParametersMeasuredWorker(QThread):
    parameters_result = Signal(list)

    def __init__(self):
        super(ParametersMeasuredWorker, self).__init__()

    def run(self):
        self.running_state = True
        paraamCalc = ParametersCalculate()
        bat = 50
        while self.running_state:
            try:
                temp = round(random.uniform(29, 33), 2)
                ph = round(random.uniform(6.1, 7.32), 2)
                do = round(random.uniform(4.55, 5.89), 2)
                tds = round(random.uniform(724.23, 892.23), 2)
                turb = round(random.uniform(56.23, 203.23), 2)

                self.parameters_result.emit([ph, do, tds, temp, turb, bat])
                time.sleep(1)
                bat -= 2
            except Exception as e:
                print(e)

    def stop(self):
        self.running_state = False
        self.wait()


class MainLayout(QMainWindow):
    def __init__(self):
        super().__init__()

        # Dimensiones de la ventana principal
        self.setFixedSize(480, 320)

        # Contenedor principal
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Layout principal
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes
        self.main_layout.setSpacing(0)

        # TopBar
        self.top_bar = QtWidgets.QStackedWidget()
        self.top_bar.setFixedSize(480, 48)
        self.main_layout.addWidget(self.top_bar)

        # BottomWidget (QStackedWidget)
        self.bottom_widget = QtWidgets.QStackedWidget()
        self.bottom_widget.setFixedSize(480, 272)  # 480x272 píxeles
        self.main_layout.addWidget(self.bottom_widget)

        top_bar_view = TopBarView(context=self.bottom_widget)
        self.top_bar.addWidget(top_bar_view)

        main_menu_view = MainView(context=self.bottom_widget)
        self.bottom_widget.addWidget(main_menu_view)


class TopBarView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = TopBar.Ui_Form()
        self.ui.setupUi(self)

        pixmap = QPixmap('./src/resources/icons/electric_bolt_b.png')
        scaled_pixmap = pixmap.scaled(
            26, 26, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.chargeIndicator.setPixmap(scaled_pixmap)
        pixmap = QPixmap('./src/resources/icons/wifi_icons/wifi_off.png')
        scaled_pixmap = pixmap.scaled(QSize(31, 31))
        self.ui.networkLbl.setPixmap(scaled_pixmap)

        self.low_battery_flag = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_top_bar)
        self.timer.start(1000)

    def update_top_bar(self):
        self.update_battery()
        self.update_time()

    def update_time(self):
        hour = datetime.now().strftime("%H:%M")
        self.ui.timeLbl.setText(hour)

    def update_battery(self):
        battery_level = self.get_battery_level()
        self.ui.batteryLbl.setText(f'{round(battery_level)}%')
        self.ui.batteryLbl.setAlignment(QtCore.Qt.AlignLeft)
        # print(f'battery_level: {battery_level}')
        if (battery_level < 25 and battery_level >= 10):
            color = '252, 163, 17'
            if (not self.low_battery_flag):
                # self.open_battery_popup()
                self.low_battery_flag = True
        elif (battery_level < 10):
            color = '230, 57, 70'
        else:
            color = '0, 0, 127'
            self.low_battery_flag = False

        if (battery_level == 100):
            percent = 0
        elif (battery_level == 0):
            percent = 0.95
        else:
            percent = round((-0.81633 * battery_level + 90.81633)/100.0, 2)

        # print(f'percent: {percent}')
        self.ui.baterryLevel.setStyleSheet(
            f'background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,stop:0 rgba(255, 255, 255, 255),stop:{percent} rgba(255, 255, 255, 255), stop:{percent + 0.01} rgba({color}, 255), stop:1 rgba({color}, 255));border-radius: 12px;')

    def open_battery_popup(self):
        popup = PopupWidgetInfo(context=self.context,
                                text='Batería baja, conecte el cargador')
        popup.show()

    def get_battery_level(self):
        # Simulación: reemplazar con código real para consultar el nivel de batería
        import random
        return random.randint(0, 100)


class MainView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = MainMenu.Ui_MainWindow()
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
        icon = QIcon('./src/resources/icons/wifi.png')
        self.ui.wifiBtn.setIcon(icon)
        self.ui.wifiBtn.setIconSize(QSize(30, 30))


    def on_monitoring_clicked(self):
        self.open_view(MonitoringView(context=self.context))

    def on_calibration_clicked(self):
        self.open_view(CalibrationView(context=self.context))

    def on_datos_clicked(self):
        self.open_view(FoldersView(context=self.context))

    def on_bluetooth_clicked(self):
        print('ble')

    def on_wifi_clicked(self):
        self.open_view(WifiView(context=self.context))

    def on_edit_clicked(self):
        self.open_view(EditCalibrationValuesView(context=self.context))

    def open_view(self, view):
        self.context.addWidget(view)
        self.context.setCurrentIndex(self.context.currentIndex() + 1)


class MonitoringView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Monitoring3.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.oxygen = None
        self.ph = None
        self.temperature = None
        self.tds = None
        self.turbidity = None

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

    def show_dialog_error(self, error: str):
        dialog = PopupWidgetInfo(context=self.context, text=error)
        dialog.show()

    def on_back_clicked(self):
        if self.parameters_worker.isRunning():
            self.parameters_worker.stop()
        self.context.removeWidget(self)

    def on_save_clicked(self):
        if (not self.receive_parameters):
            return
        view = SaveDataView(context=self.context, oxygen=self.oxygen, ph=self.ph,
                            temperature=self.temperature, tds=self.tds, turbidity=self.turbidity)
        self.context.addWidget(view)
        self.context.setCurrentIndex(self.context.currentIndex() + 1)
        self.parameters_worker.stop()
        self.context.removeWidget(self)

    def on_pause_clicked(self):
        if (self.isPause):
            if not self.parameters_worker.isRunning():
                self.parameters_worker.start()
                self.ui.pauseBtn.setText('Pausar')
                self.isPause = False
        else:
            if self.parameters_worker.isRunning():
                self.parameters_worker.stop()
                self.ui.pauseBtn.setText('Reanudar')
                self.isPause = True

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


class SaveDataView(QMainWindow):
    def __init__(self, context, oxygen, ph, temperature, tds, turbidity):
        QMainWindow.__init__(self)
        self.context = context
        self.oxygen = oxygen
        self.ph = ph
        self.temperature = temperature
        self.tds = tds
        self.turbidity = turbidity
        self.folder_name: str = None

        self.ui = Save_View.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.keyboard = KeyboardWidget(self.ui.inputPlace)
        layout = QStackedLayout(self.ui.widgetKeyboard)
        layout.addWidget(self.keyboard)
        self.ui.widgetKeyboard.setLayout(layout)

        self.keyboard2 = KeyboardWidget(self.ui.folderName)
        layout = QStackedLayout(self.ui.widgetKeyboard2)
        layout.addWidget(self.keyboard2)
        self.ui.widgetKeyboard2.setLayout(layout)

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.gpsBtn.clicked.connect(self.on_gps_clicked)
        self.ui.saveBtn.clicked.connect(self.on_save_clicked)
        self.ui.nextBtn.clicked.connect(self.on_next_clicked)
        self.ui.prevBtn.clicked.connect(self.on_prev_clicked)
        self.ui.selectFolderBtn.clicked.connect(self.on_select_folder_clicked)
        self.ui.openCreateFolderBtn.clicked.connect(
            self.on_open_create_folder_clicked)
        self.ui.createFolderBtn.clicked.connect(self.on_create_folder_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_gps_clicked(self):
        self.loading_popup = LoadingPopupWidget(
            context=self.context, text='Localizando...')
        self.loading_popup.show()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.finish_loading)
        self.timer.start(5000)

    def finish_loading(self):
        self.loading_popup.close_and_delete()
        self.timer.stop()

    def on_back_clicked(self):
        self.show_dialog()

    def on_next_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_prev_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_select_folder_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_open_create_folder_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_create_folder_clicked(self):
        name = self.ui.folderName.text().strip()
        if (name == ""):
            self.show_dialog_error(error='Ingrese el nombre de la carpeta')
            return
        self.folder_name = name
        self.ui.folderLbl.setText(name)
        self.ui.folderLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_dialog_error(self, error: str):
        dialog = PopupWidgetInfo(context=self.context, text=error)
        dialog.show()

    def show_dialog(self):
        def on_yes():
            self.context.removeWidget(self)

        def on_no():
            pass
        dialog = PopupWidget(context=self.context, yes_callback=on_yes, no_callback=on_no,
                             text='No se han guardado los datos<br>¿Desea salir?')
        dialog.show()

    def on_save_clicked(self):
        place = self.ui.inputPlace.text().strip()
        sample_origin = self.ui.comboBox.currentText()
        # Obtener la fecha actual
        from datetime import datetime
        dtatetime_now = datetime.now()
        format_date = dtatetime_now.strftime("%Y-%m-%d")
        hour = dtatetime_now.strftime("%H:%M")
        if (place == ''):
            self.show_dialog_error(error='Ingrese un nombre válido')
            self.ui.stackedWidget.setCurrentIndex(0)
            return
        if (sample_origin == 'Escoja una opción'):
            self.show_dialog_error(error='Seleccione el origen de la muestra')
            self.ui.stackedWidget.setCurrentIndex(1)
            return
        if (not self.folder_name):
            self.show_dialog_error(error='Seleccione una carpeta')
            self.ui.stackedWidget.setCurrentIndex(1)
            return
        it_rained_check = self.ui.checkBox.checkState()
        it_rained = ''
        if (it_rained_check):
            it_rained = 'Si'
        else:
            it_rained = 'No'
        lote = LoteModel(
            name=self.folder_name,
            creation_date=format_date,
            creation_hour=str(hour),
            last_add_date=format_date,
            last_add_hour=str(hour),
        )
        lote_id = WaterDataBase.insert_lote(lote)
        params = WaterQualityParams(
            name=place, device_id="Device123", latitude=4.6097, longitude=-74.0817,
            date=format_date, hour=str(hour), sample_origin=sample_origin, it_rained=it_rained,
            upload_state=1, lote_id=lote_id, conductivity=self.tds * 2, oxygen=self.oxygen, ph=self.ph,
            temperature=self.temperature, tds=self.tds, turbidity=self.turbidity
        )
        WaterDataBase.insert_water_param(params)
        finish_popup = PopupWidgetInfo(
            context=self.context, text="La muestra se guardó exitosamente", on_click=self.on_back_clicked)
        finish_popup.show()


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

    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Calibration_View.Ui_MainWindow()
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

    ######### FUNCIONES PARA CADA PASO#################
    def handle_tds(self) -> bool:
        try:
            kValue_temp = 1.2
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
        self.ph_offset = 2.7
        return True

    def handle_ph4(self):
        ph4_voltage = 3.0
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
            return True

    def handle_turb1(self):
        # self.ph_offset = self.parameters_volt.turbidity_volt()
        return True

    def handle_turb2(self):
        # self.ph_offset = self.parameters_volt.turbidity_volt()
        return True

    def handle_turb3(self):
        # self.ph_offset = self.parameters_volt.turbidity_volt()
        return True

    def handle_turb4(self):
        # self.ph_offset = self.parameters_volt.turbidity_volt()
        return True

    def handle_do(self):
        vCal = 1.76
        tempCal = 25.54
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
        if (self.oxygenOffset != None):
            df.loc[3, 'calibration_values'] = self.oxygenTemperature
            df.loc[4, 'calibration_values'] = self.oxygenOffset
            params_save_flag = True
        df.to_csv('./src/config/calibrationSettings.txt', index=False)

        if (params_save_flag):
            self.show_dialog_error('No realizo ninguna calibración')
        else:
            self.show_dialog_error('Calibración exitosa')


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class CustomNavigationToolbar(NavigationToolbar):
    def __init__(self, canvas, parent=None):
        super(CustomNavigationToolbar, self).__init__(canvas, parent)

        # Lista de herramientas que deseas mostrar
        # Ajusta según lo que necesites
        tools_to_keep = ['home', 'pan', 'zoom']

        # Ocultar herramientas no deseadas
        for action in self.actions():
            if action.text().lower() not in tools_to_keep:
                self.removeAction(action)


class GraphView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Graph_View.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.load_data()
        self.canvas_init()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        self.context.removeWidget(self)

    def load_data(self):
        self.data_list = WaterDataBase.get_water_quality_params()
        self.conductivity_values = [
            data.conductivity for data in self.data_list]

    def canvas_init(self):
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        x = range(len(self.conductivity_values))
        y = self.conductivity_values
        self.sc.axes.plot(x, y, label='Conductividad')
        self.sc.axes.set_xlabel('muestras')
        self.sc.axes.set_ylabel('uS/cm')
        self.sc.axes.legend()

        toolbar = CustomNavigationToolbar(self.sc, self)
        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignRight)
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)
        self.ui.graphWidget.setLayout(layout)


if __name__ == '__main__':
    save = SaveCalibration()
    app = QApplication(sys.argv)

    # Inicializar la aplicación
    main_layout = MainLayout()
    main_layout.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Sin bordes
    main_layout.show()

    try:
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error al cerrar: {e}")
