from PySide6.QtWidgets import *
from PySide6.QtGui import *

import GUI

import sys
sys.path.append('../')
from Model.Note import Note
from APIHelper import NoteHelper

class Menu(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.top = 350
        self.left = 0
        self.width = 800
        self.height = 1000
        self.initMe()

    def initMe(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle("FraUasNotes")
        #self.buildTable(NoteHelper.getAllNotes(self.parent.writer))
        self.show()

    '''
    This function returns one Button that opens a given Note in TextEditor
    '''
    def addNote(self, note: Note) -> QPushButton:
        def clickButton():
            self.parent.OpenTextEditor(note)
            self.close()
        button = QPushButton(note.title, self)
        button.clicked.connect(clickButton)
        return button

    def buildTable(self, notes: list):
        self.layout = QVBoxLayout(self)
        for note in notes:
            self.layout.addWidget(self.addNote(note))
        self.layout.addStretch(1)
        self.setLayout(self.layout)
