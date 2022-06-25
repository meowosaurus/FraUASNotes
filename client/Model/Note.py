from dataclasses import dataclass
import json


@dataclass
class Note(object):
    noteId: str
    title: str
    note: str
    writerId: str

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)