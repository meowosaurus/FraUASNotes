from dataclasses import dataclass
import json


@dataclass
class Writer(object):
    userName: str
    password: str
    writerId: str
    firstName: str
    email: str

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)
