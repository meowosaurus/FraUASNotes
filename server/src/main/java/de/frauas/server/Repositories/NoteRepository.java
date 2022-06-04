package de.frauas.server.Repositories;

import de.frauas.server.Entities.Note;
import de.frauas.server.Entities.Writer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface NoteRepository extends JpaRepository<Note, Long> {
    @Query("SELECT note FROM Note note WHERE note.noteId = :id")
    Optional<Note> findById(@Param("id")Long id);

    @Query("SELECT note FROM Note note WHERE note.writerId = :writerId")
    List<Note> findByWriterId(@Param("writerId")Long writerId);

    @Query("SELECT note FROM Note note WHERE note.title = :title")
    List<Note> findByTitle(@Param("title")String title);
}