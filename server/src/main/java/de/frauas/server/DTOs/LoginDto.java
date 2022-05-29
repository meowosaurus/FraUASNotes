package de.frauas.server.DTOs;

import java.io.Serializable;

public class LoginDto implements Serializable {
    private final String userName;
    private final String password;

    public LoginDto(String userName, String password){
        this.userName = userName;
        this.password = password;
    }

    public String getPassword() {
        return password;
    }

    public String getUserName() {
        return userName;
    }
}
