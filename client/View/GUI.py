import sys
import time

from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QTextEdit, QMenuBar, \
    QToolBar, QMainWindow, QLineEdit, QPushButton, QLabel

import GUI_Functionalities
from TextEditor import TextEditor
import LoginWindow
import RegisterWindow

class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.UserLogin()

    def initMyself(self):
        self.resize(600,600)
        self.show()

    def UserLogin(self):
        self.qdLogin = LoginWindow.LoginWindow(self)
        self.qdLogin.show()
        self.close()

    def UserRegisers(self):
        self.RegisterWindow = RegisterWindow.RegisterWindow(self)
        self.RegisterWindow.show()
        self.close()

    def OpenTextEditor(self):
        self.TextEditor = TextEditor()
        self.TextEditor.show()
        self.close()

if __name__ == '__main__':  # Main for testing purposes
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec())
