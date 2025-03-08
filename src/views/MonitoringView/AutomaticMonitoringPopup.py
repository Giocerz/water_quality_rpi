from PySide2.QtWidgets import QWidget
from PySide2 import QtCore
from src.views.ui_AutomaticMonitoringPopup import Ui_Form
from src.widgets.PopupWidget import PopupWidgetInfo
from src.package.Timer import Timer

class AutomaticMonitoringPopup(QWidget):
    def __init__(self, context, period:int, total_samples:int, current_samples:int, set_capture_samples:callable):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.context = context
        self.period:int = period
        self.total_samples:int = total_samples
        self.current_samples:int = current_samples
        self.set_capture_samples:callable = set_capture_samples
        self.init_ui_components()

    def init_ui_components(self):
        if self.total_samples == self.current_samples:
            self.close_and_delete()
            return
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.countLbl.setText(f'{self.current_samples}/{self.total_samples}')
        self.ui.countLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.setParent(self.context)
        self.ui.stopBtn.clicked.connect(self.on_stop_clicked)
        self.init_timers()
    
    def init_timers(self):
        self.measure_timer = Timer.periodic(duration=self.period*1000, callback=self.set_new_capture)
        self.measure_timer.start()

        self.rotation_step = 0
        self.anim_timer = Timer.periodic(duration= 300, callback= self.update_border_style)
        self.anim_timer.start()

    def set_new_capture(self):
        self.set_capture_samples()
        self.current_samples += 1
        self.ui.countLbl.setText(f'{self.current_samples}/{self.total_samples}')
        self.ui.countLbl.setAlignment(QtCore.Qt.AlignCenter)
        if self.current_samples == self.total_samples:
            self.stop_timers()
            popup = PopupWidgetInfo(context=self.context, text='Se completaron las capturas', on_click=self.close_and_delete)
            popup.show()

    def update_border_style(self):
        border_styles = [
            "border-top: 5px solid #00007f;",  # Azul arriba
            "border-right: 5px solid #00007f;",  # Azul derecha
            "border-bottom: 6px solid #00007f;",  # Azul abajo
            "border-left: 6px solid #00007f;",  # Azul izquierda
        ]
        # Actualizar el estilo según el paso actual de la rotación
        current_border = border_styles[self.rotation_step % 4]
        # Estilo general del widget
        self.ui.IconInfo.setStyleSheet(f"""
                border: 6px solid #ced4da;
                border-radius: 20px;
                {current_border}
        """)
        self.rotation_step += 1

    def on_stop_clicked(self):
        self.stop_timers()
        self.close_and_delete() 

    def stop_timers(self):
        self.measure_timer.cancel()
        self.anim_timer.cancel()

    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()