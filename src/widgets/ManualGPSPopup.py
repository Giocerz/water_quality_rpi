from PySide2.QtWidgets import QGraphicsOpacityEffect, QStackedLayout, QWidget
from PySide2 import QtCore
from src.views.ui_ManualGPSPopup import Ui_Form
from src.widgets.KeyboardWidget import NumericKeyboardWidget
from src.widgets.PopupWidget import PopupWidgetInfo

class SetManualLocationWidget(QWidget):
    def __init__(self, context, set_location:callable):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.context = context
        self.set_location:callable = set_location
        self.init_ui_components()

        self.ui.closeBtn.clicked.connect(self.on_close_clicked)
        self.ui.confirmBtn.clicked.connect(self.on_confirm_clicked)
        self.ui.lblOpacity.mousePressEvent = self.background_clicked
        self.ui.latitudeInput.mousePressEvent = self.set_latitude_focus
        self.ui.longitudeInput.mousePressEvent = self.set_longitude_focus

    def init_ui_components(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.keyboard = NumericKeyboardWidget(self.ui.latitudeInput)
        layout = QStackedLayout(self.ui.widgetKeyboard)
        layout.addWidget(self.keyboard)
        self.ui.widgetKeyboard.setLayout(layout)
        self.setParent(self.context)

    def set_latitude_focus(self, event):
        self.keyboard.changeFocusKeyboard(self.ui.latitudeInput)
    
    def set_longitude_focus(self, event):
        self.keyboard.changeFocusKeyboard(self.ui.longitudeInput)

    def on_confirm_clicked(self):
        try:
            latitude = float(self.ui.latitudeInput.text().strip())
            longitude = float(self.ui.longitudeInput.text().strip())

            # Verificar que sean valores de latitud y longitud válidos
            if not (-90 <= latitude <= 90):
                raise ValueError("La latitud debe estar<br>entre -90 y 90 grados.")

            if not (-180 <= longitude <= 180):
                raise ValueError("La longitud debe estar<br>entre -180 y 180 grados.")

        except ValueError as e:
            # Personalizar el mensaje según el tipo de error
            if "could not convert string to float" in str(e):
                error_message = "Ingrese valores numéricos<br>válidos para latitud y longitud."
            else:
                error_message = str(e)

            popup = PopupWidgetInfo(context=self.context, text=error_message)
            popup.show()

            # Limpiar los campos de entrada en caso de error
            self.ui.latitudeInput.setText("")
            self.ui.longitudeInput.setText("")
            return

        self.set_location(latitude, longitude)
        self.close_and_delete()

        
    def background_clicked(self, event):
        self.close_and_delete() 

    def on_close_clicked(self): 
        self.close_and_delete() 

    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()