package de.frauas.server.Repositories;

import de.frauas.server.Entities.Note;
import de.frauas.server.Entities.Writer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

public interface NoteRepository extends JpaRepository<Note, Long> {
    @Query("SELECT note FROM Note note WHERE note.writerId = :writerId")
    List<Note> findByWriterId(@Param("writerId")Long writerId);

    @Modifying
    @Transactional
    @Query("UPDATE Note note SET note.title = :title, note.note = :note " +
            "WHERE note.noteId = :noteId")
    void updateNote(@Param("title") String title, @Param("note") String note,
                    @Param("noteId") Long noteId);
}