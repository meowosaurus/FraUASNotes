from LizziTriesThings.classes.Writer import Writer
from LizziTriesThings.myrequests.writerRequests import writerRequests

request = writerRequests()

if __name__ == '__main__':
    print(request.getAllWriter())