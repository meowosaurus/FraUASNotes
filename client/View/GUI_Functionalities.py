from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QFileDialog


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


def heading_text(self, textbox):
    self.heading_button = QAction(QIcon('Icons/heading-solid.png'), "Heading", self)
    self.heading_button.setShortcut("Ctrl+H")
    self.heading_button.triggered.connect(lambda x: textbox.insertPlainText("#"))


def insertImage(self, textbox):
    self.image_button = QAction(QIcon('Icons/image-solid.png'), "Insert Image", self)
    self.image_button.triggered.connect(lambda x: textbox.insertPlainText("![alt text](" + getFileName(self) + ")"))


def insertTable(self, textbox):
    self.table_button = QAction(QIcon('Icons/table-solid.png'), "Insert table", self)
    self.table_button.triggered.connect(lambda x: textbox.insertPlainText("| Row | Row |\n| ----------- | ----------- |"))

def changeFontSize(self, textbox):
    pass


def changeFontFamily(self, textbox):
    pass

def getFileName(self):
    filename = QFileDialog.getOpenFileName(filter="*.jpg *.png")
    return filename[0]
