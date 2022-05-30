import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QGridLayout, QVBoxLayout, QTextEdit, QMenuBar, \
    QToolBar, QMainWindow


class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(1920, 1080)
        self.setWindowTitle("FraUasNotes")

        self.create_menu()
        self.create_textbox_1()
        self.create_textbox_2()
        self.create_toolbars()

        self.addToolBar(self.toolbar_hori)
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar_vert)
        self.setMenuBar(self.menubar)

        main_layout = QGridLayout()  # Main Layout
        main_layout.addWidget(self.tabs1, 0, 1)
        main_layout.addWidget(self.tabs2, 0, 2)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def create_textbox_1(self):
        textbox = QTextEdit()

        self.tb_1 = QWidget()  # Creates tb1 as widget
        self.tb_1.layout = QVBoxLayout()  # Creates layout of tab1_1
        self.tb_1.layout.addWidget(textbox)  # adds textbox to tab1_1
        self.tb_1.setLayout(self.tb_1.layout)
        self.tabs1 = QTabWidget()  # creates tabwidget
        self.tabs1.addTab(self.tb_1, 'Tab 1')  # adds tab1_1 to tab1 + description

    def create_textbox_2(self):
        self.textbox = QTextEdit()
        self.tb_2 = QWidget()  # Same functionality as Widget above
        self.tb_2.layout = QVBoxLayout()
        self.tb_2.layout.addWidget(self.textbox)
        self.tb_2.setLayout(self.tb_2.layout)
        self.tabs2 = QTabWidget()
        self.tabs2.addTab(self.tb_2, 'Tab 2')

    def create_menu(self):
        self.menubar = QMenuBar()  # adds Menubar
        file_menu = self.menubar.addMenu("&File")
        edit_menu = self.menubar.addMenu("&Edit")
        help_menu = self.menubar.addMenu("&Help")

    def create_toolbars(self):
        self.toolbar_hori = QToolBar()

        self.toolbar_vert = QToolBar()
        self.toolbar_vert.setOrientation(Qt.Vertical)


if __name__ == '__main__':  # Main for testing purposes
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    app.exec()
