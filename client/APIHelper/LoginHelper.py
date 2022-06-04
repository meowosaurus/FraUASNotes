import json
import re
from tkinter import N
from tkinter.messagebox import NO
import requests
from types import SimpleNamespace

import sys
sys.path.append('../')

from Model.Token import Token

def login(writer):
    '''
    Logs in writer using the password and name. 
    Returns None, if login failed and token, if login succeeded 
    '''
    headers = {
        'Accept': 'application/json',  # Accepting json strings from server
        'Content-Type': 'application/json',  # Sending json strings to server
        'Content-Encoding': 'gzip'  # Compressing all data send by the client to save bandwidth
    }
    try:
        r = requests.get("http://localhost:8090/login",
                         data=writer.toJSON(),
                         headers=headers)
        reply = json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))
        if hasattr(reply, "token"): 
            return __toToken(reply)
        else: 
            print(reply)
            return None
    except requests.exceptions.RequestException as e:
        return e

def __toToken(SN: SimpleNamespace) -> Token: 
    return Token(SN.token, SN.writerId)

def logout(): 
    pass

#from Model.Writer import Writer
#a = login(Writer("Hendrikwe", "1234", None, None, None))