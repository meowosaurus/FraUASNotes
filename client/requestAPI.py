

class RequestAPI(object):

    # Public methods

    # Registers a new user via a post request
    def userRegisterPost(self, json):
        from inspect import currentframe, getframeinfo
        if not self.__is_json(json):
            return "Error in requestAPI.py in line " + getframeinfo(currentframe()).lineno + ": json parameter is no json"
        return self.__checkPostRequest("http://localhost:8080/registerUserPost", json)

    # Checks username and password via a post request
    def userCheckLoginPost(self, json):
        from inspect import currentframe, getframeinfo
        if not self.__is_json(json):
            return "Error in requestAPI.py in line " + str(getframeinfo(currentframe()).lineno) + ": json parameter is no json"
        return self.__checkPostRequest("http://localhost:8080/checkUserLoginPost", json)

    # Downloads all notes as .json file
    def loadNotesPost(self, username):
        from inspect import currentframe, getframeinfo
        if not self.__is_json(username):
            return "Error in requestAPI.py in line " + str(getframeinfo(currentframe()).lineno) + ": json parameter is no json"
        return self.__checkPostRequest("http://localhost:8080/loadNotesPost", username)

    # Private methods

    # Try & catch for post requests
    def __checkPostRequest(self, link, json):
        import requests
        headers = {
            'Accept': 'application/json',  # Accepting json strings from server
            'Content-Type': 'application/json',  # Sending json strings to server
            'Content-Encoding': 'gzip'  # Compressing all data send by the client to save bandwidth
        }
        try:
            r = requests.post(link, data=json, headers=headers)
            return r.content
        except requests.exceptions.RequestException as e:
            return e

    def __is_json(self, s):
        import json
        try:
            json.loads(s)
        except (ValueError, TypeError) as e:
            return False
        return True


