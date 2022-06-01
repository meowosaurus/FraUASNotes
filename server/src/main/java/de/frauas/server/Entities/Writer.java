package de.frauas.server.Entities;

import de.frauas.server.Controller.WriterController;
import org.springframework.context.annotation.ComponentScan;

import javax.persistence.*;

@ComponentScan(basePackageClasses = WriterController.class)
@Entity
public class Writer {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long writerId;

    @Column(unique = true)
    private String userName;

    private String firstName;

    @Column(unique = true)
    private String email;

    private String password;

    public Writer(){

    }

    public Writer(String userName, String firstName, String email, String password){
        this.userName = userName;
        this.firstName = firstName;
        this.email = email;
        this.password = password;
    }

    public String getUserName() {
        return userName;
    }

    public String getPassword() {
        return password;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String toString(){
        return "id = " + writerId +
                "\nuserName = " + userName +
                "\nfirstName = " + firstName +
                "\n email = " + email +
                "\n password = " + password;
    }

    public String toJson(){
        return "{\"id\":" + writerId + "," +
                "\"userName\":\"" + userName + "\"," +
                "\"firstName\":\"" + firstName + "\"," +
                "\"email\":\"" + email + "\"}";
    }
}