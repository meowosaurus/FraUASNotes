import json
import re
from tkinter import N
from tkinter.messagebox import NO
import requests
from types import SimpleNamespace

import sys
sys.path.append('../')

from Model.Token import Token
from Model.Writer import Writer

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
            print(reply.Reply)
            return reply
    except requests.exceptions.RequestException as e:
        return e

def __toToken(SN: SimpleNamespace) -> Token: 
    return Token(SN.token, SN.writerId)

def logout(): 
    pass

def addWriter(writer):
    headers = {
        'Accept': 'application/json',  # Accepting json strings from server
        'Content-Type': 'application/json',  # Sending json strings to server
        'Content-Encoding': 'gzip'  # Compressing all data send by the client to save bandwidth
    }
    try:
        r = requests.get("http://localhost:8090/addWriter",
                         data=writer.toJSON(),
                         headers=headers)
        return json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))
    except requests.exceptions.RequestException as e:
        return e

print(login(Writer("H", "h", None, None, None)).token)
print(login(Writer("H", "h", None, None, None)).writerId)
