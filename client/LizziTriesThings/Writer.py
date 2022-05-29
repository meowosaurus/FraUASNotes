import json


class Writer(object):
    def __init__(self, id, userName, firstName, email, password):
        self.id = id
        self.userName = userName
        self.firstName = firstName
        self.email = email
        self.password = password

    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)