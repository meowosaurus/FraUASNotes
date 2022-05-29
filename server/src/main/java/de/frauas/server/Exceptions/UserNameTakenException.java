package de.frauas.server.Exceptions;

public class UserNameTakenException extends RuntimeException{

    public UserNameTakenException(String userName){
        super(userName + " is already taken!");
    }
}