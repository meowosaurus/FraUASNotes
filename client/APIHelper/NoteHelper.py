# Lizzi hat Token implementiert

import json
import requests
from types import SimpleNamespace

import sys
sys.path.append('../')

from Model.Note import Note
from Model.Token import Token
from Model.Writer import Writer
from Helpers.PasswordHelper import encode


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
        print(f"added {r.content}")
        return r.content
    except requests.exceptions.RequestException as e:
        return e


def updateNote(token: Token, note: Note):
    print()
    print("--- updating ---")
    print(f"note{note}")
    print()

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
        print(f"updated note{note.title}")
        return r.content
    except requests.exceptions.RequestException as e:
        return e


def deleteNote(token: Token, note: Note):
    headers = {
        'Accept': 'application/json',  # Accepting json strings from server
        'Content-Type': 'application/json',  # Sending json strings to server
        'Content-Encoding': 'gzip',  # Compressing all data send by the client to save bandwidth
        'token':  token.token
    }
    try:
        r = requests.delete("http://localhost:8090/deleteNote",
                            data=note.toJSON(),
                            headers=headers)
        print(f"Deleted Note {note.title}")
    except requests.exceptions.RequestException as e:
        return e

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
            print("return empty list")
            return []
    except requests.exceptions.RequestException as e:
        return e
