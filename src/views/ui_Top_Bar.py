# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Top_BarBxqakh.ui'
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
        self.batLblBg = QLabel(Form)
        self.batLblBg.setObjectName(u"batLblBg")
        self.batLblBg.setGeometry(QRect(360, 10, 51, 31))
        self.batLblBg.setStyleSheet(u"background-color: rgb(85, 255, 0);")
        self.batLbl = QLabel(Form)
        self.batLbl.setObjectName(u"batLbl")
        self.batLbl.setGeometry(QRect(410, 10, 61, 31))
        self.batLbl.setStyleSheet(u"text-align: center;\n"
"font-size: 12pt;")
        self.batLblPng = QLabel(Form)
        self.batLblPng.setObjectName(u"batLblPng")
        self.batLblPng.setGeometry(QRect(360, 10, 51, 31))
        self.batLblPng.setStyleSheet(u"background-color: transparent;")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 16, 191, 16))
        self.chargeLbl = QLabel(Form)
        self.chargeLbl.setObjectName(u"chargeLbl")
        self.chargeLbl.setGeometry(QRect(370, 10, 31, 31))
        self.chargeLbl.setStyleSheet(u"background-color: transparent;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.batLblBg.setText("")
        self.batLbl.setText("")
        self.batLblPng.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Citizen Aqua Probe V1.0", None))
        self.chargeLbl.setText("")
    # retranslateUi

