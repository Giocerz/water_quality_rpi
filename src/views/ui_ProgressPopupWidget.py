# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProgressPopupWidgetxoLDei.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 272)
        self.lblOpacity = QLabel(Form)
        self.lblOpacity.setObjectName(u"lblOpacity")
        self.lblOpacity.setGeometry(QRect(0, 0, 480, 320))
        self.lblOpacity.setStyleSheet(u"background-color: black;")
        self.WidgetInfo = QWidget(Form)
        self.WidgetInfo.setObjectName(u"WidgetInfo")
        self.WidgetInfo.setEnabled(True)
        self.WidgetInfo.setGeometry(QRect(29, 55, 422, 162))
        self.WidgetInfo.setStyleSheet(u"border-radius: 20px;\n"
"background-color: white;")
        self.LabelInfo = QLabel(self.WidgetInfo)
        self.LabelInfo.setObjectName(u"LabelInfo")
        self.LabelInfo.setGeometry(QRect(10, 10, 401, 61))
        self.LabelInfo.setStyleSheet(u"font: 16px \"Poppins\";\n"
"background-color: transparent;\n"
"")
        self.LabelInfo.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.WidgetInfo)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(27, 80, 371, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 10px;\n"
"    background-color: #f3f3f3;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #00007f;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblOpacity.setText("")
        self.LabelInfo.setText(QCoreApplication.translate("Form", u"Cargando...", None))
    # retranslateUi

