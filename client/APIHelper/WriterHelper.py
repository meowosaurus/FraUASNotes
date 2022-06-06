import json
import requests
from types import SimpleNamespace

import sys
sys.path.append("../")
from Model.Token import Token

def getWriter(token: Token):
    headers = {
        'Accept': 'application/json',  # Accepting json strings from server
        'Content-Type': 'application/json',  # Sending json strings to server
        'Content-Encoding': 'gzip'  # Compressing all data send by the client to save bandwidth
    }
    try:
        r = requests.get("http://localhost:8090/getWriter/id=" + token.writerId,
                         headers=headers)
        return json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))
    except requests.exceptions.RequestException as e:
        return e

