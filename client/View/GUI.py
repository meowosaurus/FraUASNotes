import sys
import time

from PySide6.QtWidgets import *

from TextEditor import TextEditor
import LoginWindow
import RegisterWindow
import Menu

sys.path.append('../')
from Model import Note, Token, Writer

class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.token: Token = None
        self.writer: Writer = None
        self.UserLogin()

    def initMenu(self):
        self.Menu = Menu.Menu(self)
        self.Menu.show()
        self.close()

    def UserLogin(self):
        self.qdLogin = LoginWindow.LoginWindow(self)
        self.qdLogin.show()
        self.close()

    def UserRegisers(self):
        self.RegisterWindow = RegisterWindow.RegisterWindow(self)
        self.RegisterWindow.show()
        self.close()

    def OpenTextEditor(self, note: Note):
        self.TextEditor = TextEditor(self)
        self.TextEditor.show()
        self.close()

if __name__ == '__main__':  # Main for testing purposes
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec())
