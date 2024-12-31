# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadingPopupWidgetpMihYW.ui'
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
        self.LabelInfo.setGeometry(QRect(140, 40, 241, 91))
        self.LabelInfo.setStyleSheet(u"font: 12pt \"Poppins\";\n"
"background-color: transparent;\n"
"")
        self.IconInfo = QLabel(self.WidgetInfo)
        self.IconInfo.setObjectName(u"IconInfo")
        self.IconInfo.setGeometry(QRect(50, 50, 60, 60))
        self.IconInfo.setStyleSheet(u"border: 6px solid #ced4da;\n"
"border-radius:  30px;\n"
"border-top: 5px solid #00007f;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblOpacity.setText("")
        self.LabelInfo.setText(QCoreApplication.translate("Form", u"Cargando...", None))
        self.IconInfo.setText("")
    # retranslateUi

