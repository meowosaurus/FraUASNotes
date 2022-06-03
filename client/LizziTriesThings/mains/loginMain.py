from LizziTriesThings.classes.Writer import Writer
from LizziTriesThings.myrequests.loginRequests import login
from LizziTriesThings.myrequests.noteRequests import getAllNotes

if __name__ == '__main__':
    # login existing Writer
    writerLogin = Writer("lizzi", "testPassword", None, None, None)
    writer = login(writerLogin)
    print(writer)
    notes = getAllNotes(writer)
    print(notes)