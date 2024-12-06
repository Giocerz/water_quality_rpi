# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalibrationfrkCgp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Calibration(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setStyleSheet(u"font-family: Poppins;\n"
"background-color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	height: 40px;\n"
"	border-radius: 20px;\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-weight: 500;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QLabel {\n"
"		text-align: center;\n"
"	}")
        self.skipBtn = QPushButton(self.centralwidget)
        self.skipBtn.setObjectName(u"skipBtn")
        self.skipBtn.setGeometry(QRect(150, 220, 181, 41))
        self.nextBtn = QPushButton(self.centralwidget)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setGeometry(QRect(150, 270, 181, 41))
        self.imgLbl = QLabel(self.centralwidget)
        self.imgLbl.setObjectName(u"imgLbl")
        self.imgLbl.setGeometry(QRect(180, 10, 121, 121))
        self.imgLbl.setStyleSheet(u"")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(20, 20, 41, 41))
        self.backBtn.setStyleSheet(u"")
        self.instLbl = QLabel(self.centralwidget)
        self.instLbl.setObjectName(u"instLbl")
        self.instLbl.setGeometry(QRect(14, 140, 451, 71))
        self.instLbl.setStyleSheet(u"font-size: 12pt;")
        self.loadingBar = QProgressBar(self.centralwidget)
        self.loadingBar.setObjectName(u"loadingBar")
        self.loadingBar.setGeometry(QRect(0, 270, 481, 31))
        self.loadingBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 5px;\n"
"    background-color: #f3f3f3;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #00007f;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.loadingBar.setValue(0)
        self.loadingBar.setTextVisible(False)
        self.showVoltLbl = QLabel(self.centralwidget)
        self.showVoltLbl.setObjectName(u"showVoltLbl")
        self.showVoltLbl.setGeometry(QRect(60, 211, 361, 51))
        self.showVoltLbl.setStyleSheet(u"font-size: 18pt;\n"
"color: rgb(213, 213, 213);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.skipBtn.setText(QCoreApplication.translate("MainWindow", u"Omitir", None))
        self.nextBtn.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.imgLbl.setText("")
        self.backBtn.setText("")
        self.instLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.showVoltLbl.setText("")
    # retranslateUi

