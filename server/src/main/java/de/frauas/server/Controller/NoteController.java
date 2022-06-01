package de.frauas.server.Controller;

import de.frauas.server.DTOs.NoteDto;
import de.frauas.server.Entities.Note;
import de.frauas.server.Repositories.NoteRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class NoteController {

    @Autowired
    private NoteRepository noteRepository;

    @PostMapping("/addNote")
    ResponseEntity<String> newNote(@RequestBody NoteDto noteDto){
        Note note = new Note(
                noteDto.getTitle(),
                noteDto.getNote(),
                noteDto.getWriterId());
        return ResponseEntity.ok().body("Note: " +
                noteRepository.save(note).getTitle() +
                " created successfully!");
    }

    //TODO: add exception NoteNotFoundException
    //TODO: add exception UserDoesNotExistException

    @GetMapping("/getAllNotes/writerId={writerId}")
    Iterable<Note> getAllNotes(@PathVariable("writerId") Long writerId){
        return noteRepository.findByWriterId(writerId);
    }

    @GetMapping("/getAllNotes/title={title}")
    Iterable<Note> getNoteByTitle(@PathVariable("title") String title){
        return noteRepository.findByTitle(title);
    }
}