import json

class Writer(object):
    def __init__(self, userName, password, id, firstName, email):
        self.userName = userName
        self.password = password
        self.id = id
        self.firstName = firstName
        self.email = email

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)