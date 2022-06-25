import sys

from PySide6.QtWidgets import *

import GUI

sys.path.append('../')
from Model.Note import Note
from APIHelper import NoteHelper, LoginHelper


class Menu(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent: GUI = parent
        self.initMe()

    def initMe(self):
        self.resize(450, 800)
        self.setWindowTitle("FraUasNotes")
        self.parent.allNotes = NoteHelper.getAllNotes(self.parent.token)

        # Buttons
        self.newNoteButton = QPushButton("New note", self)
        self.newNoteButton.clicked.connect(self._clickNewNote)
        self.logoutButton = QPushButton("Log out", self)
        self.logoutButton.clicked.connect(self._clickLogout)
        self.deleteButton = QPushButton("Delete Notes", self)
        self.deleteButton.clicked.connect(self._clickDelete)
        self.HBox1 = QHBoxLayout(self)
        self.layout = self.HBox1

        self.VBox2 = QVBoxLayout()
        self.HBox1.addLayout(self.VBox2)

        # Load notes
        self.QnoteList = QListWidget()
        self.QnoteList.setStyleSheet(
            "QListWidget{width: 70%; height: 100%; border-width: 30px; font-size: large;} QListWidget::Item::{background-color: black ;}")
        self.VBox2.addWidget(self.QnoteList)
        try:
            for note in self.parent.allNotes:
                tempItem = QListWidgetItem(note.title)
                self.QnoteList.addItem(tempItem)
        except:
            pass
        self.QnoteList.itemClicked.connect(self._clickNote)

        self.VBox1 = QVBoxLayout()
        self.HBox1.addLayout(self.VBox1)
        self.VBox1.addWidget(self.newNoteButton)
        self.VBox1.addWidget(self.logoutButton)
        self.VBox1.addWidget(self.deleteButton)
        self.VBox1.addStretch(1)

    def _clickNote(self):
        for note in self.parent.allNotes:
            if self.QnoteList.currentItem().text() == note.title:
                self.parent.OpenTextEditor(note)
                self.close()

    def _clickLogout(self):
        LoginHelper.logout(self.parent.token)
        self.parent.UserLogin()
        self.close()

    def _clickNewNote(self):
        note = Note(None, "New Note", None, None)
        self.parent.OpenTextEditor(note, True)
        self.close()

    def _clickDelete(self):
        deleteDialog = QDialog()
        deleteDialog.setWindowTitle("Delete Note")
        deleteDialog.resize(400, 300)
        notesList = self.getNotesList(deleteDialog)

        deleteButton = QPushButton("Delete", deleteDialog)
        deleteButton.move(160, 260)

        def clicked():
            for note in self.parent.allNotes:
                if notesList.currentItem().text() == note.title:
                    NoteHelper.deleteNote(self.parent.token, note)
                    self.parent.allNotes = NoteHelper.getAllNotes(self.parent.token)
                    notesList.removeItemWidget(notesList.currentItem())

        deleteButton.clicked.connect(clicked)

        deleteDialog.exec_()

    def getNotesList(self, window) -> QListWidget:
        notesList = QListWidget(window)
        notesList.resize(400, 250)
        try:
            for note in self.parent.allNotes:
                tempItem = QListWidgetItem(note.title)
                notesList.addItem(tempItem)
        except:
            pass
        return  notesList
