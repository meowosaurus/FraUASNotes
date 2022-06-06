# Lizzi hat Token implementiert

import json
import requests
from types import SimpleNamespace

import sys
sys.path.append('../')
from Model.Note import Note

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


'''
Returns a list of all notes a Writer has 
'''
def getAllNotes(writer) -> list:
    headers = {
        'Accept': 'application/json',  # Accepting json strings from server
        'Content-Type': 'application/json',  # Sending json strings to server
        'Content-Encoding': 'gzip'  # Compressing all data send by the client to save bandwidth
    }
    try:
        s = str(writer.writerId)
        r = requests.get("http://localhost:8090/getAllNotes/writerId=" + s,
                         headers=headers)
        return json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))
    except requests.exceptions.RequestException as e:
        return e
