import json
import requests
from types import SimpleNamespace


def addNote(note):
    headers = {
        'Accept': 'application/json',  # Accepting json strings from server
        'Content-Type': 'application/json',  # Sending json strings to server
        'Content-Encoding': 'gzip'  # Compressing all data send by the client to save bandwidth
    }
    try:
        r = requests.post("http://localhost:8090/addNote",
                          data=note.toJSON(),
                          headers=headers)
        return r.content
    except requests.exceptions.RequestException as e:
        return e
