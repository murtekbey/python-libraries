# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_combobox.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 251)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbSehirler = QtWidgets.QComboBox(self.centralwidget)
        self.cbSehirler.setGeometry(QtCore.QRect(30, 20, 161, 21))
        self.cbSehirler.setObjectName("cbSehirler")
        self.lblResult = QtWidgets.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(200, 80, 271, 111))
        self.lblResult.setObjectName("lblResult")
        self.btnGetItems = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetItems.setGeometry(QtCore.QRect(30, 50, 161, 51))
        self.btnGetItems.setObjectName("btnGetItems")
        self.btnLoadItems = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadItems.setGeometry(QtCore.QRect(200, 20, 161, 51))
        self.btnLoadItems.setObjectName("btnLoadItems")
        self.btnClearItems = QtWidgets.QPushButton(self.centralwidget)
        self.btnClearItems.setGeometry(QtCore.QRect(30, 110, 161, 61))
        self.btnClearItems.setObjectName("btnClearItems")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblResult.setText(_translate("MainWindow", "TextLabel"))
        self.btnGetItems.setText(_translate("MainWindow", "Get Items"))
        self.btnLoadItems.setText(_translate("MainWindow", "Load Items"))
        self.btnClearItems.setText(_translate("MainWindow", "Clear Items"))
