# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Bluetooth_ConnectedFkGesQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Bluetooth(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setStyleSheet(u"background-color: white;\n"
"font-family: Poppins;\n"
"font-size:18px;\n"
"font-weight: 500;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	height: 40px;\n"
"	border-radius: 20px;\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #00007f;\n"
"}\n"
"")
        self.deactBtn = QPushButton(self.centralwidget)
        self.deactBtn.setObjectName(u"deactBtn")
        self.deactBtn.setGeometry(QRect(130, 160, 221, 42))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(145, 110, 191, 31))
        self.label.setStyleSheet(u"text-align: center;")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(20, 20, 41, 41))
        self.backBtn.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.deactBtn.setText(QCoreApplication.translate("MainWindow", u"Activar Bluetooth", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">WATER_QUALITY_BT</p></body></html>", None))
        self.backBtn.setText("")
    # retranslateUi

