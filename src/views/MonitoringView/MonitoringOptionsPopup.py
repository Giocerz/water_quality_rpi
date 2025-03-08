from PySide2.QtWidgets import QGraphicsOpacityEffect, QStackedLayout, QWidget
from PySide2 import QtCore
from src.views.ui_ConfigMonitoringPopup import Ui_Form
from src.widgets.KeyboardWidget import NumericKeyboardWidget
from src.widgets.PopupWidget import PopupWidgetInfo

class MonitoringOptionsPopup(QWidget):
    def __init__(self, context, is_continuous_capture_active:bool, totalSamples:int, period:int, set_samples:callable, set_period:callable, set_continuous_capture:callable):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.context = context
        self.is_continuous_capture_active:bool = is_continuous_capture_active
        self.total_samples:int = totalSamples
        self.period:int = period
        self.set_samples:callable = set_samples
        self.set_period:callable = set_period
        self.set_continuous_capture:callable = set_continuous_capture
        self.init_ui_components()

        self.ui.closeBtn.clicked.connect(self.on_close_clicked)
        self.ui.confirmBtn.clicked.connect(self.on_confirm_clicked)
        self.ui.lblOpacity.mousePressEvent = self.background_clicked
        self.ui.totalSamplesLine.mousePressEvent = self.set_total_samples_focus
        self.ui.periodLine.mousePressEvent = self.set_period_focus

    def init_ui_components(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.keyboard = NumericKeyboardWidget(self.ui.totalSamplesLine, True)
        layout = QStackedLayout(self.ui.widgetKeyboard)
        layout.addWidget(self.keyboard)
        self.ui.widgetKeyboard.setLayout(layout)
        self.ui.totalSamplesLine.setText(str(self.total_samples))
        self.ui.periodLine.setText(str(self.period))
        self.ui.captureCheckBox.setChecked(self.is_continuous_capture_active)
        self.setParent(self.context)

    def set_total_samples_focus(self, event):
        self.keyboard.changeFocusKeyboard(self.ui.totalSamplesLine)
    
    def set_period_focus(self, event):
        self.keyboard.changeFocusKeyboard(self.ui.periodLine)

    def on_confirm_clicked(self):
        try:
            self.total_samples = int(self.ui.totalSamplesLine.text().strip())
            self.period = float(self.ui.periodLine.text().strip())

            # Verificar que sean valores de latitud y longitud válidos
            if not (5 <= self.total_samples<= 50):
                raise ValueError("El total de muestras debe estar<br>entre 5 y 50")

            if not (2 <= self.period <= 30):
                raise ValueError("El periodo debe debe estar<br>entre 2 y 30 segundos")

        except ValueError as e:
            # Personalizar el mensaje según el tipo de error
            if "invalid literal for int() with base 10" in str(e):
                error_message = "Ingrese valores numéricos enteros<br>válidos."
            else:
                error_message = str(e)

            popup = PopupWidgetInfo(context=self.context, text=error_message)
            popup.show()
            return
        
        continuous_capture_active = self.ui.captureCheckBox.isChecked()
        self.set_samples(self.total_samples)
        self.set_period(self.period)
        self.set_continuous_capture(continuous_capture_active)
        if continuous_capture_active > self.is_continuous_capture_active:
            popup = PopupWidgetInfo(context=self.context, text='La captura automática ha<br>sido activada', on_click=self.close_and_delete)
            popup.show()
            return
        elif continuous_capture_active < self.is_continuous_capture_active:
            popup = PopupWidgetInfo(context=self.context, text='La captura automática ha<br>sido desactivada', on_click=self.close_and_delete)
            popup.show()
            return
        self.close_and_delete()

        
    def background_clicked(self, event):
        self.close_and_delete() 

    def on_close_clicked(self): 
        self.close_and_delete() 

    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()