# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Top_BarFfMPtv.ui'
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
        Form.resize(480, 48)
        Form.setStyleSheet(u"QLabel {\n"
"	font-family: Poppins;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: white;\n"
"}\n"
"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 16, 191, 16))
        self.batteryExtBorder = QLabel(Form)
        self.batteryExtBorder.setObjectName(u"batteryExtBorder")
        self.batteryExtBorder.setGeometry(QRect(380, 11, 60, 26))
        self.batteryExtBorder.setStyleSheet(u"border: 2px solid #00007f;\n"
"border-radius: 12px;\n"
"background-color: transparent;")
        self.baterryLevel = QLabel(Form)
        self.baterryLevel.setObjectName(u"baterryLevel")
        self.baterryLevel.setGeometry(QRect(380, 11, 60, 26))
        self.baterryLevel.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 1, y2: 0,\n"
"    stop:0 rgba(255, 255, 255, 255),\n"
"	stop:0 rgba(255, 255, 255, 255), \n"
"	stop:0 rgba(0, 0, 127, 255), \n"
"	stop:1 rgba(0, 0, 127, 255)\n"
");\n"
"border-radius: 12px;\n"
"\n"
"")
        self.batteryIntBorder = QLabel(Form)
        self.batteryIntBorder.setObjectName(u"batteryIntBorder")
        self.batteryIntBorder.setGeometry(QRect(382, 13, 56, 22))
        self.batteryIntBorder.setStyleSheet(u"border: 2px solid white;\n"
"background-color: transparent;\n"
"border-radius: 10px;")
        self.batteryLbl = QLabel(Form)
        self.batteryLbl.setObjectName(u"batteryLbl")
        self.batteryLbl.setGeometry(QRect(445, 14, 31, 20))
        self.chargeIndicator = QLabel(Form)
        self.chargeIndicator.setObjectName(u"chargeIndicator")
        self.chargeIndicator.setGeometry(QRect(350, 10, 26, 26))
        self.baterryLevel.raise_()
        self.batteryExtBorder.raise_()
        self.label.raise_()
        self.batteryIntBorder.raise_()
        self.batteryLbl.raise_()
        self.chargeIndicator.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Citizen Aqua Probe V1.0", None))
        self.batteryExtBorder.setText("")
        self.baterryLevel.setText("")
        self.batteryIntBorder.setText("")
        self.batteryLbl.setText("")
        self.chargeIndicator.setText("")
    # retranslateUi

