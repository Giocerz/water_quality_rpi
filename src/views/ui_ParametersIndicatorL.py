# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ParametersIndicatorLvnRnSm.ui'
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
        Form.resize(481, 105)
        Form.setStyleSheet(u"QLabel {\n"
"	font-family: Poppins;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: white;\n"
"}")
        self.nameLbl = QLabel(Form)
        self.nameLbl.setObjectName(u"nameLbl")
        self.nameLbl.setGeometry(QRect(10, 10, 291, 21))
        self.nameLbl.setStyleSheet(u"font-size: 18px;")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 80, 461, 16))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 5px;\n"
"    background-color: #f3f3f3;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #00007f;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.valueLbl = QLabel(Form)
        self.valueLbl.setObjectName(u"valueLbl")
        self.valueLbl.setGeometry(QRect(240, 0, 231, 81))
        self.valueLbl.setStyleSheet(u"font-weight: bold;\n"
"font-size: 36px;")
        self.warningLbl = QLabel(Form)
        self.warningLbl.setObjectName(u"warningLbl")
        self.warningLbl.setGeometry(QRect(10, 40, 35, 35))
        self.stableLbl = QLabel(Form)
        self.stableLbl.setObjectName(u"stableLbl")
        self.stableLbl.setGeometry(QRect(50, 40, 35, 35))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nameLbl.setText(QCoreApplication.translate("Form", u"Conductividad Electrica", None))
        self.valueLbl.setText(QCoreApplication.translate("Form", u"1234.2 ppm", None))
        self.warningLbl.setText("")
        self.stableLbl.setText("")
    # retranslateUi

