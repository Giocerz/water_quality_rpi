# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'folder_widgethgdDjA.ui'
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
        Form.resize(200, 100)
        Form.setStyleSheet(u"border: 2px solid grey;")
        self.nameLbl = QLabel(Form)
        self.nameLbl.setObjectName(u"nameLbl")
        self.nameLbl.setGeometry(QRect(20, 10, 151, 20))
        self.descriptionLbl = QLabel(Form)
        self.descriptionLbl.setObjectName(u"descriptionLbl")
        self.descriptionLbl.setGeometry(QRect(20, 50, 151, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nameLbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.descriptionLbl.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

