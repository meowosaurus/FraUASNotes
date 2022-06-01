from myrequests import myrequests
from Writer import Writer

request = myrequests()

if __name__ == '__main__':
    print(request.getAllWriter())