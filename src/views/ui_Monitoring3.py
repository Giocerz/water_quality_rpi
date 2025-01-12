# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Monitoring3OfMNsD.ui'
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
"	font-size: 12pt;\n"
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
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 481, 221))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.odLbl = QLabel(self.gridLayoutWidget)
        self.odLbl.setObjectName(u"odLbl")
        self.odLbl.setStyleSheet(u"text-align: center;\n"
"font-size: 22pt;")

        self.gridLayout.addWidget(self.odLbl, 0, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color: #00007f;\n"
"color: white;\n"
"font-weight: bold;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;")

        self.gridLayout.addWidget(self.label_11, 5, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: #00007f;\n"
"color: white;\n"
"font-weight: bold;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;")

        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color: #00007f;\n"
"color: white;\n"
"font-weight: bold;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;")

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: #00007f;\n"
"color: white;\n"
"font-weight: bold;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: #00007f;\n"
"color: white;\n"
"font-weight: bold;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.ecLbl = QLabel(self.gridLayoutWidget)
        self.ecLbl.setObjectName(u"ecLbl")
        self.ecLbl.setStyleSheet(u"text-align: center;\n"
"font-size: 22pt;")

        self.gridLayout.addWidget(self.ecLbl, 4, 0, 1, 1)

        self.tempLbl = QLabel(self.gridLayoutWidget)
        self.tempLbl.setObjectName(u"tempLbl")
        self.tempLbl.setStyleSheet(u"text-align: center;\n"
"font-size: 22pt;")

        self.gridLayout.addWidget(self.tempLbl, 0, 0, 1, 1)

        self.phLbl = QLabel(self.gridLayoutWidget)
        self.phLbl.setObjectName(u"phLbl")
        self.phLbl.setStyleSheet(u"text-align: center;\n"
"font-size: 22pt\n"
";")

        self.gridLayout.addWidget(self.phLbl, 2, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: #00007f;\n"
"color: white;\n"
"font-weight: bold;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;")

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.tdsLbl = QLabel(self.gridLayoutWidget)
        self.tdsLbl.setObjectName(u"tdsLbl")
        self.tdsLbl.setStyleSheet(u"text-align: center;\n"
"font-size: 22pt;")

        self.gridLayout.addWidget(self.tdsLbl, 2, 0, 1, 1)

        self.turbLbl = QLabel(self.gridLayoutWidget)
        self.turbLbl.setObjectName(u"turbLbl")
        self.turbLbl.setStyleSheet(u"text-align: center;\n"
"font-size: 22pt;")

        self.gridLayout.addWidget(self.turbLbl, 4, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.pauseBtn = QPushButton(self.centralwidget)
        self.pauseBtn.setObjectName(u"pauseBtn")
        self.pauseBtn.setGeometry(QRect(100, 228, 171, 41))
        self.pauseBtn.setStyleSheet(u"border-radius: 20px;")
        self.saveBtn = QPushButton(self.centralwidget)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(290, 228, 171, 41))
        self.saveBtn.setStyleSheet(u"border-radius: 20px;")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(20, 230, 41, 41))
        self.backBtn.setStyleSheet(u"	height: 40px;\n"
"	border-radius: 20px;\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-weight: 500;\n"
"	font-size: 16px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.odLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">--</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Turbidez NTU)</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">pH</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">CE (uS/cm)</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Temperatura (\u00b0C)</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">TDS (ppm)</span></p></body></html>", None))
        self.ecLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">--</p></body></html>", None))
        self.tempLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">--</p></body></html>", None))
        self.phLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">--</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Ox\u00edgeno disuelto (mg/L)</span></p></body></html>", None))
        self.tdsLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">--</p></body></html>", None))
        self.turbLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">--</p></body></html>", None))
        self.pauseBtn.setText(QCoreApplication.translate("MainWindow", u"Pausar", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.backBtn.setText("")
    # retranslateUi

