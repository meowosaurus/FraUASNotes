package de.frauas.server.DTOs;

import java.io.Serializable;
import java.util.Objects;

public class WriterDto implements Serializable {
    private final String userName;
    private final String firstName;
    private final String email;
    private final String password;

    public WriterDto(String userName, String firstName, String email, String password) {
        this.userName = userName;
        this.firstName = firstName;
        this.email = email;
        this.password = password;
    }

    public String getUserName() {
        return userName;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getEmail() {
        return email;
    }

    public String getPassword() {
        return password;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        WriterDto entity = (WriterDto) o;
        return Objects.equals(this.userName, entity.userName) &&
                Objects.equals(this.firstName, entity.firstName) &&
                Objects.equals(this.email, entity.email) &&
                Objects.equals(this.password, entity.password);
    }

    @Override
    public int hashCode() {
        return Objects.hash(userName, firstName, email, password);
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() + "(" +
                "userName = " + userName + ", " +
                "firstName = " + firstName + ", " +
                "email = " + email + ", " +
                "password = " + password + ")";
    }
}
