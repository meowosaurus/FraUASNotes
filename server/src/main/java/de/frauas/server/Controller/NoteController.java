package de.frauas.server.Controller;

import de.frauas.server.DTOs.NoteDto;
import de.frauas.server.Entities.Note;
import de.frauas.server.Entities.Writer;
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
    String getAllNotes(@PathVariable("writerId") Long writerId){
        Iterable<Note> notes = noteRepository.findByWriterId(writerId);
        //TODO: add exception NoNotesForWriter
        String s = "{\"writers\":[";
        for(Note note: notes) {
            s += note.toJson();
            s += ",";
        }
        s = s.substring(0, s.length() - 1);
        s += "]}";
        System.out.println(s);
        return s;
    }

    @GetMapping("/getAllNotes/title={title}")
    Iterable<Note> getNoteByTitle(@PathVariable("title") String title){
        return noteRepository.findByTitle(title);
    }
}