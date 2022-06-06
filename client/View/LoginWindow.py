from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel, QVBoxLayout

import sys

sys.path.append('../')
from GUI import GUI
from APIHelper import LoginHelper
from Model.Writer import Writer
from View.GUI import GUI
from View.RegisterWindow import RegisterWindow


class LoginWindow(QDialog):
    def __init__(self, parent) -> None:
        QDialog.__init__(self)
        self.parent = parent
        self.setWindowTitle("User Login")

        self.resize(400, 300)
        self.UName = QLineEdit(self)
        self.UName.resize(130, 20)
        self.UName.move(135, 100)

        self.UPass = QLineEdit(self)
        self.UPass.resize(130, 20)
        self.UPass.move(135, 150)

        self.LoginButton = QPushButton('Login', self)
        self.LoginButton.clicked.connect(self.login)

        self.LoginButton.move(168, 190)

        self.RegButton = QPushButton('Register', self)
        self.RegButton.clicked.connect(self.register)
        self.RegButton.move(160, 220)


    def login(self):

        reply = LoginHelper.login(Writer(self.UName.text(), self.UPass.text(), None, None, None))
        if hasattr(reply, "token"):
            print("Successfully logged in")
            self.hide()
            self.parent.initMyself()
        else:
            self.falseLogin = QLabel(reply.Reply)
            self.falseLogin.resize(130, 20)
            self.falseLogin.move(168, 240)


    def register(self):
        self.parent.UserRegisers()
        self.close()
