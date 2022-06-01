from LizziTriesThings.classes.Writer import Writer
from LizziTriesThings.myrequests.loginRequests import loginRequests

request = loginRequests()

if __name__ == '__main__':
    # login existing Writer
    writerLogin = Writer("mrabe", "9rqHubhNWJw6GH", None, None, None)
    writer = login(writerLogin)
    print(writer)
