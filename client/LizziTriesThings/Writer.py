import json


class Writer(object):
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

    def addId(self, id):
        self.id = id

    def addFirstName(self, firstName):
        self.firstName = firstName

    def addEmail(self, email):
        self.email = email

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)