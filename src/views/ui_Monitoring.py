# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MonitoringqdLqNG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 272)
        MainWindow.setStyleSheet(u"QLabel {\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pauseBtn = QPushButton(self.centralwidget)
        self.pauseBtn.setObjectName(u"pauseBtn")
        self.pauseBtn.setGeometry(QRect(129, 222, 101, 41))
        self.pauseBtn.setStyleSheet(u"border-radius: 20px;")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(17, 222, 41, 41))
        self.backBtn.setStyleSheet(u"	height: 40px;\n"
"	border-radius: 20px;\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-weight: 500;\n"
"	font-size: 16px;")
        self.captureBtn = QPushButton(self.centralwidget)
        self.captureBtn.setObjectName(u"captureBtn")
        self.captureBtn.setGeometry(QRect(245, 222, 101, 41))
        self.captureBtn.setStyleSheet(u"border-radius: 20px;")
        self.captureCountLbl = QLabel(self.centralwidget)
        self.captureCountLbl.setObjectName(u"captureCountLbl")
        self.captureCountLbl.setGeometry(QRect(330, 210, 37, 37))
        self.captureCountLbl.setStyleSheet(u"background-color: #e63946;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"color: white;\n"
"border-radius: 18px;\n"
"")
        self.indicatorsWidget = QWidget(self.centralwidget)
        self.indicatorsWidget.setObjectName(u"indicatorsWidget")
        self.indicatorsWidget.setGeometry(QRect(0, 0, 481, 211))
        self.optionsBtn = QPushButton(self.centralwidget)
        self.optionsBtn.setObjectName(u"optionsBtn")
        self.optionsBtn.setGeometry(QRect(73, 222, 41, 41))
        self.optionsBtn.setStyleSheet(u"	height: 40px;\n"
"	border-radius: 20px;\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-weight: 500;\n"
"	font-size: 16px;")
        self.saveBtn = QPushButton(self.centralwidget)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(363, 222, 101, 41))
        self.saveBtn.setStyleSheet(u"border-radius: 20px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.indicatorsWidget.raise_()
        self.pauseBtn.raise_()
        self.backBtn.raise_()
        self.captureBtn.raise_()
        self.captureCountLbl.raise_()
        self.optionsBtn.raise_()
        self.saveBtn.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pauseBtn.setText(QCoreApplication.translate("MainWindow", u"Pausar", None))
        self.backBtn.setText("")
        self.captureBtn.setText(QCoreApplication.translate("MainWindow", u"Capturar", None))
        self.captureCountLbl.setText(QCoreApplication.translate("MainWindow", u"+30", None))
        self.optionsBtn.setText("")
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
    # retranslateUi

