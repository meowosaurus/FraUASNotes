
from PySide6.QtGui import Qt, QFont
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QGridLayout, QVBoxLayout, QTextEdit, QMenuBar, \
    QToolBar, QDialog, QLineEdit, QPushButton, QMainWindow

import GUI_Functionalities

class TextEditor(QMainWindow):

    textbox_1 = None

    def __init__(self):
        super().__init__()

        #Initiliaze buttons for later use
        self.underline_button = None
        self.italic_button = None
        self.bold_button = None

        #Configure window size + title
        self.resize(1920, 1080)
        self.setWindowTitle("FraUasNotes")

        #Call function to create file menu, textbox 1&2 and both toolbars
        self.create_menu()
        self.create_textbox_1()
        self.create_textbox_2()
        self.create_toolbars()
        self.addToolBar(self.toolbar_hori)
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar_vert)
        self.setMenuBar(self.menubar)

        #Add tabs to main layout
        main_layout = QGridLayout()  # Main Layout
        main_layout.addWidget(self.tabs1, 0, 1)
        main_layout.addWidget(self.tabs2, 0, 2)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def create_textbox_1(self):

        #Create textbox
        self.textbox_1 = QTextEdit()

        #Set Fontsize and Fontstyle
        font = QFont('Times', 12)
        self.textbox_1.setFont(font)
        #Fontsize needs to be called again
        self.textbox_1.setFontPointSize(12)

        self.tb_1 = QWidget()  # Creates tb1 as widget
        self.tb_1.layout = QVBoxLayout()  # Creates layout of tab1_1
        self.tb_1.layout.addWidget(self.textbox_1)  # adds textbox to tab1_1
        self.tb_1.setLayout(self.tb_1.layout)
        self.tabs1 = QTabWidget()  # creates tabwidget
        self.tabs1.addTab(self.tb_1, 'Tab 1')  # adds tab1_1 to tab1 + description

    def create_textbox_2(self):
        self.textbox_2 = QTextEdit()
        self.tb_2 = QWidget()  # Same functionality as textbox above
        self.tb_2.layout = QVBoxLayout()
        self.tb_2.layout.addWidget(self.textbox_2)
        self.tb_2.setLayout(self.tb_2.layout)
        self.tabs2 = QTabWidget()
        self.tabs2.addTab(self.tb_2, 'Tab 2')

    def create_menu(self):
        self.menubar = QMenuBar()  # adds Menubar
        file_menu = self.menubar.addMenu("&File")
        edit_menu = self.menubar.addMenu("&Edit")
        help_menu = self.menubar.addMenu("&Help")

    def create_toolbars(self):
        #Creates toolbar horizontal
        self.toolbar_hori = QToolBar()

        #Calls function from GUI_Functionalities and crates bold_button, italic_button, underline_button
        GUI_Functionalities.bold_text(self, self.textbox_1)
        GUI_Functionalities.italic_text(self, self.textbox_1)
        GUI_Functionalities.underline_text(self, self.textbox_1)

        #Adds buttons to toolbar
        self.toolbar_hori.addAction(self.bold_button)
        self.toolbar_hori.addAction(self.italic_button)
        self.toolbar_hori.addAction(self.underline_button)

        #Creates vertical toolbar
        self.toolbar_vert = QToolBar()
        self.toolbar_vert.setOrientation(Qt.Vertical)
