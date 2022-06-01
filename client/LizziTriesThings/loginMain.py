from myrequests import myrequests
from Writer import Writer

request = myrequests()

if __name__ == '__main__':
    # login existing Writer
    writerLogin = Writer("mrabe", "9rqHubhNWJw6GH", None, None, None)
    writer = request.login(writerLogin)
    print(writer)
