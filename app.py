import sys
import time
from pynput.mouse import Controller, Button
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide2.QtCore import QThread, Signal
from src.views.TopBarView.TopBarView import TopBarView
from src.views.MainMenuView.MainMenuView import MainMenuView
from src.logic.PCF8574 import PCF8574


class ButtonListener(QThread):
    def __init__(self, parent=None):
        super(ButtonListener, self).__init__(parent)
        self.running = True
        self.pcf8574 = PCF8574()
        self.distance = 1
        self.flag_center_clicked = False
        self.tick = time.time_ns() / 1e6

    def run(self):
        mouse_controller = Controller()
        try:
            while self.running:
                if self.pcf8574.read_P0():
                    mouse_controller.move(-self.distance, 0)
                if self.pcf8574.read_P1():
                    mouse_controller.move(0, self.distance)
                if self.pcf8574.read_P3():
                    mouse_controller.move(self.distance, 0)
                if self.pcf8574.read_P4():
                    mouse_controller.move(0, -self.distance)
                

                tock = time.time_ns() / 1e6
                if not self.flag_center_clicked and self.pcf8574.read_P2():
                    mouse_controller.click(Button.left)
                    self.flag_center_clicked = True
                    self.tick = tock
                elif self.flag_center_clicked and tock - self.tick >= 300:
                    self.flag_center_clicked = False

                time.sleep(0.01)
        except Exception as e:
            print(f"Error con GPIO: {e}")
        finally:
            self.running = False

    def stop(self):
        self.running = False
        self.wait()

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(480, 320)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self.top_bar = QtWidgets.QStackedWidget()
        self.top_bar.setFixedSize(480, 48)  
        self.main_layout.addWidget(self.top_bar)
        
        self.bottom_widget = QtWidgets.QStackedWidget()
        self.bottom_widget.setFixedSize(480, 272)
        self.main_layout.addWidget(self.bottom_widget)
        
        top_bar_view = TopBarView(context= self.bottom_widget)
        self.top_bar.addWidget(top_bar_view)

        main_menu_view = MainMenuView(context= self.bottom_widget)
        self.bottom_widget.addWidget(main_menu_view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome = MyApp()
    button_listener = ButtonListener()
    button_listener.start()

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
    finally:
        button_listener.stop()
        pass
