package de.frauas.server.DTOs;

import java.io.Serializable;
import java.util.Objects;
import java.util.UUID;

public class TokenDto implements Serializable {
    private final UUID token;
    private final Long writerId;

    public TokenDto(UUID token, Long writerId) {
        this.token = token;
        this.writerId = writerId;
    }

    public UUID getToken() {
        return token;
    }

    public Long getWriterId() {
        return writerId;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        TokenDto entity = (TokenDto) o;
        return Objects.equals(this.token, entity.token) &&
                Objects.equals(this.writerId, entity.writerId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(token, writerId);
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() + "(" +
                "token = " + token + ", " +
                "writerId = " + writerId + ")";
    }
}
