import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QColor

form_class = uic.loadUiType("C:\PyQt\qss\First8.ui")[0]
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 1500, 1200)
        self.setFixedSize(1500,1200)
        
app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()