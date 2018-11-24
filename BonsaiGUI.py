# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BonsaiGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.displayMessage = QtWidgets.QTextBrowser(self.centralwidget)
        self.displayMessage.setGeometry(QtCore.QRect(0, 150, 600, 400))
        self.displayMessage.setObjectName("displayMessage")
        self.tempDisplay = QtWidgets.QLabel(self.centralwidget)
        self.tempDisplay.setGeometry(QtCore.QRect(0, 0, 81, 31))
        self.tempDisplay.setObjectName("tempDisplay")
        self.humDisplay = QtWidgets.QLabel(self.centralwidget)
        self.humDisplay.setGeometry(QtCore.QRect(0, 30, 81, 31))
        self.humDisplay.setObjectName("humDisplay")
        self.fanStatus = QtWidgets.QLabel(self.centralwidget)
        self.fanStatus.setGeometry(QtCore.QRect(110, 0, 81, 31))
        self.fanStatus.setObjectName("fanStatus")
        self.humStatus = QtWidgets.QLabel(self.centralwidget)
        self.humStatus.setGeometry(QtCore.QRect(110, 30, 111, 31))
        self.humStatus.setObjectName("humStatus")
        self.heatStatus = QtWidgets.QLabel(self.centralwidget)
        self.heatStatus.setGeometry(QtCore.QRect(170, 0, 81, 31))
        self.heatStatus.setObjectName("heatStatus")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bonsai Environment Controller"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.tempDisplay.setText(_translate("MainWindow", "Temperature:"))
        self.humDisplay.setText(_translate("MainWindow", "Humidity:"))
        self.fanStatus.setText(_translate("MainWindow", "FAN:OFF"))
        self.humStatus.setText(_translate("MainWindow", "HUMIDIFIER:OFF"))
        self.heatStatus.setText(_translate("MainWindow", "HEAT:OFF"))
        self.label.setText(_translate("MainWindow", "Message Log"))


