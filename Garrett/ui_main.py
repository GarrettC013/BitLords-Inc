# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Zachary Burgess\OneDrive\Documents\GitHub\BitLords-Inc\Garrett\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(852, 514)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 150, 411, 311))
        self.calendarWidget.setStyleSheet("font:12pt;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.tasksListWidget = QtWidgets.QListWidget(Form)
        self.tasksListWidget.setGeometry(QtCore.QRect(480, 150, 341, 301))
        self.tasksListWidget.setStyleSheet("font:12pt;")
        self.tasksListWidget.setObjectName("tasksListWidget")
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(480, 460, 341, 28))
        self.saveButton.setStyleSheet("border-radius:10px;\n"
"background-color: #01BFFF;\n"
"color:white;\n"
"font:11pt;")
        self.saveButton.setObjectName("saveButton")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(730, 110, 93, 28))
        self.addButton.setStyleSheet("border-radius:10px;\n"
"background-color: #01BFFF;\n"
"color:white;\n"
"")
        self.addButton.setObjectName("addButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 851, 101))
        self.label.setStyleSheet("font-size : 24pt;\n"
"background : #01BFFF;\n"
"color:white;\n"
"border-radius:8px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.taskLineEdit = QtWidgets.QLineEdit(Form)
        self.taskLineEdit.setGeometry(QtCore.QRect(480, 110, 241, 31))
        self.taskLineEdit.setStyleSheet("font:12pt;")
        self.taskLineEdit.setObjectName("taskLineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.saveButton.setText(_translate("Form", "Save Changes"))
        self.addButton.setText(_translate("Form", "Add new"))
        self.label.setText(_translate("Form", "Daily Task Planner"))
