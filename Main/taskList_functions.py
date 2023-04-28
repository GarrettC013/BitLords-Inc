import sqlite3
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5 import uic, QtGui, QtWidgets, QtCore

def updateTaskList(self, date): #, time
    def inner():
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
    inner()
    return inner

def saveChanges(self):
    def inner():
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
            print("Query:", query, "Row:", row)
            cursor.execute(query, row)
            db.commit()

        # Remove checked items from the list
        for i in reversed(range(self.tasksListWidget.count())):
            item = self.tasksListWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                self.tasksListWidget.takeItem(i)

        messageBox = QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()
        pass
    return inner

def addNewTask(self):
    print(type(self))
    def inner():
        db = sqlite3.connect('Main\data.db')
        cursor = db.cursor()

        newTask = str(self.taskLineEdit.text())
        
        if newTask.isspace == True:
            messageBox = QMessageBox()
            messageBox.setText("No Task Entered")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()   
        date = self.calendarWidget.selectedDate().toPyDate()

        query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)" 
        row = (newTask, "NO", date,)
        cursor.execute(query, row)
        db.commit()
        updateTaskList(self, date) 
        self.taskLineEdit.clear()

    return inner
