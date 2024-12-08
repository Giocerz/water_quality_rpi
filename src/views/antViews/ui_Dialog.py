# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogJAVPNY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(480, 320)
        Dialog.setModal(True)
        self.WidgetInfo = QWidget(Dialog)
        self.WidgetInfo.setObjectName(u"WidgetInfo")
        self.WidgetInfo.setEnabled(True)
        self.WidgetInfo.setGeometry(QRect(29, 79, 422, 162))
        self.WidgetInfo.setStyleSheet(u"border-radius: 20px;\n"
"background-color: white;")
        self.si = QPushButton(self.WidgetInfo)
        self.si.setObjectName(u"si")
        self.si.setGeometry(QRect(220, 110, 122, 41))
        self.si.setStyleSheet(u"font: 500 18px \"Poppins\";\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"background-color: white;\n"
"color: #00007f;")
        self.LabelInfo = QLabel(self.WidgetInfo)
        self.LabelInfo.setObjectName(u"LabelInfo")
        self.LabelInfo.setGeometry(QRect(80, 10, 331, 91))
        self.LabelInfo.setStyleSheet(u"font: 12pt \"Poppins\";\n"
"background-color: transparent;\n"
"")
        self.IconInfo = QLabel(self.WidgetInfo)
        self.IconInfo.setObjectName(u"IconInfo")
        self.IconInfo.setGeometry(QRect(10, 30, 61, 61))
        self.IconInfo.setStyleSheet(u"background-color: transparent;")
        self.no = QPushButton(self.WidgetInfo)
        self.no.setObjectName(u"no")
        self.no.setGeometry(QRect(60, 110, 122, 41))
        self.no.setStyleSheet(u"font: 500 18px \"Poppins\";\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"background-color: white;\n"
"color: #00007f;")
        self.lblOpacity = QLabel(Dialog)
        self.lblOpacity.setObjectName(u"lblOpacity")
        self.lblOpacity.setGeometry(QRect(0, 0, 480, 320))
        self.lblOpacity.setStyleSheet(u"background-color: black;")
        self.lblOpacity.raise_()
        self.WidgetInfo.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.si.setText(QCoreApplication.translate("Dialog", u"Si", None))
        self.LabelInfo.setText(QCoreApplication.translate("Dialog", u"\u00a1Ajustes aplicados exitosamente!", None))
        self.IconInfo.setText("")
        self.no.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.lblOpacity.setText("")
    # retranslateUi

