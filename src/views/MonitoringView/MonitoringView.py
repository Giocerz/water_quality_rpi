from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QGridLayout, QSizePolicy
from PySide2.QtCore import QSize, QThread, Signal, QPropertyAnimation, QSequentialAnimationGroup, QEasingCurve, QRect
from PySide2.QtGui import QIcon
from src.views.ui_Monitoring import Ui_MainWindow
from src.widgets.ParametersIndicator import ParametersIndicator
from src.logic.AppConstans import AppConstants
import time
from w1thermsensor import W1ThermSensor
from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import *
from src.views.SaveDataView.SaveDataView import SaveDataView
from src.views.SaveDataView.SaveSelectView import SaveSelectView
from src.package.Navigator import Navigator
from src.logic.batteryLevel import BatteryProvider
from src.logic.filters import MovingAverageFilter
from src.widgets.PopupWidget import PopupWidgetInfo
from src.views.MonitoringView.AutomaticMonitoringPopup import AutomaticMonitoringPopup
from src.views.MonitoringView.MonitoringOptionsPopup import MonitoringOptionsPopup
from src.model.SensorData import SensorData
from src.logic.sensorStabilizer import SensorStabilizer

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
    def __init__(self, context, tds_check:bool, ph_check:bool, oxygen_check:bool, turbidity_check:bool):
        QMainWindow.__init__(self)
        self.context = context
        self.tds_check:bool = tds_check
        self.ph_check:bool = ph_check
        self.oxygen_check:bool = oxygen_check
        self.turbidity_check:bool = turbidity_check
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.setup_grid()
        self.init_animation()
        self.init_stabilizers()

        self.oxygen = None
        self.ph = None
        self.temperature = None
        self.tds = None
        self.turbidity = None
        self.battery = None

        self.max_samples:int = 15
        self.capture_period:int = 3
        self.is_automatic_capture_active = False
        self.capture_samples:list[SensorData] = []

        self.receive_parameters = False
        
        self.isPause = False


        self.parameters_worker = ParametersMeasuredWorker()
        if not self.parameters_worker.isRunning():
            self.parameters_worker.start()

        self.ui.captureBtn.clicked.connect(self.on_capture_clicked)
        self.ui.optionsBtn.clicked.connect(self.on_options_clicked)
        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.saveBtn.clicked.connect(self.on_save_clicked)
        self.ui.pauseBtn.clicked.connect(self.on_pause_clicked)

        self.parameters_worker.parameters_result.connect(
            self.handle_parameters_result)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/more.png')
        self.ui.optionsBtn.setIcon(icon)
        self.ui.optionsBtn.setIconSize(QSize(30, 30))
        self.ui.captureCountLbl.setText('')
        self.ui.captureCountLbl.hide()

    def init_stabilizers(self):
        self.tds_stabilization:SensorStabilizer = SensorStabilizer(
            window_size=AppConstants.MONITORING_STABLE_TDS['window'],
            threshold=AppConstants.MONITORING_STABLE_TDS['threshold'],
            is_stable_number=AppConstants.MONITORING_STABLE_TDS['repeat']
        )

        self.ph_stabilization:SensorStabilizer = SensorStabilizer(
            window_size=AppConstants.MONITORING_STABLE_PH['window'],
            threshold=AppConstants.MONITORING_STABLE_PH['threshold'],
            is_stable_number=AppConstants.MONITORING_STABLE_PH['repeat']
        )

        self.do_stabilization:SensorStabilizer = SensorStabilizer(
            window_size=AppConstants.MONITORING_STABLE_DO['window'],
            threshold=AppConstants.MONITORING_STABLE_DO['threshold'],
            is_stable_number=AppConstants.MONITORING_STABLE_DO['repeat']
        )

        self.turbidity_stabilization:SensorStabilizer = SensorStabilizer(
            window_size=AppConstants.MONITORING_STABLE_TURBIDITY['window'],
            threshold=AppConstants.MONITORING_STABLE_TURBIDITY['threshold'],
            is_stable_number=AppConstants.MONITORING_STABLE_TURBIDITY['repeat']
        )
        self.tds_is_stable:bool = False
        self.ph_is_stable:bool = False
        self.do_is_stable:bool = False
        self.turbidity_is_stable:bool = False


    def on_back_clicked(self):
        if self.parameters_worker.isRunning():
            self.parameters_worker.stop()
        Navigator.pop(context=self.context, view= self)
    
    def pause_monitoring(self):
        if self.parameters_worker.isRunning():
                self.parameters_worker.stop()
        self.ui.pauseBtn.setText('Reanudar')
        self.isPause = True

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
        self.pause_monitoring()
        if len(self.capture_samples) > 1:
            view = SaveSelectView(context=self.context, capture_samples=self.capture_samples, close_monitoring_callback=self.on_back_clicked)
        elif len(self.capture_samples) > 0:
            view = SaveDataView(context=self.context, capture_samples=self.capture_samples, close_monitoring_callback=self.on_back_clicked)
        else:
            sample = SensorData(
                    temperature=self.temperature,
                    ph=self.ph,
                    tds=self.tds,
                    conductivity=None if self.tds is None else self.tds * 2,
                    oxygen=self.oxygen,
                    turbidity=self.turbidity,
                    battery=self.battery)
            view = SaveDataView(context=self.context, capture_samples=[sample], close_monitoring_callback=self.on_back_clicked)
        Navigator.push(context=self.context, view=view)
    
    def init_animation(self):
        self.original_rect = self.ui.captureCountLbl.geometry()
        self.up_rect = QRect(self.original_rect.x(), self.original_rect.y() - 50, 
                             self.original_rect.width(), self.original_rect.height())

        # Crear las animaciones
        self.up_animation = QPropertyAnimation(self.ui.captureCountLbl, b"geometry")
        self.up_animation.setDuration(300)
        self.up_animation.setStartValue(self.original_rect)
        self.up_animation.setEndValue(self.up_rect)
        self.up_animation.setEasingCurve(QEasingCurve.OutQuad)  # Suave al subir

        self.down_animation = QPropertyAnimation(self.ui.captureCountLbl, b"geometry")
        self.down_animation.setDuration(500)
        self.down_animation.setStartValue(self.up_rect)
        self.down_animation.setEndValue(self.original_rect)
        self.down_animation.setEasingCurve(QEasingCurve.OutBounce)  # Rebote al caer

        # Grupo de animaciones en secuencia
        self.animation_group = QSequentialAnimationGroup()
        self.animation_group.addAnimation(self.up_animation)
        self.animation_group.addAnimation(self.down_animation)

    def on_capture_clicked(self):
        if not self.receive_parameters:
            return
        if len(self.capture_samples) >= self.max_samples:
            popup = PopupWidgetInfo(context=self.context, text=f'Solo puededs capturar un<br>máximo de {self.max_samples} muestras')
            popup.show()
            return
        if self.is_automatic_capture_active:
            self.init_automatic_capture()
            return
        self.set_capture_samples()
        self.start_animation()
    
    def set_capture_samples(self):
        self.capture_samples.append(SensorData(
            temperature=self.temperature,
            ph=self.ph,
            tds=self.tds,
            conductivity=None if self.tds is None else self.tds * 2,
            oxygen=self.oxygen,
            turbidity=self.turbidity,
            battery=self.battery
        ))
        self.ui.captureCountLbl.setText(f'+{len(self.capture_samples)}')
        self.ui.captureCountLbl.show()

    def start_animation(self):
        """Inicia la animación completa al presionar el botón."""
        self.animation_group.start()

    def setup_grid(self):
        main_layout = QVBoxLayout(self.ui.indicatorsWidget)
        main_layout.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0, 0, 0, 0)

        num_parameters = self.tds_check * 2 + self.ph_check + self.oxygen_check + self.turbidity_check + 1
        parameter_indicator_size = 'L' if num_parameters <= 2 else 'M' if num_parameters <= 3 else 'S'
        num_cols = 1 if num_parameters <= 3 else 2
        
        pos = 0
        self.indicators = {}

        # Lista de parámetros activados en base a los CheckBox
        self.parameters_keys = ["temperature"]
        if self.tds_check:
            self.parameters_keys.extend(["tds", "conductivity"])
        if self.ph_check:
            self.parameters_keys.append("ph")
        if self.oxygen_check:
            self.parameters_keys.append("oxygen")
        if self.turbidity_check:
            self.parameters_keys.append("turbidity")

        for param_key in self.parameters_keys:
            param_info = AppConstants.PARAMS_ATTRIBUTES.get(param_key, {})
            name = param_info.get("name", "")

            unit = param_info.get("unit", "")
            if isinstance(unit, list):  # Si hay varias unidades, usar la primera
                unit = unit[0]

            # Extraer valores de los límites
            min_value = param_info.get("minValue")
            max_value = param_info.get("maxValue")
            lower_limit = param_info.get("lowerLimit")
            upper_limit = param_info.get("upperLimit")
            significant_figures = param_info.get("significant_figures")

            # Crear el widget `ParametersIndicator` con todos los valores necesarios
            self.indicators[param_key] = ParametersIndicator(
                name=name,
                unit=unit,
                widget_size=parameter_indicator_size,
                min_value=min_value,
                max_value=max_value,
                lower_limit=lower_limit,
                upper_limit=upper_limit,
                significant_figures = significant_figures
            )

            recommended_size = self.indicators[param_key].sizeHint()
            self.indicators[param_key].setMinimumSize(recommended_size)
            self.indicators[param_key].setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

            row = pos // num_cols
            col = pos % num_cols

            grid_layout.setRowMinimumHeight(row, 70)
            grid_layout.setColumnMinimumWidth(col, 240)
            grid_layout.addWidget(self.indicators[param_key], row, col)

            pos += 1

        main_layout.addLayout(grid_layout)

    def handle_parameters_result(self, parameters):
        self.receive_parameters = True
        
        self.temperature = parameters[0]
        self.indicators['temperature'].setValue(self.temperature)

        if self.oxygen_check:
            self.oxygen = parameters[1]
            self.do_is_stable = self.do_stabilization.value_is_stable(self.oxygen)
            self.indicators['oxygen'].setValue(self.oxygen)
            self.indicators['oxygen'].setStable(self.do_is_stable)

        if self.tds_check:
            self.tds = parameters[2]
            self.td_is_stable = self.tds_stabilization.value_is_stable(self.tds)
            self.indicators['tds'].setValue(self.tds)
            self.indicators['tds'].setStable(self.td_is_stable)
            self.indicators['conductivity'].setValue(self.tds * 2)
            self.indicators['conductivity'].setStable(self.td_is_stable)

        if self.ph_check:
            self.ph = parameters[3]
            self.ph_is_stable = self.ph_stabilization.value_is_stable(self.ph)
            self.indicators['ph'].setValue(self.ph)
            self.indicators['ph'].setStable(self.ph_is_stable)

        if self.turbidity_check:
            self.turbidity = parameters[4]
            self.turbidity_is_stable = self.turbidity_stabilization.value_is_stable(self.turbidity)
            self.indicators['turbidity'].setValue(self.turbidity)
            self.indicators['turbidity'].setStable(self.turbidity_is_stable)

        
        self.battery = parameters[5]
    
    #Automatic monitoring methods
    def on_options_clicked(self):
        def set_period(period:int):
            self.capture_period = period
        def set_samples(samples:int):
            self.max_samples = samples
        def set_continuous_capture(value:bool):
            self.is_automatic_capture_active = value
        popup = MonitoringOptionsPopup(context=self.context, 
                                       is_continuous_capture_active=self.is_automatic_capture_active, 
                                       totalSamples=self.max_samples,
                                       period=self.capture_period,
                                       set_period=set_period,
                                       set_samples=set_samples,
                                       set_continuous_capture=set_continuous_capture)
        popup.show()
    
    def init_automatic_capture(self):
        if self.isPause:
            popup = PopupWidgetInfo(context=self.context, text='Reanuda la medición para<br>la captura automática.')
            popup.show()
            return
        popup = AutomaticMonitoringPopup(context=self.context, period=self.capture_period, 
                                         total_samples=self.max_samples,
                                         current_samples=len(self.capture_samples),
                                         set_capture_samples=self.set_capture_samples)
        popup.show()