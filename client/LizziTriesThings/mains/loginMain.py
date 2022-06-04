from Model import Writer
from LizziTriesThings.myrequests.loginRequests import login
from LizziTriesThings.myrequests.noteRequests import getAllNotes
from LizziTriesThings.myrequests.writerRequests import getWriter

if __name__ == '__main__':
    # login existing Writer
    writerLogin = Writer("lizzi", "testPassword", None, None, None)
    token = login(writerLogin)
    print(token)
    writer = getWriter(token)
    notes = getAllNotes(writer)
    print(notes)
