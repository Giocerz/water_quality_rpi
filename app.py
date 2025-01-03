import sys
import time
import RPi.GPIO as GPIO
from pynput.mouse import Controller, Button
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide2.QtCore import QThread, Signal
from src.views.TopBarView.TopBarView import TopBarView
from src.views.MainMenuView.MainMenuView import MainMenuView


class ButtonListener(QThread):

    def __init__(self, button_pins, parent=None):
        super(ButtonListener, self).__init__(parent)
        self.button_pins = button_pins
        self.running = True
        self.pressed_times = {pin: None for pin in button_pins}
        GPIO.setmode(GPIO.BCM)

        for pin in self.button_pins:
            GPIO.setup(pin, GPIO.IN)

    def run(self):
        mouse_controller = Controller()  # Controlador de mouse
        try:
            while self.running:
                for i, pin in enumerate(self.button_pins):
                    if GPIO.input(pin) == GPIO.LOW:
                        if self.pressed_times[pin] is None:
                            self.pressed_times[pin] = time.time()
                        press_duration = time.time() - self.pressed_times[pin]
                        base_speed = 10
                        acceleration = min(press_duration * 10, 100) 
                        distance = int(base_speed + acceleration)

                        if i == 0:
                            print(f"Movimiento: Arriba ({distance}px)")
                            mouse_controller.move(0, -distance)
                        elif i == 1:
                            print(f"Movimiento: Abajo ({distance}px)")
                            mouse_controller.move(0, distance)
                        elif i == 2:
                            print(f"Movimiento: Izquierda ({distance}px)")
                            mouse_controller.move(-distance, 0)
                        elif i == 3:
                            print(f"Movimiento: Derecha ({distance}px)")
                            mouse_controller.move(distance, 0)
                        elif i == 4:
                            print("Clic Izquierdo")
                            mouse_controller.click(Button.left)

                    else: 
                        self.pressed_times[pin] = None

                time.sleep(0.01)
        except Exception as e:
            print(f"Error con GPIO: {e}")
        finally:
            self.running = False
            GPIO.cleanup()

    def stop(self):
        self.running = False
        GPIO.cleanup()
        self.wait()


class ButtonListener2(QThread):
    button_pressed = Signal()

    def __init__(self, button_pin):
        super(ButtonListener, self).__init__()
        self.button_pin = button_pin
        self.app = app
        self.running = True

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN)

    def run(self):
            try:
                while self.running:
                    if GPIO.input(self.button_pin) == GPIO.LOW:
                        time.sleep(0.3) 
                        if GPIO.input(self.button_pin) == GPIO.LOW:
                            self.button_pressed.emit()
                    time.sleep(0.01)
            except GPIO.error as e:
                pass
            finally:
                self.running = False
                GPIO.cleanup()

    def stop(self):
        self.running = False
        GPIO.cleanup()


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
    button_pins = [5, 24, 22, 23, 27]

    #button_listener = ButtonListener(button_pins)
    #button_listener.start()

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
