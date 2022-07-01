import sys

from PySide6.QtWidgets import *

import LoginWindow
import Menu
import RegisterWindow
from TextEditor import TextEditor
from View.RegisterWindow import RegisterWindow

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
        self.RegisterWindow = RegisterWindow(self)
        self.RegisterWindow.show()
        self.close()

    def OpenTextEditor(self, note: Note, newNote=False):
        self.TextEditor = TextEditor(self, note, newNote)
        self.TextEditor.textbox_2.setMarkdown(self.TextEditor.textbox_1.toPlainText())
        self.TextEditor.show()
        self.close()

if __name__ == '__main__':  # Main for testing purposes
    app = QApplication(sys.argv)
    # Open the sqq styles file and read in the css-alike styling code
    with open('style.qss', 'r') as f:
        style = f.read()
        # Set the stylesheet of the application
        app.setStyleSheet(style)
    app.setStyle('Fusion')
    gui = GUI()
    sys.exit(app.exec())
