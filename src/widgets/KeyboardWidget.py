from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtCore import QThread, Signal, QTimer
from src.views.ui_Keyboard import Ui_Keyboard

class KeyboardWidget(QWidget):
    def __init__(self, focusLine):
        QWidget.__init__(self)
        self.ui = Ui_Keyboard()
        self.ui.setupUi(self)
        self.focusLine = focusLine #atributo de linea texto seleccionada
        self.focusLine.setFocus() #Mantiene el cursor del texto en el line seleccionado

        self.capStatus = False #atributo de estado del boton de capitalizar
        self.numbersCharsStatus = False #Atributo de estado del boton de caracteres
        self.numberCharsStatus_2 = False #Atributo de estado del boton de caracteres extra

        self.timerBackSpace = QTimer(self)
        self.timerBackSpace.setInterval(1000)
        self.timerBackSpace.setSingleShot(True)
        self.timerBackSpace.timeout.connect(self.backspaceHeld)

        self.set_minus()

        #Eventos al presionar
        self.ui.btn1.pressed.connect(self.btnPressed)
        self.ui.btn2.pressed.connect(self.btnPressed)
        self.ui.btn3.pressed.connect(self.btnPressed)
        self.ui.btn4.pressed.connect(self.btnPressed)
        self.ui.btn5.pressed.connect(self.btnPressed)
        self.ui.btn6.pressed.connect(self.btnPressed)
        self.ui.btn7.pressed.connect(self.btnPressed)
        self.ui.btn8.pressed.connect(self.btnPressed)
        self.ui.btn9.pressed.connect(self.btnPressed)
        self.ui.btn10.pressed.connect(self.btnPressed)
        self.ui.btn11.pressed.connect(self.btnPressed)
        self.ui.btn12.pressed.connect(self.btnPressed)
        self.ui.btn13.pressed.connect(self.btnPressed)
        self.ui.btn14.pressed.connect(self.btnPressed)
        self.ui.btn15.pressed.connect(self.btnPressed)
        self.ui.btn16.pressed.connect(self.btnPressed)
        self.ui.btn17.pressed.connect(self.btnPressed)
        self.ui.btn18.pressed.connect(self.btnPressed)
        self.ui.btn19.pressed.connect(self.btnPressed)
        self.ui.btn20.pressed.connect(self.btnPressed)
        self.ui.btn22.pressed.connect(self.btnPressed)
        self.ui.btn23.pressed.connect(self.btnPressed)
        self.ui.btn24.pressed.connect(self.btnPressed)
        self.ui.btn25.pressed.connect(self.btnPressed)
        self.ui.btn26.pressed.connect(self.btnPressed)
        self.ui.btn27.pressed.connect(self.btnPressed)
        self.ui.btn28.pressed.connect(self.btnPressed)
        self.ui.btn31.pressed.connect(self.btnPressed)
        self.ui.btn32.pressed.connect(self.btnPressed)
        self.ui.btn34.pressed.connect(self.btnPressed)

        # Eventos al soltar
        self.ui.btn1.released.connect(self.btnReleased)
        self.ui.btn2.released.connect(self.btnReleased)
        self.ui.btn3.released.connect(self.btnReleased)
        self.ui.btn4.released.connect(self.btnReleased)
        self.ui.btn5.released.connect(self.btnReleased)
        self.ui.btn6.released.connect(self.btnReleased)
        self.ui.btn7.released.connect(self.btnReleased)
        self.ui.btn8.released.connect(self.btnReleased)
        self.ui.btn9.released.connect(self.btnReleased)
        self.ui.btn10.released.connect(self.btnReleased)
        self.ui.btn11.released.connect(self.btnReleased)
        self.ui.btn12.released.connect(self.btnReleased)
        self.ui.btn13.released.connect(self.btnReleased)
        self.ui.btn14.released.connect(self.btnReleased)
        self.ui.btn15.released.connect(self.btnReleased)
        self.ui.btn16.released.connect(self.btnReleased)
        self.ui.btn17.released.connect(self.btnReleased)
        self.ui.btn18.released.connect(self.btnReleased)
        self.ui.btn19.released.connect(self.btnReleased)
        self.ui.btn20.released.connect(self.btnReleased)
        self.ui.btn22.released.connect(self.btnReleased)
        self.ui.btn23.released.connect(self.btnReleased)
        self.ui.btn24.released.connect(self.btnReleased)
        self.ui.btn25.released.connect(self.btnReleased)
        self.ui.btn26.released.connect(self.btnReleased)
        self.ui.btn27.released.connect(self.btnReleased)
        self.ui.btn28.released.connect(self.btnReleased)
        self.ui.btn31.released.connect(self.btnReleased)
        self.ui.btn32.released.connect(self.btnReleased)
        self.ui.btn34.released.connect(self.btnReleased)

        self.ui.btn21.pressed.connect(self.capPressed)  # Capitalize
        self.ui.btn21.released.connect(self.capReleased)  # Capitalize
        self.ui.btn30.pressed.connect(self.numbersCharsPressed)  # Números y caracteres
        self.ui.btn30.released.connect(self.numbersCharsReleased)  # Números y caracteres

        self.ui.btn29.pressed.connect(self.backspacePressed)  # Backspace
        self.ui.btn29.released.connect(self.backspaceReleased)  # Backspace

        self.ui.btn33.setText(" ")
        self.ui.btn33.pressed.connect(self.btnPressedSpace)  # Espacio
        self.ui.btn33.released.connect(self.btnReleasedSpace)  # Espacio


    def changeFocusKeyboard(self, focus):
        self.focusLine = focus
        self.focusLine.setFocus()

    def btnPressed(self):
        button = self.sender()
        buttonText = button.text()
        self.originalSize = button.size()
        self.focusLine.setText(self.focusLine.text() + buttonText)
        button.raise_()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(204, 204, 204); font: 18pt \"Poppins\";")
        button.setAutoFillBackground(False)
        button.resize(99,61) 
        button.move(button.x()-15,button.y()-15)

    def btnReleased(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(255, 255, 255); font: 11pt \"Poppins\";")
        button.resize(self.originalSize) 
        button.move(button.x() + 15,button.y() + 15)
        self.focusLine.setFocus()

    def btnPressedSpace(self):
        button = self.sender()
        buttonText = button.text()
        self.originalSize = button.size()
        self.focusLine.setText(self.focusLine.text() + buttonText)
        button.setStyleSheet("border-radius: 10px; background-color: rgb(155, 155, 155); font: 11pt \"Poppins\";")
        #self.mainBtn.move(330, 10) #Titulo ajustes

    def btnReleasedSpace(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(255, 255, 255); font: 11pt \"Poppins\";")
        self.focusLine.setFocus()  

    def backspacePressed(self):
        self.timerBackSpace.start()
        button = self.sender()
        self.focusLine.setText(self.focusLine.text()[:-1])
        button.setStyleSheet("border-radius: 10px; background-color: rgb(0, 68, 141); font: 12pt \"Poppins\"; color: rgb(255, 255, 255);")

    def backspaceReleased(self):
        self.timerBackSpace.stop()
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(0, 98, 204); font: 12pt \"Poppins\"; color: rgb(255, 255, 255);")
        self.focusLine.setFocus()   

    def backspaceHeld(self):
        self.focusLine.clear()
        self.focusLine.setFocus()    

    def capPressed(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(0, 68, 141); font: 11pt \"Poppins\"; color: rgb(255, 255, 255);")

        if not self.numbersCharsStatus:
            if not self.capStatus:
                self.capStatus = True #atributo booleano para conocer si el boton cap fue presionado
                self.set_mayus()
            
            else:
                self.capStatus = False #atributo booleano para conocer si el boton cap fue presionado
                self.set_minus()

        else:
            if not self.numberCharsStatus_2:
                self.numberCharsStatus_2 = True

                self.ui.btn21.setText("?123")

                self.ui.btn1.setText('~')
                self.ui.btn2.setText("´")
                self.ui.btn3.setText('|')
                self.ui.btn4.setText('•')
                self.ui.btn5.setText('√')
                self.ui.btn6.setText('π')
                self.ui.btn7.setText('÷')
                self.ui.btn8.setText('×')
                self.ui.btn9.setText('¶')
                self.ui.btn10.setText('∆')
                self.ui.btn11.setText('£')
                self.ui.btn12.setText('¢')
                self.ui.btn13.setText('€')
                self.ui.btn14.setText('¥')
                self.ui.btn15.setText('^')
                self.ui.btn16.setText('°')
                self.ui.btn17.setText('=')
                self.ui.btn18.setText('{')
                self.ui.btn19.setText('}')
                self.ui.btn20.setText("\\")

                self.ui.btn22.setText('%')
                self.ui.btn23.setText('©')
                self.ui.btn24.setText("®")
                self.ui.btn25.setText('™')
                self.ui.btn26.setText('✓')
                self.ui.btn27.setText('[')
                self.ui.btn28.setText(']')


            else:
                self.numberCharsStatus_2 = False

                self.ui.btn21.setText("=\\<")

                self.ui.btn1.setText('1')
                self.ui.btn2.setText('2')
                self.ui.btn3.setText('3')
                self.ui.btn4.setText('4')
                self.ui.btn5.setText('5')
                self.ui.btn6.setText('6')
                self.ui.btn7.setText('7')
                self.ui.btn8.setText('8')
                self.ui.btn9.setText('9')
                self.ui.btn10.setText('0')
                self.ui.btn11.setText('@')
                self.ui.btn12.setText('#')
                self.ui.btn13.setText('$')
                self.ui.btn14.setText('_')
                self.ui.btn15.setText('&')
                self.ui.btn16.setText('-')
                self.ui.btn17.setText('+')
                self.ui.btn18.setText('(')
                self.ui.btn19.setText(')')
                self.ui.btn20.setText('/')

                self.ui.btn22.setText('*')
                self.ui.btn23.setText('"')
                self.ui.btn24.setText("'")
                self.ui.btn25.setText(':')
                self.ui.btn26.setText(';')
                self.ui.btn27.setText('!')
                self.ui.btn28.setText('?')


    def capReleased(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(0, 98, 204); font: 11pt \"Poppins\"; color: rgb(255, 255, 255);")
        self.focusLine.setFocus()   

    def numbersCharsPressed(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(0, 68, 141); font: 11pt \"Poppins\"; color: rgb(255, 255, 255);")

        if not self.numbersCharsStatus:
            self.numbersCharsStatus = True #atributo booleano para conocer si el boton cap fue presionado

            self.ui.btn30.setText("ABC")
            self.ui.btn21.setText("=\\<")

            self.ui.btn1.setText('1')
            self.ui.btn2.setText('2')
            self.ui.btn3.setText('3')
            self.ui.btn4.setText('4')
            self.ui.btn5.setText('5')
            self.ui.btn6.setText('6')
            self.ui.btn7.setText('7')
            self.ui.btn8.setText('8')
            self.ui.btn9.setText('9')
            self.ui.btn10.setText('0')
            self.ui.btn11.setText('@')
            self.ui.btn12.setText('#')
            self.ui.btn13.setText('$')
            self.ui.btn14.setText('_')
            self.ui.btn15.setText('&')
            self.ui.btn16.setText('-')
            self.ui.btn17.setText('+')
            self.ui.btn18.setText('(')
            self.ui.btn19.setText(')')
            self.ui.btn20.setText('/')

            self.ui.btn22.setText('*')
            self.ui.btn23.setText('"')
            self.ui.btn24.setText("'")
            self.ui.btn25.setText(':')
            self.ui.btn26.setText(';')
            self.ui.btn27.setText('!')
            self.ui.btn28.setText('?')

        
        else:
            self.numbersCharsStatus = False #Cambia el estado del boton a no presionado
            self.numberCharsStatus_2 = False #Cambia el estado del boton de caracteres extra a no presionado
            self.ui.btn30.setText("?123")
            self.ui.btn21.setText("Mayús")
            #Devuelve las letras dependiendo el estad que tuviera el boton capitalizar
            if not self.capStatus:
                self.set_minus()
            else:
                self.set_mayus()

    def numbersCharsReleased(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(0, 98, 204); font: 11pt \"Poppins\"; color: rgb(255, 255, 255);")
        self.focusLine.setFocus()      

    def set_mayus(self):
        self.ui.btn1.setText('Q')
        self.ui.btn2.setText('W')
        self.ui.btn3.setText('E')
        self.ui.btn4.setText('R')
        self.ui.btn5.setText('T')
        self.ui.btn6.setText('Y')
        self.ui.btn7.setText('U')
        self.ui.btn8.setText('I')
        self.ui.btn9.setText('O')
        self.ui.btn10.setText('P')
        self.ui.btn11.setText('A')
        self.ui.btn12.setText('S')
        self.ui.btn13.setText('D')
        self.ui.btn14.setText('F')
        self.ui.btn15.setText('G')
        self.ui.btn16.setText('H')
        self.ui.btn17.setText('J')
        self.ui.btn18.setText('K')
        self.ui.btn19.setText('L')
        self.ui.btn20.setText('Ñ')

        self.ui.btn22.setText('Z')
        self.ui.btn23.setText('X')
        self.ui.btn24.setText('C')
        self.ui.btn25.setText('V')
        self.ui.btn26.setText('B')
        self.ui.btn27.setText('N')
        self.ui.btn28.setText('M')

    def set_minus(self):
        self.ui.btn1.setText('q')
        self.ui.btn2.setText('w')
        self.ui.btn3.setText('e')
        self.ui.btn4.setText('r')
        self.ui.btn5.setText('t')
        self.ui.btn6.setText('y')
        self.ui.btn7.setText('u')
        self.ui.btn8.setText('i')
        self.ui.btn9.setText('o')
        self.ui.btn10.setText('p')
        self.ui.btn11.setText('a')
        self.ui.btn12.setText('s')
        self.ui.btn13.setText('d')
        self.ui.btn14.setText('f')
        self.ui.btn15.setText('g')
        self.ui.btn16.setText('h')
        self.ui.btn17.setText('j')
        self.ui.btn18.setText('k')
        self.ui.btn19.setText('l')
        self.ui.btn20.setText('ñ')

        self.ui.btn22.setText('z')
        self.ui.btn23.setText('x')
        self.ui.btn24.setText('c')
        self.ui.btn25.setText('v')
        self.ui.btn26.setText('b')
        self.ui.btn27.setText('n')
        self.ui.btn28.setText('m')

