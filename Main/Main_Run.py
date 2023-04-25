import sqlite3
import sys

from calendar_functions import calendarDateChanged
from taskList_functions import saveChanges, addNewTask

from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5 import uic, QtGui, QtCore, QtWidgets


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi(r"Main/main.ui", self)
        self.calendarWidget.selectionChanged.connect(calendarDateChanged(self))
        calendarDateChanged(self)
        self.saveButton.clicked.connect(saveChanges(self))
        self.addButton.clicked.connect(addNewTask(self))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())