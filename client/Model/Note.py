import dataclasses
import json

class Note(object):
    def __init__(self, noteId, title, note, writerId):
        self.noteId = noteId
        self.title = title
        self.note = note
        self.writerId = writerId

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)