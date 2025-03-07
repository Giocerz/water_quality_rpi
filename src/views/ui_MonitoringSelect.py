# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MonitoringSelectjwYgdQ.ui'
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
        self.initBtn = QPushButton(self.centralwidget)
        self.initBtn.setObjectName(u"initBtn")
        self.initBtn.setGeometry(QRect(140, 220, 171, 41))
        self.initBtn.setStyleSheet(u"border-radius: 20px;")
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
        self.tdsCheckBox = QCheckBox(self.centralwidget)
        self.tdsCheckBox.setObjectName(u"tdsCheckBox")
        self.tdsCheckBox.setGeometry(QRect(140, 50, 141, 21))
        self.tdsCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.tdsCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 21px;\n"
"	font-family: Poppins;\n"
"	font-size: 14px;\n"
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
        self.phCheckBox = QCheckBox(self.centralwidget)
        self.phCheckBox.setObjectName(u"phCheckBox")
        self.phCheckBox.setGeometry(QRect(140, 80, 141, 21))
        self.phCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.phCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 21px;\n"
"	font-family: Poppins;\n"
"	font-size: 14px;\n"
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
        self.oxygenCheckBox = QCheckBox(self.centralwidget)
        self.oxygenCheckBox.setObjectName(u"oxygenCheckBox")
        self.oxygenCheckBox.setGeometry(QRect(110, 110, 171, 21))
        self.oxygenCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.oxygenCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 21px;\n"
"	font-family: Poppins;\n"
"	font-size: 14px;\n"
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
        self.turbidityCheckBox = QCheckBox(self.centralwidget)
        self.turbidityCheckBox.setObjectName(u"turbidityCheckBox")
        self.turbidityCheckBox.setGeometry(QRect(140, 140, 141, 21))
        self.turbidityCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.turbidityCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 21px;\n"
"	font-family: Poppins;\n"
"	font-size: 14px;\n"
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
        self.allCheckBox = QCheckBox(self.centralwidget)
        self.allCheckBox.setObjectName(u"allCheckBox")
        self.allCheckBox.setGeometry(QRect(140, 170, 141, 21))
        self.allCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.allCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 21px;\n"
"	font-family: Poppins;\n"
"	font-size: 14px;\n"
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.initBtn.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.backBtn.setText("")
        self.tdsCheckBox.setText(QCoreApplication.translate("MainWindow", u"TDS/CE", None))
        self.phCheckBox.setText(QCoreApplication.translate("MainWindow", u"pH", None))
        self.oxygenCheckBox.setText(QCoreApplication.translate("MainWindow", u"Ox\u00edgeno Disuelto", None))
        self.turbidityCheckBox.setText(QCoreApplication.translate("MainWindow", u"Turbidez", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u00bfQue p\u00e1rametros desea monitorear?</p></body></html>", None))
        self.allCheckBox.setText(QCoreApplication.translate("MainWindow", u"Marcar todos", None))
    # retranslateUi

