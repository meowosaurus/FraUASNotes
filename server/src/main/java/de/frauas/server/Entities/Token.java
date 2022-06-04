package de.frauas.server.Entities;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import java.util.UUID;

@Entity
public class Token {
    @Id
    @Column(nullable = false, length = 20)
    private UUID token;
    @Column(unique = true, nullable = false)
    private Long writerId;

    public Token(){}

    public Token(Long writerId){
        this.writerId = writerId;
        token = UUID.randomUUID();
    }

    public UUID getToken() {
        return token;
    }

    public void setToken(UUID token) {
        this.token = token;
    }

    public Long getWriterId() {
        return writerId;
    }

    public void setWriterId(Long writerId) {
        this.writerId = writerId;
    }

    public String toJson(){
        return "{\"token\":\"" + token + "\"," +
                "\"writerId\":" + writerId + "}";
    }

}