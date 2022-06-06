from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel, QVBoxLayout

import sys

sys.path.append('../')
from GUI import GUI
from APIHelper import LoginHelper
from APIHelper import WriterHelper
from Model.Writer import Writer
from View.GUI import GUI
from View.RegisterWindow import RegisterWindow


class LoginWindow(QDialog):
    def __init__(self, parent) -> None:
        QDialog.__init__(self)
        self.parent = parent
        self.setWindowTitle("User Login")

        self.QLabel = QLabel("Enter your login data...", self)
        print(self.QLabel.size())
        self.QLabel.move(130, 60)

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

        self.QLabelMessage = QLabel("", self)
        self.QLabelMessage.move(120, 250)

    def login(self):

        reply = LoginHelper.login(Writer(self.UName.text(), self.UPass.text(), None, None, None))
        if hasattr(reply, "token"):
            print("Successfully logged in")
            self.hide()
            #self.parent.token = reply
            #self.parent.writer = WriterHelper.getWriter(reply)
            self.parent.initMenu()
        else:
            self.QLabelMessage.resize(300,30)
            self.QLabelMessage.setText(reply.Reply)

    def register(self):
        self.parent.UserRegisers()
        self.close()
