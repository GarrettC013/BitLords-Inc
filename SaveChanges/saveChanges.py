import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5 import uic, QtGui
import sys

from PyQt5 import QtCore
def saveChanges(self):
    db = sqlite3.connect('Main\data.db')
    cursor = db.cursor()
    date = self.calendarWidget.selectedDate().toPyDate()

    for i in range(self.tasksListWidget.count()):
        item = self.tasksListWidget.item(i)
        task = item.text()
        if item.checkState() == QtCore.Qt.Checked:
            query = "UPDATE tasks SET completed = 'YES' WHERE task = ? AND date = ?"
        else:
            query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND date = ?"
            row = (task, date,)
            cursor.execute(query, row)
    db.commit()
            
    for i in reversed(range(self.tasksListWidget.count())):
        item = self.tasksListWidget.item(i)
        if item.checkState() == QtCore.Qt.Checked:
            self.tasksListWidget.takeItem(i)

    messageBox = QMessageBox()
    messageBox.setText("Changes saved.")
    messageBox.setStandardButtons(QMessageBox.Ok)
    messageBox.exec()