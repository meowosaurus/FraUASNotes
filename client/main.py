import json
import sys
from PySide6.QtWidgets import QApplication, QLabel
from requestAPI import RequestAPI
req = RequestAPI()

loginData = {
  "username": "bjsonnen",
  "password": "rYkTGV69YfV3zy"
}
print(req.userCheckLoginPost(json.dumps(loginData)))

newUserData = {
  "username": "mrabe",
  "password": "9rqHubhNWJw6GH",
  "email": "mrabe@yes.yes",
  "prename": "Max"
}
print(req.userRegisterPost(json.dumps(newUserData)))

app = QApplication(sys.argv)
label = QLabel("Hello World!")
label.show()
app.exec()
