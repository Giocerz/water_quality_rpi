# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Graphics_viewoWPjIN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Graphics_view(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 320)
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
"}\n"
"\n"
"QLabel {\n"
"	color: #00007f;\n"
"}\n"
"")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(20, 20, 41, 41))
        self.backBtn.setStyleSheet(u"")
        self.graphWidget = QWidget(self.centralwidget)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setGeometry(QRect(9, 69, 461, 241))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText("")
    # retranslateUi
