import json

class Writer(object):
    def __init__(self, userName, password, writerId, firstName, email):
        self.userName = userName
        self.password = password
        self.writerId = writerId
        self.firstName = firstName
        self.email = email

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)