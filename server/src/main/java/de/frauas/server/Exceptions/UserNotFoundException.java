package de.frauas.server.Exceptions;

public class UserNotFoundException extends RuntimeException{
    public UserNotFoundException(String s){
        super("User could not be found with userName/email: " + s);
    }

    public UserNotFoundException(Long id){
        super("User could not be found with id: " + id);
    }
}
