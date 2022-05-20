import sys
from PySide6.QtWidgets import QApplication, QLabel
import requests

request = requests.get("http://localhost:8080/test")
print(request.content)

app = QApplication(sys.argv)
label = QLabel("Hello World!")
label.show()
app.exec()
