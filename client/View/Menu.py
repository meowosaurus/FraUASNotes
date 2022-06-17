from PySide6.QtWidgets import *
from PySide6.QtGui import *

import GUI
import sys
sys.path.append('../')
from Model.Note import Note
from Model.Token import Token
from APIHelper import LoginHelper, NoteHelper

class Menu(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent: GUI = parent
        self.top = 350
        self.left = 0
        self.width = 800
        self.height = 1000
        self.initMe()

    def initMe(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle("FraUasNotes")
        self.notes = NoteHelper.getAllNotes(self.parent.token)


        self.newNoteButton = QPushButton("New note", self)
        self.newNoteButton.clicked.connect(self._clickNewNote)
        self.logoutButton = QPushButton ("Log out", self)
        self.logoutButton.clicked.connect(self._clickLogout)
        self.HBox1 = QHBoxLayout(self)
        self.layout = self.HBox1

        self.VBox2 = QVBoxLayout()
        self.HBox1.addLayout(self.VBox2)

        #n = [Note(1, "eins", "hallo was geht ab", self.parent.writer.writerId)]

        try:
            for note in self.notes:
                self.VBox2.addWidget(self._addNoteButton(note))
        except TypeError:
            pass

        self.VBox2.addStretch(1)

        self.HBox1.addStretch(1)
        self.VBox1 = QVBoxLayout()
        self.HBox1.addLayout(self.VBox1)
        self.VBox1.addWidget(self.newNoteButton)
        self.VBox1.addWidget(self.logoutButton)
        self.VBox1.addStretch(1)
        '''
        # TODO: das richtig ins lprint(self.parent.token.token)
        #         print(self.parent.token.writerId)
        #         allNotes = NoteHelper.getAllNotes(self.parent.token)
        #         print(allNotes)
        #         self._buildTable(allNotes)
        #         self.show()
        #
        #         n = Note(None, "kjlj", "LJlk", None)
        #
        #         def clickButton():
        #             self.parent.OpenTextEditor(n)
        #             self.close()
        #
        #         self.button = QPushButton(n.title, self)
        #         self.button.clicked.connect(clickButton)ayout einbauen
        #print(self.parent.writer)
        '''




    '''
        This function returns one Button that opens a given Note in TextEditor
    '''
    def _addNoteButton(self, note: Note) -> QPushButton:
        def clickButton():
            self.parent.OpenTextEditor(note)
            self.close()
        button = QPushButton(note.title, self)
        button.clicked.connect(clickButton)
        return button

    def _buildTable(self, notes: list):
        self.layout = QVBoxLayout(self)
        try:
            for note in notes:
                self.layout.addWidget(self._addNoteButton(note))
        except TypeError:
            pass
        self.layout.addStretch(1)
        self.setLayout(self.layout)

    def _clickLogout(self):
        #LoginHelper.logout(token)
        self.parent.UserLogin()
        self.close()

    def _clickNewNote(self):
        # TODO: hier muss addNote ID etc zurückgeben
        note = Note(None, "New Note", None, None)
        self.parent.OpenTextEditor(note, True)
        self.close()
