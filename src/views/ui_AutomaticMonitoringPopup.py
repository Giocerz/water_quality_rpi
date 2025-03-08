# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutomaticMonitoringPopupWgNgki.ui'
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
        Form.setStyleSheet(u"QLabel {\n"
"	font-family: Poppins;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-size: 14px;\n"
"	font-family: Poppins;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"")
        self.captureWidget = QWidget(Form)
        self.captureWidget.setObjectName(u"captureWidget")
        self.captureWidget.setGeometry(QRect(0, 210, 481, 62))
        self.captureWidget.setStyleSheet(u"background-color: white;")
        self.stopBtn = QPushButton(self.captureWidget)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setGeometry(QRect(340, 10, 101, 41))
        self.stopBtn.setStyleSheet(u"border-radius: 20px;")
        self.label = QLabel(self.captureWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 111, 41))
        self.countLbl = QLabel(self.captureWidget)
        self.countLbl.setObjectName(u"countLbl")
        self.countLbl.setGeometry(QRect(210, 10, 111, 41))
        self.countLbl.setAlignment(Qt.AlignCenter)
        self.IconInfo = QLabel(self.captureWidget)
        self.IconInfo.setObjectName(u"IconInfo")
        self.IconInfo.setGeometry(QRect(30, 10, 41, 41))
        self.IconInfo.setStyleSheet(u"border: 6px solid #ced4da;\n"
"border-radius:  20px;\n"
"border-top: 5px solid #00007f;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.stopBtn.setText(QCoreApplication.translate("Form", u"Detener", None))
        self.label.setText(QCoreApplication.translate("Form", u"Capturando...", None))
        self.countLbl.setText(QCoreApplication.translate("Form", u"1/50", None))
        self.IconInfo.setText("")
    # retranslateUi

