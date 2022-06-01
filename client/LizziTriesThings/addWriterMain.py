from myrequests import myrequests
from Writer import Writer

request = myrequests()

if __name__ == '__main__':
    # adding a new Writer
    newWriter = Writer("lizzi", "testPassword", None, "liz", "test@gmail.com")
    # newWriter.addFirstName("liz")
    # newWriter.addEmail("test@gmail.com")
    print(request.addWriter(newWriter))