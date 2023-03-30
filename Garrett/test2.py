import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5 import uic
import sys

from PyQt5 import QtCore

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi(r"C:\Users\garbe\OneDrive\Documents\GitHub\BitLords-Inc\Garrett\main.ui'", self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())