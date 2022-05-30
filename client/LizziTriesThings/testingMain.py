import sys

from myrequests import myrequests
from Writer import Writer

request = myrequests()

if __name__ == '__main__':
    # adding a new Writer
    newWriter = Writer("mrabe", "9rqHubhNWJw6GH")
    newWriter.addFirstName("Max")
    newWriter.addEmail("mrabe@yes.yes")
    print(request.addWriter(newWriter))

    # login existing Writer
    writerLogin = Writer("mrabe", "9rqHubhNWJw6GH")
    writer = request.login(writerLogin)
    print(writer)