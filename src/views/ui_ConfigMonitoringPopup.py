# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfigMonitoringPopupTUCmEQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 272)
        Form.setStyleSheet(u"font: 14px Poppins;")
        self.lblOpacity = QLabel(Form)
        self.lblOpacity.setObjectName(u"lblOpacity")
        self.lblOpacity.setGeometry(QRect(0, 0, 480, 320))
        self.lblOpacity.setStyleSheet(u"background-color: black;")
        self.Widget1 = QWidget(Form)
        self.Widget1.setObjectName(u"Widget1")
        self.Widget1.setEnabled(True)
        self.Widget1.setGeometry(QRect(50, 10, 381, 221))
        self.Widget1.setStyleSheet(u"border-radius: 20px;\n"
"background-color: white;")
        self.periodLine = QLineEdit(self.Widget1)
        self.periodLine.setObjectName(u"periodLine")
        self.periodLine.setGeometry(QRect(140, 140, 91, 26))
        self.periodLine.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"font: 14px \"Poppins\";\n"
"background-color: rgb(234, 234, 234);")
        self.periodLine.setMaxLength(50)
        self.periodLine.setEchoMode(QLineEdit.Normal)
        self.confirmBtn = QPushButton(self.Widget1)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setGeometry(QRect(250, 130, 101, 41))
        self.confirmBtn.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-size: 14px;\n"
"	font-family: Poppins;\n"
"	font-weight: 500;\n"
"}")
        self.closeBtn = QPushButton(self.Widget1)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(10, 10, 41, 41))
        self.closeBtn.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-size: 14px;\n"
"	font-family: Poppins;\n"
"	font-weight: 500;\n"
"}")
        self.captureCheckBox = QCheckBox(self.Widget1)
        self.captureCheckBox.setObjectName(u"captureCheckBox")
        self.captureCheckBox.setGeometry(QRect(40, 95, 271, 31))
        self.captureCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 14px \"Poppins\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #00007f; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.totalSamplesLine = QLineEdit(self.Widget1)
        self.totalSamplesLine.setObjectName(u"totalSamplesLine")
        self.totalSamplesLine.setGeometry(QRect(210, 60, 141, 26))
        self.totalSamplesLine.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"font: 14px \"Poppins\";\n"
"background-color: rgb(234, 234, 234);")
        self.totalSamplesLine.setMaxLength(50)
        self.totalSamplesLine.setEchoMode(QLineEdit.Normal)
        self.label = QLabel(self.Widget1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 171, 16))
        self.label_3 = QLabel(self.Widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 65, 161, 16))
        self.label_4 = QLabel(self.Widget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 145, 91, 16))
        self.periodLine.raise_()
        self.closeBtn.raise_()
        self.captureCheckBox.raise_()
        self.totalSamplesLine.raise_()
        self.confirmBtn.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.widgetKeyboard = QWidget(Form)
        self.widgetKeyboard.setObjectName(u"widgetKeyboard")
        self.widgetKeyboard.setGeometry(QRect(0, 202, 480, 70))
        self.widgetKeyboard.setStyleSheet(u"background-color: rgb(234, 234, 234);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblOpacity.setText("")
        self.periodLine.setPlaceholderText("")
        self.confirmBtn.setText(QCoreApplication.translate("Form", u"Confirmar", None))
        self.closeBtn.setText(QCoreApplication.translate("Form", u"X", None))
        self.captureCheckBox.setText(QCoreApplication.translate("Form", u"Activar captura autom\u00e1tica", None))
        self.totalSamplesLine.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("Form", u"Opciones de captura", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"N\u00famero de muestras", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Per\u00edodo (s):", None))
    # retranslateUi

