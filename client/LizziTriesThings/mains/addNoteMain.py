from LizziTriesThings.classes.Note import Note
from LizziTriesThings.myrequests.noteRequests import addNote

if __name__ == '__main__':
    # adding a new Writer
    newNote = Note(None, "new title", "my note", 9)
    print(addNote(newNote))
