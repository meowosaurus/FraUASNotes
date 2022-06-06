from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel

import sys
sys.path.append('../')
from APIHelper import LoginHelper
from Model.Writer import Writer
from View.GUI import GUI

class RegisterWindow(QDialog):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.setWindowTitle("User Registration")
        self.resize(400,300)

        # Fields
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
        self.password.resize(130, 20)
        self.password.move(135, 110)

        self.QLabelpassword2 = QLabel(self)
        self.QLabelpassword2.setText("Password")
        self.QLabelpassword2.move(60, 140)
        self.password = QLineEdit(self)
        self.password.resize(130, 20)
        self.password.move(135, 140)

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

    def register(self):
        print("trys to reg")
        if self.QLabelpassword.text() != self.QLabelpassword2.text():
            print("Passwöter müssen glecih sein ")
            return
        reply = LoginHelper.addWriter(Writer(self.firstName.text(), self.password.text(), None, self.firstName.text(), self.email.text()))
        print(reply)
        if hasattr(reply, "writerId"):
            print(f"User {reply.userName} registered.")
            # TODO directly log in
            self.parent.UserLogin()
            self.close()
