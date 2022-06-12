import sys
import xml.etree.ElementTree as ET

from PySide6 import QtCore
from PySide6.QtGui import Qt, QFont, QAction
from PySide6.QtWidgets import QWidget, QTabWidget, QGridLayout, QVBoxLayout, QTextEdit, QMenuBar, \
    QToolBar, QMainWindow, QFileDialog, QApplication, QPushButton

import GUI_Functionalities


class TextEditor(QMainWindow):
    textbox_1 = None
    filename = None
    path = None

    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        # Initiliaze buttons for later use
        self.underline_button = None
        self.italic_button = None
        self.bold_button = None
        self.heading_button = None
        self.table_button = None
        self.image_button = None

        # Configure window size + title
        self.resize(1920, 1080)
        self.setWindowTitle("FraUasNotes")


        # Call function to create file menu, textbox 1&2 and both toolbars
        self.create_textbox_1()
        self.create_textbox_2()
        self.create_toolbars()
        self.create_menu()
        self.addToolBar(self.toolbar_hori)
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar_vert)
        self.setMenuBar(self.menubar)



        # Add tabs to main layout
        main_layout = QGridLayout()  # Main Layout
        main_layout.addWidget(self.tabs1, 0, 1)
        main_layout.addWidget(self.tabs2, 0, 2)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def create_textbox_1(self):
        # Create textbox
        self.textbox_1 = QTextEdit()

        self.textbox_1.acceptRichText()
        self.textbox_1.installEventFilter(self)
        # Set Fontsize and Fontstyle
        font = QFont('Times', 12)
        self.textbox_1.setFont(font)
        # Fontsize needs to be called again
        self.textbox_1.setFontPointSize(12)
        self.tb_1 = QWidget()  # Creates tb1 as widget
        self.tb_1.layout = QVBoxLayout()  # Creates layout of tab1_1
        self.tb_1.layout.addWidget(self.textbox_1)  # adds textbox to tab1_1
        self.tb_1.setLayout(self.tb_1.layout)
        self.tabs1 = QTabWidget()  # creates tabwidget
        self.tabs1.addTab(self.tb_1, 'Editor')  # adds tab1_1 to tab1 + description

    def create_textbox_2(self):
        self.textbox_2 = QTextEdit(readOnly=True)
        self.tb_2 = QWidget()  # Same functionality as textbox above
        self.tb_2.layout = QVBoxLayout()
        self.tb_2.layout.addWidget(self.textbox_2)
        self.tb_2.setLayout(self.tb_2.layout)
        self.tabs2 = QTabWidget()
        self.tabs2.addTab(self.tb_2, 'Markdown Preview')

    def create_menu(self):
        self.menubar = QMenuBar()  # adds Menubar

        file_menu = self.menubar.addMenu("&File")
        edit_menu = self.menubar.addMenu("&Edit")
        help_menu = self.menubar.addMenu("&Help")

        newFile = QAction("&New File", self)
        newFile.setShortcut("Ctrl+N")
        newFile.triggered.connect(self.new_file)
        file_menu.addAction(newFile)

        openFile = QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.triggered.connect(self.file_open)
        file_menu.addAction(openFile)

        saveFile = QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.triggered.connect(self.save_file)
        file_menu.addAction(saveFile)

    def create_toolbars(self):
        # Creates toolbar horizontal
        self.toolbar_hori = QToolBar()

        # Calls function from GUI_Functionalities and crates bold_button, italic_button, underline_button
        GUI_Functionalities.bold_text(self, self.textbox_1)
        GUI_Functionalities.italic_text(self, self.textbox_1)
        GUI_Functionalities.underline_text(self, self.textbox_1)
        GUI_Functionalities.heading_text(self, self.textbox_1)
        GUI_Functionalities.insertTable(self,self.textbox_1)
        GUI_Functionalities.insertImage(self, self.textbox_1)

        self.back = QPushButton("Back", self)
        self.back.clicked.connect(self.go_to_menu)

        # Adds buttons to toolbar
        self.toolbar_hori.addAction(self.bold_button)
        self.toolbar_hori.addAction(self.italic_button)
        self.toolbar_hori.addAction(self.underline_button)
        self.toolbar_hori.addAction(self.heading_button)
        self.toolbar_hori.addAction(self.table_button)
        self.toolbar_hori.addAction(self.image_button)
        self.toolbar_hori.addWidget(self.back)
        # Creates vertical toolbar
        self.toolbar_vert = QToolBar()
        self.toolbar_vert.setOrientation(Qt.Vertical)

    def file_open(self):
        self.filename = QFileDialog.getOpenFileName()
        self.path = self.filename[0]
        with open(self.path, 'r') as f:
            content = f.read()
            self.textbox_1.setText(content)
            self.textbox_2.setMarkdown(content)

    def save_file(self):
        data = ET.Element('root')
        element1 = ET.SubElement(data, 'Content')
        element1.text = self.textbox_1.toPlainText()
        b_xml = ET.tostring(element1, encoding='utf-8')

        with open("XML_Files/current_file.xml", "wb") as f:
            f.write(b_xml)


    def new_file(self):
        pass

    def go_to_menu(self):
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
