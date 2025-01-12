# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cal_Value_EditTavNXH.ui'
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
"font: 11pt Poppins;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(435, 0, 41, 41))
        self.backBtn.setStyleSheet(u"	height: 40px;\n"
"	border-radius: 20px;\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-weight: 500;\n"
"	font-size: 16px;")
        self.widgetKeyboard = QWidget(self.centralwidget)
        self.widgetKeyboard.setObjectName(u"widgetKeyboard")
        self.widgetKeyboard.setGeometry(QRect(0, 140, 480, 135))
        self.widgetKeyboard.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.saveBtn = QPushButton(self.centralwidget)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(260, 100, 211, 31))
        self.saveBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;\n"
"font-size: 11pt;\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 61, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 30, 61, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 30, 61, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 30, 61, 21))
        self.doubleSPinVal1 = QDoubleSpinBox(self.centralwidget)
        self.doubleSPinVal1.setObjectName(u"doubleSPinVal1")
        self.doubleSPinVal1.setGeometry(QRect(20, 60, 101, 26))
        self.doubleSPinVal1.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"font: 12pt \"Poppins\";\n"
"background-color: rgb(234, 234, 234);")
        self.doubleSPinVal1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSPinVal1.setMaximum(500.000000000000000)
        self.doubleSPinVal1.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSPinVal2 = QDoubleSpinBox(self.centralwidget)
        self.doubleSPinVal2.setObjectName(u"doubleSPinVal2")
        self.doubleSPinVal2.setGeometry(QRect(130, 60, 101, 26))
        self.doubleSPinVal2.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"font: 12pt \"Poppins\";\n"
"background-color: rgb(234, 234, 234);")
        self.doubleSPinVal2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSPinVal2.setMaximum(500.000000000000000)
        self.doubleSPinVal2.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSPinVal3 = QDoubleSpinBox(self.centralwidget)
        self.doubleSPinVal3.setObjectName(u"doubleSPinVal3")
        self.doubleSPinVal3.setGeometry(QRect(240, 60, 101, 26))
        self.doubleSPinVal3.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"font: 12pt \"Poppins\";\n"
"background-color: rgb(234, 234, 234);")
        self.doubleSPinVal3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSPinVal3.setMaximum(500.000000000000000)
        self.doubleSPinVal3.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSPinVal4 = QDoubleSpinBox(self.centralwidget)
        self.doubleSPinVal4.setObjectName(u"doubleSPinVal4")
        self.doubleSPinVal4.setGeometry(QRect(350, 60, 101, 26))
        self.doubleSPinVal4.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"font: 12pt \"Poppins\";\n"
"background-color: rgb(234, 234, 234);")
        self.doubleSPinVal4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSPinVal4.setProperty("showGroupSeparator", False)
        self.doubleSPinVal4.setMaximum(500.000000000000000)
        self.doubleSPinVal4.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText("")
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Valor 1</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Valor 2</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Valor 3</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Valor 4</p></body></html>", None))
        self.doubleSPinVal1.setSuffix("")
    # retranslateUi

