import sys
 
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QStackedWidget




class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("window.ui",self)

app= QApplication(sys.argv)
window = Window()
widget = QStackedWidget()

widget.addWidget(window)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")