from dataclasses import dataclass
import json


@dataclass
class Token(object):
    token: str
    writerId: str

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)
