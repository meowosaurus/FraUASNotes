import json

class Token(object):
    def __init__(self, token, writerId):
        self.token = token
        self.writerId = writerId

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)