# Lizzi hat Token implementiert

import json
import requests
from types import SimpleNamespace
from Model.Note import Note
from Model.Token import Token

import sys

sys.path.append('../')


def addNote(token: Token, note: Note):
    headers = {
        'Accept': 'application/json',  # Accepting json strings from server
        'Content-Type': 'application/json',  # Sending json strings to server
        'Content-Encoding': 'gzip',  # Compressing all data send by the client to save bandwidth
        'token': token.token
    }
    try:
        r = requests.post("http://localhost:8090/addNote",
                          data=note.toJSON(),
                          headers=headers)
        return r.content
    except requests.exceptions.RequestException as e:
        return e


def updateNote(token, note):
    headers = {
        'Accept': 'application/json',  # Accepting json strings from server
        'Content-Type': 'application/json',  # Sending json strings to server
        'Content-Encoding': 'gzip',  # Compressing all data send by the client to save bandwidth
        'token': token.token
    }
    try:
        r = requests.post("http://localhost:8090/updateNote",
                          data=note.toJSON(),
                          headers=headers)
        return r.content
    except requests.exceptions.RequestException as e:
        return e


'''
Returns a list of all notes a Writer has 
'''


def getAllNotes(token: Token) -> list:
    headers = {
        'Accept': 'application/json',  # Accepting json strings from server
        'Content-Type': 'application/json',  # Sending json strings to server
        'Content-Encoding': 'gzip'  # Compressing all data send by the client to save bandwidth
    }
    try:
        r = requests.get("http://localhost:8090/getAllNotes",
                         data=token.toJSON(),
                         headers=headers)
        s = r.content.replace(b"\n", b"\\n")
        l = json.loads(s, object_hook=lambda d: SimpleNamespace(**d))
        print(l)
        if hasattr(l, "notes"):
            return list(map(lambda x: Note(x.noteId, x.title, x.note, x.writerId), l.notes))
        else:
            return l
    except requests.exceptions.RequestException as e:
        return e


'''
writer = Writer("a", "a", None, None, None)
token = LoginHelper.login(writer)
print(token.token)
addNote(token, Note(None, "xx", "sdjbvljbövhjkvdkv", token.writerId))
addNote(token, Note(None, "fuvbfv", "dhHÖDOIFOÖERG", token.writerId))
notes = getAllNotes(token)
print(notes)
'''
