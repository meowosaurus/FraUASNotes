import sys

from myrequests import requests
from Writer import Writer

request = requests()

if __name__ == '__main__':
    writerLogin = Writer("mrabe", "9rqHubhNWJw6GH")
    writer = request.login(writerLogin)
    print(writer.userName)