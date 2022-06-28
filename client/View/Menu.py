import sys

from PySide6.QtWidgets import *

import GUI
from View.TextEditor import TextEditor

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

        # create notes list
        self.QnoteList = QListWidget()
        self.QnoteList.setStyleSheet(
            "QListWidget{width: 70%; height: 100%; border-width: 30px; font-size: large;} QListWidget::Item::{background-color: black ;}")
        self.VBox2.addWidget(self.QnoteList)
        self.QnoteList.itemClicked.connect(self._clickNote)

        # fill notes list
        self.filNotesList(self.QnoteList)




        self.VBox1 = QVBoxLayout()
        self.HBox1.addLayout(self.VBox1)
        self.VBox1.addWidget(self.newNoteButton)
        self.VBox1.addWidget(self.logoutButton)
        self.VBox1.addWidget(self.deleteButton)
        self.VBox1.addStretch(1)

    def filNotesList(self, list: QListWidget):
        self.parent.allNotes = NoteHelper.getAllNotes(self.parent.token)
        print(f"filling noteslist {list} with notes: {self.parent.allNotes}")
        list.clear()
        try:
            for note in self.parent.allNotes:
                tempItem = QListWidgetItem(note.title)
                self.QnoteList.addItem(tempItem)
        except:
            pass
        # deprecated
    def loadNotesList(self):
        print("HI")
        self.parent.allNotes = NoteHelper.getAllNotes(self.parent.token)
        print(f"load noteslist with notes: {self.parent.allNotes}")
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
        self.deleteDialog = DeleteDialog(self)



class DeleteDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent: Menu = parent
        self._initMe()
        self.show()

    def _initMe(self):
        self.resize(300, 300)

        listWidget = QListWidget()
        self.setWindowTitle("Delete Notes")

        for note in self.parent.parent.allNotes:
            QListWidgetItem(note.title, listWidget)

        window_layout = QVBoxLayout(self)
        window_layout.addWidget(listWidget)

        button = QPushButton("Delete")

        def click():
            delNote: Note = None
            for note in self.parent.parent.allNotes:
                if listWidget.currentItem().text() == note.title:
                    delNote = note
            try:
                print(listWidget.currentItem().text())
                listWidget.takeItem(listWidget.currentIndex().row())
                NoteHelper.deleteNote(self.parent.parent.token, delNote)
                #self.parent.parent.allNotes = NoteHelper.getAllNotes(self.parent.token)
                self.parent.filNotesList(self.parent.QnoteList)
            except AttributeError:
                pass

        button.clicked.connect(click)
        window_layout.addWidget(button)

        self.setLayout(window_layout)



        '''
        
        self.list = QListWidget()

        for note in self.allNotes:
            QListWidgetItem(note.title, self.list)

        self.button = QPushButton("Delete")
        def _click():
            #self.list.takeItem(self.list.currentIndex().row())
            #print(f"QDialog is trying to delete {self.list.currentItem()}")
            print("Hi")

        self.button.clicked.connect(_click())

        self.window_layout = QVBoxLayout(self)
        self.window_layout.addWidget(self.list)
        self.window_layout.addWidget(self.button)
        self.setLayout(self.window_layout)

        
        
        ######
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
        '''