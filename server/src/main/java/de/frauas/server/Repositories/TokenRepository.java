package de.frauas.server.Repositories;

import de.frauas.server.Entities.Token;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.transaction.annotation.Transactional;

import java.util.Date;
import java.util.Optional;
import java.util.UUID;

public interface TokenRepository extends JpaRepository<Token, String> {

    @Query("SELECT token FROM Token token WHERE token.writerId = :writerId")
    Optional<Token> findByWriterId(@Param("writerId")Long writerId);

    @Query("SELECT token FROM Token token WHERE token.token = :token")
    Optional<Token> findByToken(@Param("token")String token);

    @Modifying
    @Transactional
    @Query("UPDATE Token token SET token.lastUsed = :lastUsed WHERE token.writerId = :writerId")
    void updateToken(@Param("lastUsed") Date lastUsed, @Param("writerId")Long writerId);

    @Modifying
    @Transactional
    @Query("DELETE FROM Token token WHERE token.writerId = :writerId")
    void deleteTokenByWriterId(@Param("writerId")Long writerId);
}