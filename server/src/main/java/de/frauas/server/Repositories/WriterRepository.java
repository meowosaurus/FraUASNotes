package de.frauas.server.Repositories;

import de.frauas.server.Entities.Writer;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;

import java.util.Optional;

public interface WriterRepository extends CrudRepository<Writer, String> {

    @Query("SELECT writer FROM Writer writer WHERE writer.userName = :userName")
    Optional<Writer> findByUserName(@Param("userName")String userName);

    @Query("SELECT writer FROM Writer writer WHERE writer.email = :email")
    Optional<Writer> findByEmail(@Param("email")String email);

    @Query("SELECT writer FROM Writer writer WHERE writer.id = :id")
    Optional<Writer> findById(@Param("id")Long id);

    @Query("SELECT writer.password FROM Writer writer WHERE writer.userName = :userName")
    String findPasswordByUserName(@Param("userName")String userName);
}