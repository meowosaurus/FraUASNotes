import sys

from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QGridLayout, QVBoxLayout, QTextEdit, QMenuBar, QMenu


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1920, 1080)
        self.setWindowTitle("FraUasNotes")

        main_layout = QGridLayout()  # Main Layout
        textbox = QTextEdit()
        textbox_2 = QTextEdit()
        menubar = QMenuBar()

        self.tb_1 = QWidget()  # Creates tb1 as widget
        self.tb_1.layout = QVBoxLayout()  # Creates layout of tab1_1
        self.tb_1.layout.addWidget(textbox)  # adds textbox to tab1_1
        self.tb_1.setLayout(self.tb_1.layout)
        self.tabs1 = QTabWidget()  # creates tabwidget
        self.tabs1.addTab(self.tb_1, 'Tab 1')  # adds tab1_1 to tab1 + description
        main_layout.addWidget(self.tabs1, 1, 0) #adds Widget to mainLayout

        self.tb_2 = QWidget()                   #Same functionality as Widget above
        self.tb_2.layout = QVBoxLayout()
        self.tb_2.layout.addWidget(textbox_2)
        self.tb_2.setLayout(self.tb_2.layout)
        self.tabs2 = QTabWidget()
        self.tabs2.addTab(self.tb_2, 'Tab 2')
        main_layout.addWidget(self.tabs2, 1, 1)

        fileMenu = QMenu("&File", self)         #adds Menubar
        menubar.addMenu(fileMenu)
        main_layout.addWidget(menubar, 0, 0)    #adds Menubar to Layout


        self.setLayout(main_layout)  # sets Layout


if __name__ == '__main__':  # Main for testing purposes
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    app.exec()
