import sys
import types
import xml.etree.ElementTree as ET

from PySide6 import QtCore
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import *

import GUI_Functionalities

sys.path.append("../")
from APIHelper import NoteHelper
from Model.Note import Note

class TextEditor(QMainWindow):
    textbox_1 = None
    filename = None
    path = None

    def __init__(self, parent, note, newNote=False):
        super().__init__()
        self.list = None
        self.note = note
        self.newNote = newNote
        self.parent = parent
        # relaod all the notes
        self.parent.allNotes = NoteHelper.getAllNotes(self.parent.token)
        
        # Initialize buttons for later use
        self.underline_button = None
        self.italic_button = None
        self.bold_button = None
        self.heading_button = None
        self.table_button = None
        self.image_button = None

        # Configure window size + title
        self.resize(1910, 1080)
        self.setWindowTitle("FraUasNotes")

        # Call function to create file menu, textbox 1&2 and both toolbars
        self.create_textbox_1()
        self.create_textbox_2()
        self.create_toolbar()
        #self.create_menu()
        self.createList()
        #self.setMenuBar(self.menubar)

        # Add tabs to main layout
        main_layout = QGridLayout()  # Main Layout
        main_layout.addWidget(self.toolbar_hori,0, 0, 1, 8)
        main_layout.addWidget(self.tabs1, 1, 4, 2, 1)
        main_layout.addWidget(self.tabs2, 1, 6, 2, 1)
        main_layout.addWidget(self.list, 1, 0, 1, 3)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def create_textbox_1(self):
        # Create textbox
        self.textbox_1 = QTextEdit()
        self.textbox_1.setText(self.note.note)
        self.textbox_1.acceptRichText()
        self.textbox_1.installEventFilter(self)
        # Set Font size and Fontstyle
        font = QFont('Times', 12)
        self.textbox_1.setFont(font)
        # Font size needs to be called again
        self.textbox_1.setFontPointSize(12)
        self.tb_1 = QWidget()  # Creates tb1 as widget
        self.tb_1.setStyleSheet("background-color: #323333")
        self.tb_1.layout = QVBoxLayout()  # Creates layout of tab1_1
        self.tb_1.layout.addWidget(self.textbox_1)  # adds textbox to tab1_1
        self.tb_1.setLayout(self.tb_1.layout)
        self.tabs1 = QTabWidget()  # creates tab widget
        self.tabs1.addTab(self.tb_1, 'Editor')  # adds tab1_1 to tab1 + description
        self.tabs1.setStyleSheet("background-color: #323333; color: white;")

    def create_textbox_2(self):
        self.textbox_2 = QTextEdit(readOnly=True)
        self.tb_2 = QWidget()  # Same functionality as textbox above
        self.tb_2.layout = QVBoxLayout()
        self.tb_2.layout.addWidget(self.textbox_2)
        self.tb_2.setLayout(self.tb_2.layout)
        self.tabs2 = QTabWidget()
        self.tabs2.addTab(self.tb_2, 'Markdown Preview')
        self.tabs2.setStyleSheet("background-color: #323333; color: white;")

    def create_menu(self):
        self.menubar = QMenuBar()  # adds Menubar

        file_menu = self.menubar.addMenu("&File")
        edit_menu = self.menubar.addMenu("&Edit")
        help_menu = self.menubar.addMenu("&Help")

        newFile = QAction("&New File", self)
        newFile.setShortcut("Ctrl+N")
        newFile.triggered.connect(self.new_file)
        file_menu.addAction(newFile)

        openFileFromDisk = QAction("&Open File from Disk", self)
        openFileFromDisk.setShortcut("Ctrl+O")
        openFileFromDisk.triggered.connect(self.file_open_disk)
        file_menu.addAction(openFileFromDisk)

        saveFile = QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.triggered.connect(self.save_file)
        file_menu.addAction(saveFile)

    def create_toolbar(self):
        # Creates toolbar horizontal
        self.toolbar_hori = QToolBar()

        # Calls function from GUI_Functionalities and crates bold_button, italic_button, underline_button
        GUI_Functionalities.bold_text(self, self.textbox_1)
        GUI_Functionalities.italic_text(self, self.textbox_1)
        GUI_Functionalities.underline_text(self, self.textbox_1)
        GUI_Functionalities.heading_text(self, self.textbox_1)
        GUI_Functionalities.insertTable(self, self.textbox_1)
        GUI_Functionalities.insertImage(self, self.textbox_1)

        self.back = QPushButton("Back", self)
        self.back.setFixedSize(50,25)
        self.back.clicked.connect(self.go_to_menu)
        self.nameField = QLineEdit(self)
        self.nameField.resize(200, self.height())
        try:
            self.nameField.setText(self.note.title)
        except AttributeError:
            print("No title found")
            pass

        # Adds buttons to toolbar
        self.toolbar_hori.addAction(self.bold_button)
        self.toolbar_hori.addAction(self.italic_button)
        self.toolbar_hori.addAction(self.underline_button)
        self.toolbar_hori.addAction(self.heading_button)
        self.toolbar_hori.addAction(self.table_button)
        self.toolbar_hori.addAction(self.image_button)
        self.toolbar_hori.addWidget(self.nameField)
        self.toolbar_hori.addWidget(self.back)
        # Creates vertical toolbar

    def createList(self):
        self.list = QListWidget()
        if isinstance(self.parent.allNotes, types.SimpleNamespace):
            return
        for note in self.parent.allNotes:
            self.list.addItem(note.title)
        self.list.itemClicked.connect(self.clicked)

    def clicked(self, title):
        for note in self.parent.allNotes:
            if title.text() == note.title:
                print("other note")
                self.save_file()
                self.parent.OpenTextEditor(note)
                self.close()
                return 

    def file_open_disk(self):
        self.filename = QFileDialog.getOpenFileName()
        self.path = self.filename[0]
        with open(self.path, 'r') as f:
            content = f.read()
            self.textbox_1.setText(content)
            self.textbox_2.setMarkdown(content)

    def save_file(self) -> bool:
        if self.newNote:
            if self.nameField.text().rstrip(" ") in list(map(lambda x: str(x.title), self.parent.allNotes)):
                print("name schon besetzt!")
                return False
            NoteHelper.addNote(self.parent.token, Note(None, self.nameField.text().rstrip(), self.textbox_1.toPlainText(),
                                                       self.parent.writer.writerId))
            return True
        else:
            print()
            print(f"saving note {self.nameField.text().rstrip()}")
            print(f"with content: {self.textbox_1.toPlainText()}")
            print(f"with content: {self.textbox_1}")
            print()
            NoteHelper.updateNote(self.parent.token, Note(self.note.noteId, self.note.title, self.textbox_1.toPlainText(), self.note.writerId))
            return True

    def new_file(self):
        pass

    def go_to_menu(self):
        saved = self.save_file()
        if saved:
            self.parent.currentNote = None
            self.parent.initMenu()
            self.close()

    def eventFilter(self, obj, event):
        if obj is self.textbox_1 and event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Space:
                self.textbox_1.insertPlainText(" ")
                self.textbox_2.setMarkdown(self.textbox_1.toPlainText())
                return True
        return super(TextEditor, self).eventFilter(obj, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TextEditor(parent=None)
    w.show()
    app.exec()
