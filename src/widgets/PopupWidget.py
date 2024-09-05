from PySide2.QtWidgets import QDialog, QApplication, QGraphicsOpacityEffect, QWidget
from PySide2 import QtCore
from src.views.ui_PopupWidget import Ui_Popup


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
    def __init__(self, context, text, button = True):
        super().__init__()
        self.context = context
        self.ui = Ui_Popup()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.ui.LabelInfo.setText(text)
        self.ui.si.hide()
        self.ui.no.hide()
        if(button):
            self.ui.no.show()
            self.ui.no.setText('OK')
            self.ui.lblOpacity.mousePressEvent = self.handle_click

        self.ui.no.clicked.connect(self.ok_clicked)
        self.setParent(self.context)


    def ok_clicked(self):
        self.close_and_delete()
    
    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()
    
    def handle_click(self, event):
        self.close_and_delete()