# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainVJhbKA.ui'
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
        MainWindow.resize(480, 320)
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
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 481, 321))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(140, 0, 140, 0)
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
    # retranslateUi

