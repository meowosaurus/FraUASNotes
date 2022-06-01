from LizziTriesThings.classes.Writer import Writer
from LizziTriesThings.myrequests.writerRequests import addWriter

if __name__ == '__main__':
    # adding a new Writer
    newWriter = Writer("lizzi", "testPassword", None, "liz", "test@gmail.com")
    # newWriter.addFirstName("liz")
    # newWriter.addEmail("test@gmail.com")
    print(addWriter(newWriter))