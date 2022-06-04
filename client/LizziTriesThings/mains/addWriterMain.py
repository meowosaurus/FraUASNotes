from Model.Writer import Writer
from LizziTriesThings.myrequests.writerRequests import addWriter

if __name__ == '__main__':
    newWriter = Writer("lizzi", "testPassword", None, "liz", "test@gmail.com")
    print(addWriter(newWriter))