import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QGridLayout, QVBoxLayout, QTextEdit, QMenuBar, QMenu, \
    QToolBar


class GUI(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(1920, 1080)
        self.setWindowTitle("FraUasNotes")

        self.create_menu()
        self.create_textbox_1()
        self.create_textbox_2()
        self.create_toolbar_horizontal()
        self.create_toolbar_vertical()

        main_layout = QGridLayout()  # Main Layout
        main_layout.setMenuBar(self.menubar)
        main_layout.addWidget(self.tabs1, 2, 2)
        main_layout.addWidget(self.tabs2, 2, 3)
        main_layout.addWidget(self.toolbar_hori, 1, 0)
        main_layout.addWidget(self.toolbar_vert, 0, 0)

        self.setLayout(main_layout)  # sets Layout

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

        self.file_menu = QMenu("&File", self)
        self.menubar.addMenu(self.file_menu)

    def create_toolbar_horizontal(self):
        self.toolbar_hori = QToolBar("Yes")

    def create_toolbar_vertical(self):
        self.toolbar_vert = QToolBar("Yes")
        self.toolbar_vert.setOrientation(Qt.Vertical)
        self.toolbar_vert.setIconSize(QSize(16,16))



if __name__ == '__main__':  # Main for testing purposes
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    app.exec()
