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


def login(writer: Writer):
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
        r = requests.post("http://localhost:8090/login",
                          data=writer.toJSON(),
                          headers=headers)
        reply = json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))
        if hasattr(reply, "token") & hasattr(reply, "writerId"):
            return __toToken(reply)
        else:
            return reply
    except requests.exceptions.RequestException as e:
        return "Connection to Server Failed"


def __toToken(SN: SimpleNamespace) -> Token:
    return Token(SN.token, SN.writerId)


def logout(token: Token):
    headers = {
        'Accept': 'application/json',  # Accepting json strings from server
        'Content-Type': 'application/json',  # Sending json strings to server
        'Content-Encoding': 'gzip'  # Compressing all data send by the client to save bandwidth
    }
    try:
        r = requests.delete("http://localhost:8090/logout",
                            data=token.toJSON(),
                            headers=headers)
        print(f"logging out writer {token.writerId}")
        return json.loads(r.content, object_hook=lambda d: SimpleNamespace(**d))
    except requests.exceptions.RequestException as e:
        return e


# print(login(Writer("H", "h", None, None, None)).token)
# print(login(Writer("H", "h", None, None, None)).writerId)

'''
import LoginHelper
import Helpers.PasswordHelper

w = Writer("o", Helpers.PasswordHelper.encode("o"), None,None, None)

print(LoginHelper.login(w))

'''
