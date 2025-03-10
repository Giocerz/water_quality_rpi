# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenuDWnRbn.ui'
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
        MainWindow.setStyleSheet(u"background-color: white;\n"
"font-family: Poppins;\n"
"font-size:20px;\n"
"font-weight: 500;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	height: 50px;\n"
"	border-radius: 25px;\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"}")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 0, 421, 281))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(80, 0, 80, 6)
        self.monitoringBtn = QPushButton(self.verticalLayoutWidget)
        self.monitoringBtn.setObjectName(u"monitoringBtn")
        self.monitoringBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.monitoringBtn)

        self.calibrationBtn = QPushButton(self.verticalLayoutWidget)
        self.calibrationBtn.setObjectName(u"calibrationBtn")
        self.calibrationBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.calibrationBtn)

        self.dataBtn = QPushButton(self.verticalLayoutWidget)
        self.dataBtn.setObjectName(u"dataBtn")

        self.verticalLayout.addWidget(self.dataBtn)

        self.bluetoothBtn = QPushButton(self.verticalLayoutWidget)
        self.bluetoothBtn.setObjectName(u"bluetoothBtn")

        self.verticalLayout.addWidget(self.bluetoothBtn)

        self.powerBtn = QPushButton(self.centralwidget)
        self.powerBtn.setObjectName(u"powerBtn")
        self.powerBtn.setGeometry(QRect(420, 212, 50, 50))
        self.powerBtn.setStyleSheet(u"")
        self.wifiBtn = QPushButton(self.centralwidget)
        self.wifiBtn.setObjectName(u"wifiBtn")
        self.wifiBtn.setGeometry(QRect(420, 150, 50, 50))
        self.wifiBtn.setStyleSheet(u"")
        self.helpBtn = QPushButton(self.centralwidget)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setGeometry(QRect(420, 90, 50, 50))
        self.helpBtn.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.monitoringBtn.setText(QCoreApplication.translate("MainWindow", u"Monitoreo", None))
        self.calibrationBtn.setText(QCoreApplication.translate("MainWindow", u"Calibraci\u00f3n", None))
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"Datos", None))
        self.bluetoothBtn.setText(QCoreApplication.translate("MainWindow", u"Bluetooth", None))
        self.powerBtn.setText("")
        self.wifiBtn.setText("")
        self.helpBtn.setText("")
    # retranslateUi

