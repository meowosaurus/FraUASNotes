package de.frauas.server.Exceptions;

public class NoNotesForWriterException extends RuntimeException {

    public NoNotesForWriterException(Long id){
        super("No Notes for Writer exist, writerId: " + id);
    }
}