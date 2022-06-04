package de.frauas.server.Entities;

import org.hibernate.annotations.Parameter;
import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;


@Entity
public class Writer {
    @Id
    @GeneratedValue(generator = "sequence-generator_writer")
    @GenericGenerator(
            name = "sequence-generator_writer",
            strategy = "org.hibernate.id.enhanced.SequenceStyleGenerator",
            parameters = {
                    @Parameter(name = "sequence_name", value = "writer_sequence")
            }
    )
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

    public Long getWriterId() {
        return writerId;
    }

    public String toString(){
        return "id = " + writerId +
                "\nuserName = " + userName +
                "\nfirstName = " + firstName +
                "\n email = " + email +
                "\n password = " + password;
    }

    public String toJson(){
        return "{\"writerId\":" + writerId + "," +
                "\"userName\":\"" + userName + "\"," +
                "\"firstName\":\"" + firstName + "\"," +
                "\"email\":\"" + email + "\"}";
    }
}