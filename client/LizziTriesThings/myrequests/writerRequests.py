import json
import requests
from types import SimpleNamespace


def addWriter(writer):
    # now in API Helper as register
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


def getAllWriter():
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

def getWriter(token):
    headers = {
        'Accept': 'application/json',  # Accepting json strings from server
        'Content-Type': 'application/json',  # Sending json strings to server
        'Content-Encoding': 'gzip'  # Compressing all data send by the client to save bandwidth
    }
    try:
        r = requests.get("http://localhost:8090/getWriter/id=" + token.writerId,
                         headers=headers)
        return json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))
    except requests.exceptions.RequestException as e:
        return e