# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_tableForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableProducts = QtWidgets.QTableWidget(self.centralwidget)
        self.tableProducts.setGeometry(QtCore.QRect(20, 10, 351, 291))
        self.tableProducts.setObjectName("tableProducts")
        self.tableProducts.setColumnCount(0)
        self.tableProducts.setRowCount(0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(400, 10, 311, 291))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblName = QtWidgets.QLabel(self.widget)
        self.lblName.setObjectName("lblName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblName)
        self.lblPrice = QtWidgets.QLabel(self.widget)
        self.lblPrice.setObjectName("lblPrice")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblPrice)
        self.txtPrice = QtWidgets.QLineEdit(self.widget)
        self.txtPrice.setObjectName("txtPrice")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtPrice)
        self.txtName = QtWidgets.QLineEdit(self.widget)
        self.txtName.setObjectName("txtName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtName)
        self.btnSave = QtWidgets.QPushButton(self.widget)
        self.btnSave.setObjectName("btnSave")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btnSave)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 26))
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
        self.lblName.setText(_translate("MainWindow", "Name:"))
        self.lblPrice.setText(_translate("MainWindow", "Price:"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
