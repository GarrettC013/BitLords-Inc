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

#def highlightDatesWithTasks(self):
        