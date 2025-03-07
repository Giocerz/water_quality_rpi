# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManualGPSkSpWTX.ui'
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
        self.lblOpacity = QLabel(Form)
        self.lblOpacity.setObjectName(u"lblOpacity")
        self.lblOpacity.setGeometry(QRect(0, 0, 480, 320))
        self.lblOpacity.setStyleSheet(u"background-color: black;")
        self.Widget1 = QWidget(Form)
        self.Widget1.setObjectName(u"Widget1")
        self.Widget1.setEnabled(True)
        self.Widget1.setGeometry(QRect(15, 10, 451, 201))
        self.Widget1.setStyleSheet(u"border-radius: 20px;\n"
"background-color: white;")
        self.lbl = QLabel(self.Widget1)
        self.lbl.setObjectName(u"lbl")
        self.lbl.setGeometry(QRect(220, 10, 191, 31))
        self.lbl.setStyleSheet(u"font: 16px \"Poppins\";\n"
"background-color: transparent;\n"
"")
        self.latitudInput = QLineEdit(self.Widget1)
        self.latitudInput.setObjectName(u"latitudInput")
        self.latitudInput.setGeometry(QRect(220, 50, 201, 26))
        self.latitudInput.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"font: 16px \"Poppins\";\n"
"background-color: rgb(234, 234, 234);")
        self.latitudInput.setMaxLength(50)
        self.latitudInput.setEchoMode(QLineEdit.Password)
        self.longitudeInput = QLineEdit(self.Widget1)
        self.longitudeInput.setObjectName(u"longitudeInput")
        self.longitudeInput.setGeometry(QRect(220, 90, 201, 26))
        self.longitudeInput.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"font: 16px \"Poppins\";\n"
"background-color: rgb(234, 234, 234);")
        self.longitudeInput.setMaxLength(50)
        self.longitudeInput.setEchoMode(QLineEdit.Password)
        self.lbl_2 = QLabel(self.Widget1)
        self.lbl_2.setObjectName(u"lbl_2")
        self.lbl_2.setGeometry(QRect(60, 10, 131, 31))
        self.lbl_2.setStyleSheet(u"font: 16px \"Poppins\";\n"
"background-color: transparent;\n"
"")
        self.initBtn = QPushButton(self.Widget1)
        self.initBtn.setObjectName(u"initBtn")
        self.initBtn.setGeometry(QRect(260, 130, 131, 41))
        self.initBtn.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-size: 14px;\n"
"	font-family: Poppins;\n"
"	font-weight: 500;\n"
"}")
        self.QRLbl = QLabel(self.Widget1)
        self.QRLbl.setObjectName(u"QRLbl")
        self.QRLbl.setGeometry(QRect(60, 50, 131, 131))
        self.QRLbl.setStyleSheet(u"")
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
        self.lbl.setText(QCoreApplication.translate("Form", u"Ingrese la ubicaci\u00f3n", None))
        self.latitudInput.setPlaceholderText(QCoreApplication.translate("Form", u"Latitud", None))
        self.longitudeInput.setPlaceholderText(QCoreApplication.translate("Form", u"Longitud", None))
        self.lbl_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt;\">Escanea el QR</span></p></body></html>", None))
        self.initBtn.setText(QCoreApplication.translate("Form", u"Confirmar", None))
        self.QRLbl.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
        self.closeBtn.setText(QCoreApplication.translate("Form", u"X", None))
    # retranslateUi

