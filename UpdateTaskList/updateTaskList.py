import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5 import uic, QtGui
import sys
from PyQt5 import QtCore
def updateTaskList(self, date):
    self.tasksListWidget.clear()

    db = sqlite3.connect('Main\data.db')
    cursor = db.cursor()

    query = "SELECT task, completed FROM tasks WHERE date = ?"
    row = (date,)
    results = cursor.execute(query, row).fetchall()
    for result in results:
        item = QListWidgetItem(str(result[0]))
        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        if result[1] == "YES":
            item.setCheckState(QtCore.Qt.Checked)
        elif result[1] == "NO":
            item.setCheckState(QtCore.Qt.Unchecked)
        self.tasksListWidget.addItem(item)