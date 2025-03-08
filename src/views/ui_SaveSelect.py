# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SaveSelectTfnLuB.ui'
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
"QLabel {\n"
"	text-align: center;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.continueBtn = QPushButton(self.centralwidget)
        self.continueBtn.setObjectName(u"continueBtn")
        self.continueBtn.setGeometry(QRect(140, 220, 171, 41))
        self.continueBtn.setStyleSheet(u"border-radius: 20px;")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(5, 5, 41, 41))
        self.backBtn.setStyleSheet(u"	height: 40px;\n"
"	border-radius: 20px;\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-weight: 500;\n"
"	font-size: 16px;")
        self.allCheckBox = QCheckBox(self.centralwidget)
        self.allCheckBox.setObjectName(u"allCheckBox")
        self.allCheckBox.setGeometry(QRect(110, 70, 211, 21))
        self.allCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.allCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 21px;\n"
"	font-family: Poppins;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px; /* Ancho del indicador */\n"
"    height: 15px; /* Alto del indicador */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #00007f; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.meanCheckBox = QCheckBox(self.centralwidget)
        self.meanCheckBox.setObjectName(u"meanCheckBox")
        self.meanCheckBox.setGeometry(QRect(110, 130, 211, 21))
        self.meanCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.meanCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 21px;\n"
"	font-family: Poppins;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px; /* Ancho del indicador */\n"
"    height: 15px; /* Alto del indicador */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #00007f; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 10, 301, 31))
        self.allLbl = QLabel(self.centralwidget)
        self.allLbl.setObjectName(u"allLbl")
        self.allLbl.setGeometry(QRect(100, 90, 211, 31))
        self.allLbl.setStyleSheet(u"font-size: 14px;")
        self.meanLbl = QLabel(self.centralwidget)
        self.meanLbl.setObjectName(u"meanLbl")
        self.meanLbl.setGeometry(QRect(20, 150, 451, 41))
        self.meanLbl.setStyleSheet(u"font-size: 14px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.continueBtn.setText(QCoreApplication.translate("MainWindow", u"Continuar", None))
        self.backBtn.setText("")
        self.allCheckBox.setText(QCoreApplication.translate("MainWindow", u"Todas las muestras", None))
        self.meanCheckBox.setText(QCoreApplication.translate("MainWindow", u"Promedio", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u00bfComo desea guardar las muestras?</p></body></html>", None))
        self.allLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Total de muestras: </p></body></html>", None))
        self.meanLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Temp: 123.22, OD: 23.2, pH: 7.2, Turb: 22.2</p></body></html>", None))
    # retranslateUi

