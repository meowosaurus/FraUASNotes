from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QFileDialog

from View.TextEditor import TextEditor


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
    self.table_button.triggered.connect(
        lambda x: textbox.insertPlainText("| Row | Row |\n| ----------- | ----------- |"))


def safe_button(self):
    self.saveFile = QAction(QIcon('Icons/floppy-disk-solid.png'), "Save file", self)
    self.saveFile.setShortcut("Ctrl+S")
    self.saveFile.triggered.connect(lambda x: TextEditor.save_file(self))


def open_button(self, textbox_1, textbox_2):
    self.openFileFromDisk = QAction(QIcon('Icons/folder-open-solid.png'), "Open file from disk", self)
    self.openFileFromDisk.setShortcut("Ctrl+O")
    self.openFileFromDisk.triggered.connect(lambda x: file_open_disk(self, textbox_1, textbox_2))


def export(self, textbox, name):
    self.exportButton = QAction(QIcon('Icons/folder-open-solid.png'), "Export to PDF", self)
    self.exportButton.setShortcut("Ctrl+O")
    self.exportButton.triggered.connect(lambda x: exportPDF(self, textbox, name))


def getFileName(self):
    filename = QFileDialog.getOpenFileName(filter="*.jpg *.png")
    return filename[0]


#def exportPDF(self, textbox, name):
    #print(name)
    #with open(name, "x") as f:
        #f.write(textbox)
        #f.close()


def file_open_disk(self, textbox_1, textbox_2):
    self.filename = QFileDialog.getOpenFileName()
    self.path = self.filename[0]
    print(self.filename[0])
    with open(self.path, 'r') as f:
        content = f.read()
        textbox_1.setText(content)
        textbox_2.setMarkdown(content)
