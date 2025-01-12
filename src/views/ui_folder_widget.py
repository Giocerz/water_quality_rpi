# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'folder_widgettOPzhx.ui'
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
        Form.resize(133, 100)
        Form.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"}\n"
"")
        self.nameLbl = QLabel(Form)
        self.nameLbl.setObjectName(u"nameLbl")
        self.nameLbl.setGeometry(QRect(0, 80, 133, 20))
        self.folderBtn = QPushButton(Form)
        self.folderBtn.setObjectName(u"folderBtn")
        self.folderBtn.setGeometry(QRect(26, 0, 81, 81))
        self.folderBtn.setStyleSheet(u"border: 0px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nameLbl.setText("")
        self.folderBtn.setText("")
    # retranslateUi

