# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(918, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnHobilerSecilenleriAl = QtWidgets.QPushButton(self.centralwidget)
        self.btnHobilerSecilenleriAl.setGeometry(QtCore.QRect(60, 230, 151, 61))
        self.btnHobilerSecilenleriAl.setObjectName("btnHobilerSecilenleriAl")
        self.lblResultHobiler = QtWidgets.QLabel(self.centralwidget)
        self.lblResultHobiler.setGeometry(QtCore.QRect(60, 290, 151, 171))
        self.lblResultHobiler.setText("")
        self.lblResultHobiler.setObjectName("lblResultHobiler")
        self.groupHobiler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupHobiler.setGeometry(QtCore.QRect(20, 10, 291, 231))
        self.groupHobiler.setObjectName("groupHobiler")
        self.layoutWidget = QtWidgets.QWidget(self.groupHobiler)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 231, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbSinema = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbSinema.setObjectName("cbSinema")
        self.verticalLayout.addWidget(self.cbSinema)
        self.cbKitap = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbKitap.setObjectName("cbKitap")
        self.verticalLayout.addWidget(self.cbKitap)
        self.cbSpor = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbSpor.setObjectName("cbSpor")
        self.verticalLayout.addWidget(self.cbSpor)
        self.groupDersler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDersler.setGeometry(QtCore.QRect(360, 10, 291, 231))
        self.groupDersler.setObjectName("groupDersler")
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupDersler)
        self.layoutWidget_3.setGeometry(QtCore.QRect(40, 40, 231, 181))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cbWebTasarim = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.cbWebTasarim.setObjectName("cbWebTasarim")
        self.verticalLayout_3.addWidget(self.cbWebTasarim)
        self.cbProgramlama = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.cbProgramlama.setObjectName("cbProgramlama")
        self.verticalLayout_3.addWidget(self.cbProgramlama)
        self.cbMatematik = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.cbMatematik.setObjectName("cbMatematik")
        self.verticalLayout_3.addWidget(self.cbMatematik)
        self.btnDerslerSecilenleriAl = QtWidgets.QPushButton(self.centralwidget)
        self.btnDerslerSecilenleriAl.setGeometry(QtCore.QRect(400, 230, 151, 61))
        self.btnDerslerSecilenleriAl.setObjectName("btnDerslerSecilenleriAl")
        self.lblResultDersler = QtWidgets.QLabel(self.centralwidget)
        self.lblResultDersler.setGeometry(QtCore.QRect(400, 290, 151, 171))
        self.lblResultDersler.setText("")
        self.lblResultDersler.setObjectName("lblResultDersler")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 918, 26))
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
        self.btnHobilerSecilenleriAl.setText(_translate("MainWindow", "Seçilenleri Al"))
        self.groupHobiler.setTitle(_translate("MainWindow", "GroupBox"))
        self.cbSinema.setText(_translate("MainWindow", "Sinema"))
        self.cbKitap.setText(_translate("MainWindow", "Kitap"))
        self.cbSpor.setText(_translate("MainWindow", "Spor"))
        self.groupDersler.setTitle(_translate("MainWindow", "GroupBox"))
        self.cbWebTasarim.setText(_translate("MainWindow", "Web Tasarım"))
        self.cbProgramlama.setText(_translate("MainWindow", "Programlama"))
        self.cbMatematik.setText(_translate("MainWindow", "Matematik"))
        self.btnDerslerSecilenleriAl.setText(_translate("MainWindow", "Seçilenleri Al"))
