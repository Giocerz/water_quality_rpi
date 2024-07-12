import sys
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QIODevice
from src.views.ui_Main import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        QMainWindow. __init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.bluetoothBtn.clicked.connect(self.on_bluetooth_clicked)

    def on_bluetooth_clicked(self):
        print("Hola")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome = MyApp()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(320)
    widget.setFixedWidth(480)
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exit")   