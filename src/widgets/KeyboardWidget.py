from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QTimer
from src.views.ui_Keyboard import Ui_Form as Standard_Keyboard
from src.views.ui_NumericKeyboard import Ui_Form as Numeric_Keyboard

class KeyboardWidget(QWidget):
    def __init__(self, focusLine):
        QWidget.__init__(self)
        self.__ui = Standard_Keyboard()
        self.__ui.setupUi(self)
        self.__focusLine = focusLine 
        self.__focusLine.setFocus() 

        self.__capStatus = False 
        self.__numbersCharsStatus = False 
        self.__numberCharsStatus_2 = False 

        self.__timerBackSpace = QTimer(self)
        self.__timerBackSpace.setInterval(1000)
        self.__timerBackSpace.setSingleShot(True)
        self.__timerBackSpace.timeout.connect(self.__backspaceHeld)

        self.__set_minus()

        #Eventos al presionar
        self.__ui.btn1.pressed.connect(self.__btnPressed)
        self.__ui.btn2.pressed.connect(self.__btnPressed)
        self.__ui.btn3.pressed.connect(self.__btnPressed)
        self.__ui.btn4.pressed.connect(self.__btnPressed)
        self.__ui.btn5.pressed.connect(self.__btnPressed)
        self.__ui.btn6.pressed.connect(self.__btnPressed)
        self.__ui.btn7.pressed.connect(self.__btnPressed)
        self.__ui.btn8.pressed.connect(self.__btnPressed)
        self.__ui.btn9.pressed.connect(self.__btnPressed)
        self.__ui.btn10.pressed.connect(self.__btnPressed)
        self.__ui.btn11.pressed.connect(self.__btnPressed)
        self.__ui.btn12.pressed.connect(self.__btnPressed)
        self.__ui.btn13.pressed.connect(self.__btnPressed)
        self.__ui.btn14.pressed.connect(self.__btnPressed)
        self.__ui.btn15.pressed.connect(self.__btnPressed)
        self.__ui.btn16.pressed.connect(self.__btnPressed)
        self.__ui.btn17.pressed.connect(self.__btnPressed)
        self.__ui.btn18.pressed.connect(self.__btnPressed)
        self.__ui.btn19.pressed.connect(self.__btnPressed)
        self.__ui.btn20.pressed.connect(self.__btnPressed)
        self.__ui.btn22.pressed.connect(self.__btnPressed)
        self.__ui.btn23.pressed.connect(self.__btnPressed)
        self.__ui.btn24.pressed.connect(self.__btnPressed)
        self.__ui.btn25.pressed.connect(self.__btnPressed)
        self.__ui.btn26.pressed.connect(self.__btnPressed)
        self.__ui.btn27.pressed.connect(self.__btnPressed)
        self.__ui.btn28.pressed.connect(self.__btnPressed)
        self.__ui.btn31.pressed.connect(self.__btnPressed)
        self.__ui.btn32.pressed.connect(self.__btnPressed)
        self.__ui.btn34.pressed.connect(self.__btnPressed)

        # Eventos al soltar
        self.__ui.btn1.released.connect(self.__btnReleased)
        self.__ui.btn2.released.connect(self.__btnReleased)
        self.__ui.btn3.released.connect(self.__btnReleased)
        self.__ui.btn4.released.connect(self.__btnReleased)
        self.__ui.btn5.released.connect(self.__btnReleased)
        self.__ui.btn6.released.connect(self.__btnReleased)
        self.__ui.btn7.released.connect(self.__btnReleased)
        self.__ui.btn8.released.connect(self.__btnReleased)
        self.__ui.btn9.released.connect(self.__btnReleased)
        self.__ui.btn10.released.connect(self.__btnReleased)
        self.__ui.btn11.released.connect(self.__btnReleased)
        self.__ui.btn12.released.connect(self.__btnReleased)
        self.__ui.btn13.released.connect(self.__btnReleased)
        self.__ui.btn14.released.connect(self.__btnReleased)
        self.__ui.btn15.released.connect(self.__btnReleased)
        self.__ui.btn16.released.connect(self.__btnReleased)
        self.__ui.btn17.released.connect(self.__btnReleased)
        self.__ui.btn18.released.connect(self.__btnReleased)
        self.__ui.btn19.released.connect(self.__btnReleased)
        self.__ui.btn20.released.connect(self.__btnReleased)
        self.__ui.btn22.released.connect(self.__btnReleased)
        self.__ui.btn23.released.connect(self.__btnReleased)
        self.__ui.btn24.released.connect(self.__btnReleased)
        self.__ui.btn25.released.connect(self.__btnReleased)
        self.__ui.btn26.released.connect(self.__btnReleased)
        self.__ui.btn27.released.connect(self.__btnReleased)
        self.__ui.btn28.released.connect(self.__btnReleased)
        self.__ui.btn31.released.connect(self.__btnReleased)
        self.__ui.btn32.released.connect(self.__btnReleased)
        self.__ui.btn34.released.connect(self.__btnReleased)

        self.__ui.btn21.pressed.connect(self.__capPressed)  # Capitalize
        self.__ui.btn21.released.connect(self.__capReleased)  # Capitalize
        self.__ui.btn30.pressed.connect(self.__numbersCharsPressed)  # Números y caracteres
        self.__ui.btn30.released.connect(self.__numbersCharsReleased)  # Números y caracteres

        self.__ui.btn29.pressed.connect(self.__backspacePressed)  # Backspace
        self.__ui.btn29.released.connect(self.__backspaceReleased)  # Backspace

        self.__ui.btn33.setText(" ")
        self.__ui.btn33.pressed.connect(self.__btnPressedSpace)  # Espacio
        self.__ui.btn33.released.connect(self.__btnReleasedSpace)  # Espacio


    def changeFocusKeyboard(self, focus):
        self.__focusLine = focus
        self.__focusLine.setFocus()

    def __btnPressed(self):
        button = self.sender()
        buttonText = button.text()
        self.originalSize = button.size()
        self.__focusLine.setText(self.__focusLine.text() + buttonText)
        button.raise_()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(204, 204, 204); font: 18pt \"Poppins\";")
        button.setAutoFillBackground(False)
        button.resize(99,61) 
        button.move(button.x()-15,button.y()-15)

    def __btnReleased(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(255, 255, 255); font: 11pt \"Poppins\";")
        button.resize(self.originalSize) 
        button.move(button.x() + 15,button.y() + 15)
        self.__focusLine.setFocus()

    def __btnPressedSpace(self):
        button = self.sender()
        buttonText = button.text()
        self.originalSize = button.size()
        self.__focusLine.setText(self.__focusLine.text() + buttonText)
        button.setStyleSheet("border-radius: 10px; background-color: rgb(155, 155, 155); font: 11pt \"Poppins\";")
        #self.mainBtn.move(330, 10) #Titulo ajustes

    def __btnReleasedSpace(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(255, 255, 255); font: 11pt \"Poppins\";")
        self.__focusLine.setFocus()  

    def __backspacePressed(self):
        self.__timerBackSpace.start()
        button = self.sender()
        self.__focusLine.setText(self.__focusLine.text()[:-1])
        button.setStyleSheet("border-radius: 10px; background-color: rgb(0, 68, 141); font: 12pt \"Poppins\"; color: rgb(255, 255, 255);")

    def __backspaceReleased(self):
        self.__timerBackSpace.stop()
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: #00007F; font: 12pt \"Poppins\"; color: rgb(255, 255, 255);")
        self.__focusLine.setFocus()   

    def __backspaceHeld(self):
        self.__focusLine.clear()
        self.__focusLine.setFocus()    

    def __capPressed(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(0, 68, 141); font: 11pt \"Poppins\"; color: rgb(255, 255, 255);")

        if not self.__numbersCharsStatus:
            if not self.__capStatus:
                self.__capStatus = True #atributo booleano para conocer si el boton cap fue presionado
                self.__set_mayus()
            
            else:
                self.__capStatus = False #atributo booleano para conocer si el boton cap fue presionado
                self.__set_minus()

        else:
            if not self.__numberCharsStatus_2:
                self.__numberCharsStatus_2 = True

                self.__ui.btn21.setText("?123")

                self.__ui.btn1.setText('~')
                self.__ui.btn2.setText("´")
                self.__ui.btn3.setText('|')
                self.__ui.btn4.setText('•')
                self.__ui.btn5.setText('√')
                self.__ui.btn6.setText('π')
                self.__ui.btn7.setText('÷')
                self.__ui.btn8.setText('×')
                self.__ui.btn9.setText('¶')
                self.__ui.btn10.setText('∆')
                self.__ui.btn11.setText('£')
                self.__ui.btn12.setText('¢')
                self.__ui.btn13.setText('€')
                self.__ui.btn14.setText('¥')
                self.__ui.btn15.setText('^')
                self.__ui.btn16.setText('°')
                self.__ui.btn17.setText('=')
                self.__ui.btn18.setText('{')
                self.__ui.btn19.setText('}')
                self.__ui.btn20.setText("\\")

                self.__ui.btn22.setText('%')
                self.__ui.btn23.setText('©')
                self.__ui.btn24.setText("®")
                self.__ui.btn25.setText('™')
                self.__ui.btn26.setText('✓')
                self.__ui.btn27.setText('[')
                self.__ui.btn28.setText(']')


            else:
                self.__numberCharsStatus_2 = False

                self.__ui.btn21.setText("=\\<")

                self.__ui.btn1.setText('1')
                self.__ui.btn2.setText('2')
                self.__ui.btn3.setText('3')
                self.__ui.btn4.setText('4')
                self.__ui.btn5.setText('5')
                self.__ui.btn6.setText('6')
                self.__ui.btn7.setText('7')
                self.__ui.btn8.setText('8')
                self.__ui.btn9.setText('9')
                self.__ui.btn10.setText('0')
                self.__ui.btn11.setText('@')
                self.__ui.btn12.setText('#')
                self.__ui.btn13.setText('$')
                self.__ui.btn14.setText('_')
                self.__ui.btn15.setText('&')
                self.__ui.btn16.setText('-')
                self.__ui.btn17.setText('+')
                self.__ui.btn18.setText('(')
                self.__ui.btn19.setText(')')
                self.__ui.btn20.setText('/')

                self.__ui.btn22.setText('*')
                self.__ui.btn23.setText('"')
                self.__ui.btn24.setText("'")
                self.__ui.btn25.setText(':')
                self.__ui.btn26.setText(';')
                self.__ui.btn27.setText('!')
                self.__ui.btn28.setText('?')


    def __capReleased(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: #00007F; font: 11pt \"Poppins\"; color: rgb(255, 255, 255);")
        self.__focusLine.setFocus()   

    def __numbersCharsPressed(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(0, 68, 141); font: 11pt \"Poppins\"; color: rgb(255, 255, 255);")

        if not self.__numbersCharsStatus:
            self.__numbersCharsStatus = True #atributo booleano para conocer si el boton cap fue presionado

            self.__ui.btn30.setText("ABC")
            self.__ui.btn21.setText("=\\<")

            self.__ui.btn1.setText('1')
            self.__ui.btn2.setText('2')
            self.__ui.btn3.setText('3')
            self.__ui.btn4.setText('4')
            self.__ui.btn5.setText('5')
            self.__ui.btn6.setText('6')
            self.__ui.btn7.setText('7')
            self.__ui.btn8.setText('8')
            self.__ui.btn9.setText('9')
            self.__ui.btn10.setText('0')
            self.__ui.btn11.setText('@')
            self.__ui.btn12.setText('#')
            self.__ui.btn13.setText('$')
            self.__ui.btn14.setText('_')
            self.__ui.btn15.setText('&')
            self.__ui.btn16.setText('-')
            self.__ui.btn17.setText('+')
            self.__ui.btn18.setText('(')
            self.__ui.btn19.setText(')')
            self.__ui.btn20.setText('/')

            self.__ui.btn22.setText('*')
            self.__ui.btn23.setText('"')
            self.__ui.btn24.setText("'")
            self.__ui.btn25.setText(':')
            self.__ui.btn26.setText(';')
            self.__ui.btn27.setText('!')
            self.__ui.btn28.setText('?')

        
        else:
            self.__numbersCharsStatus = False #Cambia el estado del boton a no presionado
            self.__numberCharsStatus_2 = False #Cambia el estado del boton de caracteres extra a no presionado
            self.__ui.btn30.setText("?123")
            self.__ui.btn21.setText("Mayús")
            #Devuelve las letras dependiendo el estad que tuviera el boton capitalizar
            if not self.__capStatus:
                self.__set_minus()
            else:
                self.__set_mayus()

    def __numbersCharsReleased(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: #00007F; font: 11pt \"Poppins\"; color: rgb(255, 255, 255);")
        self.__focusLine.setFocus()      

    def __set_mayus(self):
        self.__ui.btn1.setText('Q')
        self.__ui.btn2.setText('W')
        self.__ui.btn3.setText('E')
        self.__ui.btn4.setText('R')
        self.__ui.btn5.setText('T')
        self.__ui.btn6.setText('Y')
        self.__ui.btn7.setText('U')
        self.__ui.btn8.setText('I')
        self.__ui.btn9.setText('O')
        self.__ui.btn10.setText('P')
        self.__ui.btn11.setText('A')
        self.__ui.btn12.setText('S')
        self.__ui.btn13.setText('D')
        self.__ui.btn14.setText('F')
        self.__ui.btn15.setText('G')
        self.__ui.btn16.setText('H')
        self.__ui.btn17.setText('J')
        self.__ui.btn18.setText('K')
        self.__ui.btn19.setText('L')
        self.__ui.btn20.setText('Ñ')

        self.__ui.btn22.setText('Z')
        self.__ui.btn23.setText('X')
        self.__ui.btn24.setText('C')
        self.__ui.btn25.setText('V')
        self.__ui.btn26.setText('B')
        self.__ui.btn27.setText('N')
        self.__ui.btn28.setText('M')

    def __set_minus(self):
        self.__ui.btn1.setText('q')
        self.__ui.btn2.setText('w')
        self.__ui.btn3.setText('e')
        self.__ui.btn4.setText('r')
        self.__ui.btn5.setText('t')
        self.__ui.btn6.setText('y')
        self.__ui.btn7.setText('u')
        self.__ui.btn8.setText('i')
        self.__ui.btn9.setText('o')
        self.__ui.btn10.setText('p')
        self.__ui.btn11.setText('a')
        self.__ui.btn12.setText('s')
        self.__ui.btn13.setText('d')
        self.__ui.btn14.setText('f')
        self.__ui.btn15.setText('g')
        self.__ui.btn16.setText('h')
        self.__ui.btn17.setText('j')
        self.__ui.btn18.setText('k')
        self.__ui.btn19.setText('l')
        self.__ui.btn20.setText('ñ')

        self.__ui.btn22.setText('z')
        self.__ui.btn23.setText('x')
        self.__ui.btn24.setText('c')
        self.__ui.btn25.setText('v')
        self.__ui.btn26.setText('b')
        self.__ui.btn27.setText('n')
        self.__ui.btn28.setText('m')


class NumericKeyboardWidget(QWidget):
    def __init__(self, focusLine, natural_numbers:bool = False):
        QWidget.__init__(self)
        self.__ui = Numeric_Keyboard()
        self.__ui.setupUi(self)
        self.__focusLine = focusLine 
        self.__focusLine.setFocus() 
        self.__natural_numbers:bool = natural_numbers
        self.__init_ui_components()

        self.__timerBackSpace = QTimer(self)
        self.__timerBackSpace.setInterval(1000)
        self.__timerBackSpace.setSingleShot(True)
        self.__timerBackSpace.timeout.connect(self.__backspaceHeld)

        #Eventos al presionar
        self.__ui.btn1.pressed.connect(self.__btnPressed)
        self.__ui.btn2.pressed.connect(self.__btnPressed)
        self.__ui.btn3.pressed.connect(self.__btnPressed)
        self.__ui.btn4.pressed.connect(self.__btnPressed)
        self.__ui.btn5.pressed.connect(self.__btnPressed)
        self.__ui.btn6.pressed.connect(self.__btnPressed)
        self.__ui.btn7.pressed.connect(self.__btnPressed)
        self.__ui.btn8.pressed.connect(self.__btnPressed)
        self.__ui.btn9.pressed.connect(self.__btnPressed)
        self.__ui.btn10.pressed.connect(self.__btnPressed)
        self.__ui.btn11.pressed.connect(self.__btnPressed)
        self.__ui.btn12.pressed.connect(self.__btnPressed)

        # Eventos al soltar
        self.__ui.btn1.released.connect(self.__btnReleased)
        self.__ui.btn2.released.connect(self.__btnReleased)
        self.__ui.btn3.released.connect(self.__btnReleased)
        self.__ui.btn4.released.connect(self.__btnReleased)
        self.__ui.btn5.released.connect(self.__btnReleased)
        self.__ui.btn6.released.connect(self.__btnReleased)
        self.__ui.btn7.released.connect(self.__btnReleased)
        self.__ui.btn8.released.connect(self.__btnReleased)
        self.__ui.btn9.released.connect(self.__btnReleased)
        self.__ui.btn10.released.connect(self.__btnReleased)
        self.__ui.btn11.released.connect(self.__btnReleased)
        self.__ui.btn12.released.connect(self.__btnReleased)


        self.__ui.btn13.pressed.connect(self.__backspacePressed)  # Backspace
        self.__ui.btn13.released.connect(self.__backspaceReleased)  # Backspace

    def __init_ui_components(self):
        if self.__natural_numbers:
            self.__ui.btn11.hide()
            self.__ui.btn12.hide()

    def changeFocusKeyboard(self, focus):
        self.__focusLine = focus
        self.__focusLine.setFocus()

    def __btnPressed(self):
        button = self.sender()
        buttonText = button.text()
        self.originalSize = button.size()
        self.__focusLine.setText(self.__focusLine.text() + buttonText)
        button.raise_()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(204, 204, 204); font: 18pt \"Poppins\";")
        button.setAutoFillBackground(False)
        button.resize(99,61) 
        button.move(button.x()-15,button.y()-15)

    def __btnReleased(self):
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: rgb(255, 255, 255); font: 11pt \"Poppins\";")
        button.resize(self.originalSize) 
        button.move(button.x() + 15,button.y() + 15)
        self.__focusLine.setFocus()

    def __backspacePressed(self):
        self.__timerBackSpace.start()
        button = self.sender()
        self.__focusLine.setText(self.__focusLine.text()[:-1])
        button.setStyleSheet("border-radius: 10px; background-color: rgb(0, 68, 141); font: 12pt \"Poppins\"; color: rgb(255, 255, 255);")

    def __backspaceReleased(self):
        self.__timerBackSpace.stop()
        button = self.sender()
        button.setStyleSheet("border-radius: 10px; background-color: #00007F; font: 12pt \"Poppins\"; color: rgb(255, 255, 255);")
        self.__focusLine.setFocus()   

    def __backspaceHeld(self):
        self.__focusLine.clear()
        self.__focusLine.setFocus()