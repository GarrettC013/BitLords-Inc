import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5 import uic, QtGui
import sys

from PyQt5 import QtCore


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi(r"Garrett/main.ui", self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)

    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("Date selected:", dateSelected)
        self.updateTaskList(dateSelected)

    def updateTaskList(self, date):
        self.tasksListWidget.clear()

        db = sqlite3.connect('Garrett/data.db')
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

        self.highlightDaysWithTasks()

    def saveChanges(self):
        db = sqlite3.connect("Garrett/data.db")
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

        # Remove checked items from the list
        for i in reversed(range(self.tasksListWidget.count())):
            item = self.tasksListWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                self.tasksListWidget.takeItem(i)

        messageBox = QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

        self.highlightDaysWithTasks()

    def addNewTask(self):
        db = sqlite3.connect("Garrett/data.db")
        cursor = db.cursor()

        newTask = str(self.taskLineEdit.text())
        date = self.calendarWidget.selectedDate().toPyDate()

        query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)"
        row = (newTask, "NO", date,)
        cursor.execute(query, row)
        db.commit()
        self.updateTaskList(date)
        self.taskLineEdit.clear()
        self.highlightDaysWithTasks()

    def highlightDaysWithTasks(self):
        db = sqlite3.connect("Garrett\data.db")
        cursor = db.cursor()
        query = "SELECT DISTINCT date FROM tasks"
        results = cursor.execute(query).fetchall()

        datesWithTasks = [QtCore.QDate(*x) for x in results]

        # get the current month and year of the calendar
        currentMonth = self.calendarWidget.monthShown()
        currentYear = self.calendarWidget.yearShown()

        # iterate through the days in the current month
        for day in range(1, 32):
            try:
                # create a date object for the current day
                date = QtCore.QDate(currentYear, currentMonth, day)

                # set the background color of the day if there are tasks on that day
                if date in datesWithTasks:
                    bgBrush = QtGui.QBrush(QtGui.QColor(0, 255, 0, 100))
                    fmt = QtGui.QTextCharFormat()
                    fmt.setBackground(bgBrush)
                    self.calendarWidget.setDateTextFormat(date, fmt)

            except ValueError:
                # if the day is invalid for the current month, move on to the next day
                continue

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
