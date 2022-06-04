package de.frauas.server.Exceptions;

public class UserDoesNotExistException extends RuntimeException {

    public UserDoesNotExistException(Long id){
        super("There's no User with this id: " + id);
    }
}