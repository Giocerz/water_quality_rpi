# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SaveBEXHWf.ui'
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
        self.backBtn.setGeometry(QRect(20, 0, 41, 41))
        self.backBtn.setStyleSheet(u"height: 40px;\n"
"border-radius: 20px;\n"
"border: 1px solid #00007f;\n"
"background-color: white;\n"
"color: #00007f;\n"
"font-weight: 500;\n"
"font-size: 11px;")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 481, 271))
        self.tabWidget.setLayoutDirection(Qt.RightToLeft)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 90, 281, 21))
        self.gpsBtn = QPushButton(self.tab_2)
        self.gpsBtn.setObjectName(u"gpsBtn")
        self.gpsBtn.setGeometry(QRect(160, 120, 180, 31))
        self.gpsBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;\n"
"font-size: 11pt;\n"
"")
        self.comboBox = QComboBox(self.tab_2)
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
        self.comboBox.setGeometry(QRect(190, 40, 181, 26))
        self.comboBox.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 40, 51, 21))
        self.saveBtn = QPushButton(self.tab_2)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(350, 190, 111, 31))
        self.saveBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;\n"
"font-size: 11pt;\n"
"")
        self.prevBtn = QPushButton(self.tab_2)
        self.prevBtn.setObjectName(u"prevBtn")
        self.prevBtn.setGeometry(QRect(30, 190, 111, 31))
        self.prevBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;\n"
"font-size: 11pt;\n"
"")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.widgetKeyboard = QWidget(self.tab_1)
        self.widgetKeyboard.setObjectName(u"widgetKeyboard")
        self.widgetKeyboard.setGeometry(QRect(0, 100, 480, 135))
        self.widgetKeyboard.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 26, 51, 21))
        self.inputPlace = QLineEdit(self.tab_1)
        self.inputPlace.setObjectName(u"inputPlace")
        self.inputPlace.setGeometry(QRect(140, 22, 180, 26))
        self.inputPlace.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"font: 12pt \"Poppins\";\n"
"background-color: rgb(234, 234, 234);")
        self.inputPlace.setMaxLength(30)
        self.checkBox = QCheckBox(self.tab_1)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(80, 70, 191, 16))
        self.checkBox.setStyleSheet(u"font-size: 11pt;\n"
"background-color: transparent;\n"
"height: 21px;\n"
"")
        self.nextBtn = QPushButton(self.tab_1)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setGeometry(QRect(350, 60, 111, 31))
        self.nextBtn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00007f;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 15px;\n"
"font-size: 11pt;\n"
"")
        self.tabWidget.addTab(self.tab_1, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.tabWidget.raise_()
        self.backBtn.raise_()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Latitud, longitud</p></body></html>", None))
        self.gpsBtn.setText(QCoreApplication.translate("MainWindow", u"Localizar con GPS", None))
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

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">Fuente:</span></p></body></html>", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.prevBtn.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"P\u00e1gina 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">Lugar:</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u00bfLlovi\u00f3 recientemente?", None))
        self.nextBtn.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"P\u00e1gina 1", None))
    # retranslateUi

