package de.frauas.server.Repositories;

import de.frauas.server.Entities.Writer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.Optional;

public interface WriterRepository extends JpaRepository<Writer, String> {

    @Query("SELECT writer FROM Writer writer WHERE writer.writerId = :writerId")
    Optional<Writer> findByWriterId(@Param("writerId")Long writerId);

    @Query("SELECT writer FROM Writer writer WHERE writer.userName = :userName")
    Optional<Writer> findByUserName(@Param("userName")String userName);

    @Query("SELECT writer FROM Writer writer WHERE writer.email = :email")
    Optional<Writer> findByEmail(@Param("email")String email);

    @Query("SELECT writer.password FROM Writer writer WHERE writer.userName = :userName")
    String findPasswordByUserName(@Param("userName")String userName);
}