# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lon.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from urllib.parse import urlencode
import requests
import time
import re
import json
def show_MINN():
    app=QtWidgets.QApplication(sys.argv)
    M=QtWidgets.QMainWindow()
    ui=Ui_Form()
    ui.setupUi(M)
    M.show()
    sys.exit(app.exec_())



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(542, 663)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 661))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.q2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.q2.setObjectName("q2")
        self.verticalLayout.addWidget(self.q2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.q2.setPixmap(QPixmap('ddd.jpg'))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">请扫码登录</span></p></body></html>"))
if __name__ == "__main__":
    show_MINN()