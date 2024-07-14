# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalibrationZbtIPN.ui'
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
        self.actBtn = QPushButton(self.centralwidget)
        self.actBtn.setObjectName(u"actBtn")
        self.actBtn.setGeometry(QRect(150, 220, 181, 41))
        self.actBtn_2 = QPushButton(self.centralwidget)
        self.actBtn_2.setObjectName(u"actBtn_2")
        self.actBtn_2.setGeometry(QRect(150, 270, 181, 41))
        self.imgLbl = QLabel(self.centralwidget)
        self.imgLbl.setObjectName(u"imgLbl")
        self.imgLbl.setGeometry(QRect(165, 20, 151, 121))
        self.imgLbl.setStyleSheet(u"")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(20, 20, 41, 41))
        self.backBtn.setStyleSheet(u"")
        self.instLbl = QLabel(self.centralwidget)
        self.instLbl.setObjectName(u"instLbl")
        self.instLbl.setGeometry(QRect(94, 160, 291, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actBtn.setText(QCoreApplication.translate("MainWindow", u"Omitir", None))
        self.actBtn_2.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.imgLbl.setText("")
        self.backBtn.setText("")
        self.instLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Instructions</span></p></body></html>", None))
    # retranslateUi

