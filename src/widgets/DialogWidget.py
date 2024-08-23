from PySide2.QtWidgets import QDialog, QApplication, QGraphicsOpacityEffect
from PySide2 import QtCore
from src.views.ui_Dialog import Ui_Dialog


class DialogWidget(QDialog):
    def __init__(self, yes_callback, no_callback, text):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.yes_callback = yes_callback
        self.no_callback = no_callback

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.ui.LabelInfo.setText(text)

        self.ui.si.clicked.connect(self.yes_clicked)
        self.ui.no.clicked.connect(self.no_clicked)

        self.adjust_size_and_center()

    def adjust_size_and_center(self):
        screen_rect = QApplication.desktop().availableGeometry()
        screen_width = screen_rect.width()
        screen_height = screen_rect.height()
        dialog_width = 480
        dialog_height = 320
        x = (screen_width - dialog_width) / 2
        y = (screen_height - dialog_height) / 2
        self.move(int(x), int(y))


    def yes_clicked(self):
        if self.yes_callback:
            self.yes_callback()
        self.close()

    def no_clicked(self):
        if self.no_callback:
            self.no_callback()
        self.close()


class DialogWidgetInfo(QDialog):
    def __init__(self, text):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.ui.LabelInfo.setText(text)
        self.ui.si.hide()
        self.ui.no.setText('OK')

        self.ui.no.clicked.connect(self.ok_clicked)

        self.adjust_size_and_center()

    def adjust_size_and_center(self):
        screen_rect = QApplication.desktop().availableGeometry()
        screen_width = screen_rect.width()
        screen_height = screen_rect.height()
        dialog_width = 480
        dialog_height = 320
        x = (screen_width - dialog_width) / 2
        y = (screen_height - dialog_height) / 2
        self.move(int(x), int(y))

    def ok_clicked(self):
        self.close()