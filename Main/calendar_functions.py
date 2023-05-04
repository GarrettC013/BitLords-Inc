import sqlite3
import sys
#import datetime

from taskList_functions import updateTaskList

from PyQt5.QtGui import QTextCharFormat, QColor
from datetime import datetime

from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5 import uic, QtGui, QtWidgets, QtCore

def calendarDateChanged(self):
        def inner():
                print("The calendar date was changed.")
                dateSelected = self.calendarWidget.selectedDate().toPyDate()
                print("Date selected:", dateSelected)
                updateTaskList(self,dateSelected)
                pass
        return inner

def highlightDatesWithTask(self):
    self.calendarWidget.setDateTextFormat(QtCore.QDate(), QtGui.QTextCharFormat())
    self.calendarWidget.setDateTextFormat(QtCore.QDate(), QtGui.QTextCharFormat())
    # retrieve all the dates that have tasks in the database
    conn = sqlite3.connect('Main\data.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT date FROM tasks")
    rows = c.fetchall()
    dates = [QtCore.QDate.fromString(str(row[0]), "yyyy-MM-dd") for row in rows]
    # highlight the dates in the calendar
    for date in dates:
        fmt = QtGui.QTextCharFormat()
        fmt.setBackground(QtGui.QBrush(QtGui.QColor("#FF8C00")))
        self.calendarWidget.setDateTextFormat(date, fmt)
    conn.close()