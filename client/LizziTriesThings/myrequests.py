import Writer
import json
import requests
from types import SimpleNamespace

class myrequests(object):

    def convertTest(self, writer):
        print(writer.toJSON())
        s = writer.toJSON()
        writer = json.loads(s, object_hook=lambda d: SimpleNamespace(**d))
        print(writer.userName)

    def login(self, writer):
        headers = {
            'Accept': 'application/json',  # Accepting json strings from server
            'Content-Type': 'application/json',  # Sending json strings to server
            'Content-Encoding': 'gzip'  # Compressing all data send by the client to save bandwidth
        }
        try:
            r = requests.get("http://localhost:8090/login",
                             data=writer.toJSON(),
                             headers=headers)
            return json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))
        except requests.exceptions.RequestException as e:
            return e

    def addWriter(self, writer):
        headers = {
            'Accept': 'application/json',  # Accepting json strings from server
            'Content-Type': 'application/json',  # Sending json strings to server
            'Content-Encoding': 'gzip'  # Compressing all data send by the client to save bandwidth
        }
        try:
            r = requests.get("http://localhost:8090/addWriter",
                              data=writer.toJSON(),
                              headers=headers)
            return json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))
        except requests.exceptions.RequestException as e:
            return e

    def getAllWriter(self):
        headers = {
            'Accept': 'application/json',  # Accepting json strings from server
            'Content-Type': 'application/json',  # Sending json strings to server
            'Content-Encoding': 'gzip'  # Compressing all data send by the client to save bandwidth
        }
        try:
            r = requests.get("http://localhost:8090/getAllWriter",
                              headers=headers)
            return json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))
        except requests.exceptions.RequestException as e:
            return e