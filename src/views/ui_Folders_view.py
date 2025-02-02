# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Folders_viewWDxdZb.ui'
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
        self.backBtn.setGeometry(QRect(435, 2, 41, 41))
        self.backBtn.setStyleSheet(u"	height: 40px;\n"
"	border-radius: 20px;\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-weight: 500;\n"
"	font-size: 16px;")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 431, 272))
        self.scrollArea.setStyleSheet(u"border: none;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 431, 272))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(440, 52, 31, 211))
        self.verticalSlider.setLayoutDirection(Qt.LeftToRight)
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical{ \n"
"    background-color: rgb(234, 234, 234);\n"
"    width: 30px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:vertical { \n"
"    background-color: #00007f;\n"
"   	width: 20px;\n"
"	height: 50px;\n"
"	margin-top: 0px; \n"
"	margin-bottom: 0px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider{\n"
"    background-color: rgb(234, 234, 234);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(99)
        self.verticalSlider.setValue(0)
        self.verticalSlider.setSliderPosition(0)
        self.verticalSlider.setTracking(True)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(True)
        self.verticalSlider.setInvertedControls(True)
        self.emptyFoldersNoticeLbl = QLabel(self.centralwidget)
        self.emptyFoldersNoticeLbl.setObjectName(u"emptyFoldersNoticeLbl")
        self.emptyFoldersNoticeLbl.setGeometry(QRect(50, 40, 341, 81))
        self.emptyFoldersNoticeLbl.setStyleSheet(u"color: grey;\n"
"font-size: 24px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText("")
        self.emptyFoldersNoticeLbl.setText(QCoreApplication.translate("MainWindow", u"No hay carpetas guardadas", None))
    # retranslateUi

