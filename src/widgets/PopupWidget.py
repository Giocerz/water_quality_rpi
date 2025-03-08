from PySide2.QtWidgets import QGraphicsOpacityEffect, QWidget
from PySide2.QtGui import QPixmap
from PySide2 import QtCore
from src.views.ui_PopupWidget import Ui_Form as Ui_Popup
from src.views.ui_LoadingPopupWidget import Ui_Form as Ui_Loading
from src.views.ui_ProgressPopupWidget import Ui_Form as Ui_Progress
from src.package.Timer import Timer


class PopupWidget(QWidget):
    def __init__(self, context, yes_callback, no_callback, text):
        super().__init__()
        self.context = context
        self.ui = Ui_Popup()
        self.ui.setupUi(self)

        self.yes_callback = yes_callback
        self.no_callback = no_callback

        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.ui.LabelInfo.setText(text)
        pixmap = QPixmap('./src/resources/icons/warning.png')
        pixmap = pixmap.scaled(61,61)
        self.ui.IconInfo.setPixmap(pixmap)

        self.ui.si.clicked.connect(self.yes_clicked)
        self.ui.no.clicked.connect(self.no_clicked)
        self.ui.lblOpacity.mousePressEvent = self.handle_click
        self.setParent(self.context)

    def yes_clicked(self):
        if self.yes_callback:
            self.yes_callback()
        self.close_and_delete()

    def no_clicked(self):
        if self.no_callback:
            self.no_callback()
        self.close_and_delete()
    
    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()
    
    def handle_click(self, event):
        self.close_and_delete()


class PopupWidgetInfo(QWidget):
    def __init__(self, context, text:str, button:bool = True, on_click:callable = None):
        super().__init__()
        self.context = context
        self.on_click:callable = on_click
        self.ui = Ui_Popup()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.ui.LabelInfo.setText(text)
        pixmap = QPixmap('./src/resources/icons/warning.png')
        pixmap = pixmap.scaled(61,61)
        self.ui.IconInfo.setPixmap(pixmap)

        self.ui.si.hide()
        self.ui.no.hide()
        if(button):
            self.ui.no.show()
            self.ui.no.setText('OK')
            self.ui.lblOpacity.mousePressEvent = self.handle_click

        self.ui.no.clicked.connect(self.ok_clicked)
        self.setParent(self.context)


    def ok_clicked(self):
        if self.on_click:
            self.on_click()
        self.close_and_delete()
    
    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()
    
    def handle_click(self, event):
        self.close_and_delete()

class LoadingPopupWidget(QWidget):
    def __init__(self, context, text):
        super().__init__()
        self.context = context
        self.ui = Ui_Loading()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.ui.LabelInfo.setText(text)

        self.rotation_step = 0
        self.timer = Timer.periodic(duration= 300, callback= self.update_border_style)
        self.timer.start()

        self.setParent(self.context)
    
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
                border-radius: 30px;
                {current_border}
        """)
        self.rotation_step += 1
        

    def close_and_delete(self):
        self.timer.cancel()
        self.setParent(None)
        self.deleteLater()


class ProgressPopupWidget(QWidget):
    def __init__(self, context, text):
        super().__init__()
        self.context = context
        self.ui = Ui_Progress()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.ui.LabelInfo.setText(text)
        self.ui.LabelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.progressBar.setValue(0)

        self.setParent(self.context)
    
    def set_value(self, value:int):
        self.ui.progressBar.setValue(value)
        
    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()