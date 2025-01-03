from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize, QThread, Signal
from PySide2.QtGui import QIcon, QPixmap
from src.views.ui_Folders_view import Ui_MainWindow


class FoldersView(QMainWindow):
    def __init__(self, context):
        QMainWindow().__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        self.context.removeWidget(self)
