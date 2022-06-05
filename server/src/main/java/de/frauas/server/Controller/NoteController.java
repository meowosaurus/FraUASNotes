package de.frauas.server.Controller;

import de.frauas.server.DTOs.NoteDto;
import de.frauas.server.Entities.Note;
import de.frauas.server.Entities.Token;
import de.frauas.server.Exceptions.NoNotesForWriterException;
import de.frauas.server.Exceptions.UserDoesNotExistException;
import de.frauas.server.Repositories.NoteRepository;
import de.frauas.server.Repositories.TokenRepository;
import de.frauas.server.Repositories.WriterRepository;
import org.apache.commons.collections4.IterableUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
public class NoteController {

    @Autowired
    private NoteRepository noteRepository;
    @Autowired
    private WriterRepository writerRepository;
    @Autowired
    private TokenRepository tokenRepository;

    @PostMapping("/addNote/token={token}")
    ResponseEntity<String> newNote(@PathVariable("token") Long token, @RequestBody NoteDto noteDto)
            throws UserDoesNotExistException {
        if(writerRepository.findById(noteDto.getWriterId()).isEmpty()){
                throw new UserDoesNotExistException(noteDto.getWriterId());}
        Optional<Token> tokenCheck = tokenRepository.findByToken(token);
        if(tokenCheck.isPresent() &&
                tokenCheck.get().getWriterId().equals(noteDto.getWriterId())) {
            Note note = new Note(
                    noteDto.getTitle(),
                    noteDto.getNote(),
                    noteDto.getWriterId());
            return ResponseEntity.ok().body("Note: " +
                    noteRepository.save(note).getTitle() +
                    " created successfully!");
        }
        return ResponseEntity.ok().body("Token is not correct!");
    }

    @GetMapping("/getAllNotes/token={token}/writerId={writerId}")
    ResponseEntity<String> getAllNotes(@PathVariable("token") Long token, @PathVariable("writerId") Long writerId)
            throws NoNotesForWriterException{
        Optional<Token> tokenCheck = tokenRepository.findByToken(token);
        if(tokenCheck.isPresent() &&
                tokenCheck.get().getWriterId().equals(writerId)) {
            Iterable<Note> notes = noteRepository.findByWriterId(writerId);
            if (IterableUtils.size(notes) == 0)
                throw new NoNotesForWriterException(writerId);

            //HttpHeaders responseHeaders = new HttpHeaders();
            //responseHeaders.set("Content-Encoding", "gzip");

            String s = "{\"notes\":[";
            for (Note note : notes) {
                s += note.toJson();
                s += ",";
            }
            s = s.substring(0, s.length() - 1);
            s += "]}";
            System.out.println(s);
            return ResponseEntity.ok()
                    //.headers(responseHeaders)
                    .body(s);
        }
        return ResponseEntity.ok().body("Token is not correct!");
    }
}