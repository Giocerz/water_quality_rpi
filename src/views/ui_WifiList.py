# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WifiListjQrgbi.ui'
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
"}")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(10, 10, 41, 41))
        self.backBtn.setStyleSheet(u"")
        self.networkList = QListView(self.centralwidget)
        self.networkList.setObjectName(u"networkList")
        self.networkList.setGeometry(QRect(60, 11, 351, 241))
        self.networkList.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 10px;")
        self.networkList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.networkList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(420, 11, 41, 251))
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical{ \n"
"	background-color: rgb(234, 234, 234);\n"
"	height: 251px;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QSlider::handle:vertical { \n"
"	background-color: #00007f;\n"
"    height: 60px;\n"
"    width: 20px;\n"
"    line-height: 10px; \n"
"	margin-top: 0px; \n"
"	margin-bottom: 0px;\n"
"	border-radius: 20px; \n"
"}\n"
"\n"
"QSlider{\n"
"	background-color: rgb(234, 234, 234);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.verticalSlider.setValue(0)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(True)
        self.verticalSlider.setInvertedControls(False)
        self.infoLbl = QLabel(self.centralwidget)
        self.infoLbl.setObjectName(u"infoLbl")
        self.infoLbl.setEnabled(True)
        self.infoLbl.setGeometry(QRect(80, 90, 321, 81))
        self.infoLbl.setStyleSheet(u"color: grey;\n"
"font-size: 18pt;")
        self.refreshBtn = QPushButton(self.centralwidget)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setGeometry(QRect(10, 60, 41, 41))
        self.refreshBtn.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText("")
        self.infoLbl.setText(QCoreApplication.translate("MainWindow", u"No se encontraron redes", None))
        self.refreshBtn.setText("")
    # retranslateUi

