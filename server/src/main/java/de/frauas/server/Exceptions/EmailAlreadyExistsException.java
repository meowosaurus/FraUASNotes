package de.frauas.server.Exceptions;

public class EmailAlreadyExistsException extends RuntimeException {

    public EmailAlreadyExistsException(String email){
        super("There already exists an account registered with this email: " + email);
    }
}