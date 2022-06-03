from PySide6.QtGui import QFont, QAction, QIcon, QKeySequence


def bold_text(self, textbox):
    self.bold_button = QAction(QIcon('Icons/bold-solid.png'), "Bold", self)
    self.bold_button.setShortcut(QKeySequence.Bold)
    self.bold_button.setCheckable(True)
    self.bold_button.toggled.connect(lambda x: textbox.setFontWeight(QFont.Bold if x else QFont.Normal))


def italic_text(self, textbox):
    self.italic_button = QAction(QIcon('Icons/italic-solid.png'), "Italic", self)
    self.italic_button.setShortcut(QKeySequence.Italic)
    self.italic_button.setCheckable(True)
    self.italic_button.toggled.connect(textbox.setFontItalic)


def underline_text(self, textbox):
    self.underline_button = QAction(QIcon('Icons/underline-solid.png'), "Underline", self)
    self.underline_button.setStatusTip("Underline")
    self.underline_button.setShortcut(QKeySequence.Underline)
    self.underline_button.setCheckable(True)
    self.underline_button.toggled.connect(textbox.setFontUnderline)


