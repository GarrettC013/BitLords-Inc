# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\garbe\OneDrive\Documents\GitHub\BitLords-Inc\Garrett\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from PyQt5 import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(MainWindow)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 150, 411, 311))
        self.calendarWidget.setStyleSheet("font:12pt;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.tasksListWidget = QtWidgets.QListWidget(MainWindow)
        self.tasksListWidget.setGeometry(QtCore.QRect(480, 150, 341, 301))
        self.tasksListWidget.setStyleSheet("font:12pt;")
        self.tasksListWidget.setObjectName("tasksListWidget")
        self.saveButton = QtWidgets.QPushButton(MainWindow)
        self.saveButton.setGeometry(QtCore.QRect(480, 460, 341, 28))
        self.saveButton.setStyleSheet("border-radius:10px;\n"
"background-color: #01BFFF;\n"
"color:white;\n"
"font:11pt;")
        self.saveButton.setObjectName("saveButton")
        self.addButton = QtWidgets.QPushButton(MainWindow)
        self.addButton.setGeometry(QtCore.QRect(730, 110, 93, 28))
        self.addButton.setStyleSheet("border-radius:10px;\n"
"background-color: #01BFFF;\n"
"color:white;\n"
"")
        self.addButton.setObjectName("addButton")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 851, 101))
        self.label.setStyleSheet("font-size : 24pt;\n"
"background : #01BFFF;\n"
"color:white;\n"
"border-radius:8px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.taskLineEdit = QtWidgets.QLineEdit(MainWindow)
        self.taskLineEdit.setGeometry(QtCore.QRect(480, 110, 241, 31))
        self.taskLineEdit.setStyleSheet("font:12pt;")
        self.taskLineEdit.setObjectName("taskLineEdit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saveButton.setText(_translate("MainWindow", "Save Changes"))
        self.addButton.setText(_translate("MainWindow", "Add new"))
        self.label.setText(_translate("MainWindow", "Daily Task Planner"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())