# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SaveBzzkNc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Save(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setStyleSheet(u"background-color: white;\n"
"font: 11pt Poppins;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(20, 20, 41, 41))
        self.backBtn.setStyleSheet(u"height: 40px;\n"
"border-radius: 20px;\n"
"border: 1px solid #00007f;\n"
"background-color: white;\n"
"color: #00007f;\n"
"font-weight: 500;\n"
"font-size: 11px;")
        self.widgetKeyboard = QWidget(self.centralwidget)
        self.widgetKeyboard.setObjectName(u"widgetKeyboard")
        self.widgetKeyboard.setGeometry(QRect(0, 185, 480, 135))
        self.widgetKeyboard.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 30, 321, 241))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 6, 51, 21))
        self.inputPlace = QLineEdit(self.widget)
        self.inputPlace.setObjectName(u"inputPlace")
        self.inputPlace.setGeometry(QRect(110, 2, 180, 26))
        self.inputPlace.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"font: 12pt \"Poppins\";\n"
"background-color: rgb(234, 234, 234);")
        self.inputPlace.setMaxLength(10)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 51, 51, 21))
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(110, 50, 181, 26))
        self.comboBox.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;")
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(65, 98, 191, 16))
        self.checkBox.setStyleSheet(u"font-size: 11pt;\n"
"background-color: transparent;\n"
"height: 21px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 130, 101, 21))
        self.gpsBtn = QPushButton(self.widget)
        self.gpsBtn.setObjectName(u"gpsBtn")
        self.gpsBtn.setGeometry(QRect(110, 125, 180, 31))
        self.gpsBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;\n"
"font-size: 11pt;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.widget.raise_()
        self.backBtn.raise_()
        self.widgetKeyboard.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">Lugar:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">Fuente:</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Escoja una opci\u00f3n", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Acu\u00edfero", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Arroyo", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Dep\u00f3sito de agua", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Embalse", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Estanque", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Fuente", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Llave", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Lago", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Lluvia recolectada", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Manantial", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Planta de tto de agua", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"Pozo", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"R\u00edo", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"Tanque de almacenamiento", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"Torre de agua", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"Otro", None))

        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u00bfLlovi\u00f3 recientemente?", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Localizaci\u00f3n:</p></body></html>", None))
        self.gpsBtn.setText(QCoreApplication.translate("MainWindow", u"Localizar con GPS", None))
    # retranslateUi

