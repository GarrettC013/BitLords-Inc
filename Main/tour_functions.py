import sqlite3
import sys
import datetime

from taskList_functions import updateTaskList

from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5 import uic, QtGui, QtWidgets, QtCore
def guidedTour(self):
    def inner():
        db = sqlite3.connect('Main\data.db')
        cursor = db.cursor()
        messageBox = QMessageBox()
        messageBox.setText("Welcome to the Guided Tour")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()
        messageBox2 = QMessageBox()
        messageBox2.setText("Click on the date that you would like to add to the task list")
        messageBox2.setStandardButtons(QMessageBox.Ok)
        messageBox2.exec()
        messageBox3 = QMessageBox()
        messageBox3.setText("Go to the text box and type out the name of the task")
        messageBox3.setStandardButtons(QMessageBox.Ok)
        messageBox3.exec()
        messageBox4 = QMessageBox()
        messageBox4.setText("Click the \"Add New\" button to add the task to the list")
        messageBox4.setStandardButtons(QMessageBox.Ok)
        messageBox4.exec()
        messageBox5 = QMessageBox()
        messageBox5.setText("The new task will then appear on the list")
        messageBox5.setStandardButtons(QMessageBox.Ok)
        messageBox5.exec()
        messageBox6 = QMessageBox()
        messageBox6.setText("Click the \"Save Changes\" button to save the task list for each day")
        messageBox6.setStandardButtons(QMessageBox.Ok)
        messageBox6.exec()
        messageBox7 = QMessageBox()
        messageBox7.setText("If you want to remove a task, click the checkbox and then click save changes to remove the task")
        messageBox7.setStandardButtons(QMessageBox.Ok)
        messageBox7.exec()
    return inner   