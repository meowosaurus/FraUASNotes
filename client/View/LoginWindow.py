from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton

class LoginWindow(QDialog):
    def __init__(self, parent) -> None:
        QDialog.__init__(self)
        self.parent = parent 
        self.setWindowTitle("User Login")
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose)
               
        self.resize(400, 300)
        self.UName = QLineEdit(self)
        self.UName.resize(130,20)
        self.UName.move(135,100)

        self.UPass = QLineEdit(self)
        self.UPass.resize(130,20)
        self.UPass.move(135, 160)

        self.RegButton = QPushButton('Login', self) 
        self.RegButton.clicked.connect(self.register)

        self.RegButton.move(168, 190)

    def register(self): 
        if self.UName.text() == "u" and self.UPass.text() == "u":
            self.parent.UsrLoggedIn = True
            print("HI")
        self.close()