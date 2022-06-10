from PySide6.QtGui import QFont, QAction, QIcon, QKeySequence


def bold_text(self, textbox):
    self.bold_button = QAction(QIcon('Icons/bold-solid.png'), "Bold", self)
    self.bold_button.setShortcut(QKeySequence.Bold)
    self.bold_button.triggered.connect(lambda x: textbox.insertPlainText("****"))


def italic_text(self, textbox):
    self.italic_button = QAction(QIcon('Icons/italic-solid.png'), "Italic", self)
    self.italic_button.setShortcut(QKeySequence.Italic)
    self.italic_button.triggered.connect(lambda x: textbox.insertPlainText("**"))


def underline_text(self, textbox):
    self.underline_button = QAction(QIcon('Icons/underline-solid.png'), "Underline", self)
    self.underline_button.setShortcut(QKeySequence.Underline)
    self.underline_button.triggered.connect(lambda x: textbox.insertPlainText("____"))


def login(self, username, password):
    # creates writer obj - > sends to server - > gets real writer obj. 
    pass
