import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5 import uic, QtGui
import sys

from PyQt5 import QtCore
def addNewTask(self):
    db = sqlite3.connect('Main\data.db')
    cursor = db.cursor()

    newTask = str(self.taskLineEdit.text())
    date = self.calendarWidget.selectedDate().toPyDate()

    query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)"
    row = (newTask, "NO", date,)
    cursor.execute(query, row)
    db.commit()
    self.updateTaskList(date)
    self.taskLineEdit.clear()