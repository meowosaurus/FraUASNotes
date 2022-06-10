package de.frauas.server.Entities;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import java.util.Date;
import java.util.UUID;

@Entity
public class Token {
    @Id
    @Column(nullable = false, length = 20)
    private String token;
    @Column(unique = true, nullable = false)
    private Long writerId;

    private Date lastUsed;

    public Token(){}

    public Token(Long writerId){
        this.writerId = writerId;
        token = UUID.randomUUID().toString();
        lastUsed = new Date();
    }

    public void updateLastUsed(){
        lastUsed = new Date();
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public Long getWriterId() {
        return writerId;
    }

    public void setWriterId(Long writerId) {
        this.writerId = writerId;
    }

    public Date getLastUsed() {
        return lastUsed;
    }

    public String toJson(){
        return "{\"token\":\"" + token + "\"," +
                "\"writerId\":" + writerId + "}";
    }

}