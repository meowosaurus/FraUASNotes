import requests.exceptions
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel
import re

import sys
sys.path.append('../')
from APIHelper import WriterHelper
from Model.Writer import Writer
from Helpers import PasswordHelper

class RegisterWindow(QDialog):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.setWindowTitle("User Registration")
        self.resize(400,300)

        # Fields
        self.backToLogin = QPushButton("Back to login", self)
        self.backToLogin.move(282, 265)
        self.backToLogin.clicked.connect(self.goToLoginWindow)

        self.QLabelHeader = QLabel("Please enter your registration data: ", self)
        self.QLabelHeader.move(60,40)

        self.QLabelUName = QLabel(self)
        self.QLabelUName.setText("Username")
        self.QLabelUName.move(60, 80)
        self.userName = QLineEdit(self)
        self.userName.resize(130, 20)
        self.userName.move(135, 80)

        self.QLabelpassword = QLabel(self)
        self.QLabelpassword.setText("Password")
        self.QLabelpassword.move(60, 110)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.resize(130, 20)
        self.password.move(135, 110)

        self.QLabelpassword2 = QLabel(self)
        self.QLabelpassword2.setText("Password")
        self.QLabelpassword2.move(60, 140)
        self.password2 = QLineEdit(self)
        self.password2.setEchoMode(QLineEdit.Password)
        self.password2.resize(130, 20)
        self.password2.move(135, 140)

        self.QLabelName = QLabel(self)
        self.QLabelName.setText("Name")
        self.QLabelName.move(60, 170)
        self.firstName = QLineEdit(self)
        self.firstName.resize(130, 20)
        self.firstName.move(135, 170)

        self.QLabelEmail = QLabel(self)
        self.QLabelEmail.setText("Email")
        self.QLabelEmail.move(60, 200)
        self.email = QLineEdit(self)
        self.email.resize(130, 20)
        self.email.move(135, 200)

        self.RegisterButton = QPushButton("Register", self)
        self.RegisterButton.clicked.connect(self.register)
        self.RegisterButton.move(160, 230)

        self.QLabelMessage = QLabel("", self)
        self.QLabelMessage.move(120, 270)

    def register(self):
        print("Tries to register.")
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        query: dict = {
            (not re.fullmatch(regex, self.email.text())): "No real email format!",
            (not self.firstName.text() or not self.userName.text() or not self.password.text() or not self.email.text()): "No empty spaces!",
            (self.password.text() != self.password2.text()) : "Passwords are unequal!"
        }

        for key in query:
            print(key)
            print(query.get(key))
            if key:
                self.QLabelMessage.setText(query.get(key))
                self.QLabelMessage.resize(280, 20)
                return

        reply = WriterHelper.addWriter(Writer(self.userName.text(), PasswordHelper.encode(self.password.text()), None, self.firstName.text(), self.email.text()))
        if hasattr(reply, "writerId"):
            print(f"User {reply.userName} registered.")
            self.parent.UserLogin()
            self.close()
        elif isinstance(reply, requests.exceptions.ConnectionError):
            self.QLabelMessage.setText("Connection to server failed")
            self.QLabelMessage.resize(200, 20)
            self.QLabelMessage.move(95, 270)
        else:
            self.QLabelMessage.setText("Credentials not free... try again!")
            self.QLabelMessage.move(80, 270)
            self.QLabelMessage.resize(200, 20)
            return


    def goToLoginWindow(self):
        self.parent.UserLogin()
        self.close()