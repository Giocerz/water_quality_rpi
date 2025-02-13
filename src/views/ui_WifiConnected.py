# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WifiConnectedBvZgCx.ui'
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
        self.Widget2 = QWidget(Form)
        self.Widget2.setObjectName(u"Widget2")
        self.Widget2.setEnabled(True)
        self.Widget2.setGeometry(QRect(65, 51, 351, 171))
        self.Widget2.setStyleSheet(u"border-radius: 20px;\n"
"background-color: white;")
        self.forgetBtn = QPushButton(self.Widget2)
        self.forgetBtn.setObjectName(u"forgetBtn")
        self.forgetBtn.setGeometry(QRect(200, 90, 122, 31))
        self.forgetBtn.setStyleSheet(u"font: 500 18px \"Poppins\";\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"background-color: white;\n"
"color: #00007f;")
        self.ssidLbl = QLabel(self.Widget2)
        self.ssidLbl.setObjectName(u"ssidLbl")
        self.ssidLbl.setGeometry(QRect(30, 10, 301, 31))
        self.ssidLbl.setStyleSheet(u"font: 16px \"Poppins\";\n"
"background-color: transparent;\n"
"")
        self.disconnectBtn = QPushButton(self.Widget2)
        self.disconnectBtn.setObjectName(u"disconnectBtn")
        self.disconnectBtn.setGeometry(QRect(20, 90, 141, 31))
        self.disconnectBtn.setStyleSheet(u"font: 500 18px \"Poppins\";\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"background-color: white;\n"
"color: #00007f;")
        self.connectBtn = QPushButton(self.Widget2)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setGeometry(QRect(20, 90, 141, 31))
        self.connectBtn.setStyleSheet(u"font: 500 18px \"Poppins\";\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"background-color: white;\n"
"color: #00007f;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblOpacity.setText("")
        self.forgetBtn.setText(QCoreApplication.translate("Form", u"Olvidar", None))
        self.ssidLbl.setText(QCoreApplication.translate("Form", u"titulo", None))
        self.disconnectBtn.setText(QCoreApplication.translate("Form", u"Desconectar", None))
        self.connectBtn.setText(QCoreApplication.translate("Form", u"Conectar", None))
    # retranslateUi

