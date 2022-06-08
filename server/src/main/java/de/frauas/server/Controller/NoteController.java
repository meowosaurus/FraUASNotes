package de.frauas.server.Controller;

import de.frauas.server.DTOs.NoteDto;
import de.frauas.server.DTOs.TokenDto;
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
import java.util.UUID;

@RestController
public class NoteController {

    @Autowired
    private NoteRepository noteRepository;
    @Autowired
    private WriterRepository writerRepository;
    @Autowired
    private TokenRepository tokenRepository;

    @PostMapping("/addNote")
    ResponseEntity<String> newNote(@RequestHeader UUID token, @RequestBody NoteDto noteDto)
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
            tokenCheck.get().updateLastUsed();
            tokenRepository.updateToken(tokenCheck.get().getLastUsed(), tokenCheck.get().getWriterId());
            return ResponseEntity.ok().body("Note: " +
                    noteRepository.save(note).getTitle() +
                    " created successfully!");
        }
        return ResponseEntity.ok().body("Token is not correct!");
    }

    @GetMapping("/getAllNotes")
    ResponseEntity<String> getAllNotes(@RequestBody TokenDto tokenDto)
            throws NoNotesForWriterException{
        Optional<Token> tokenCheck = tokenRepository.findByToken(tokenDto.getToken());
        if(tokenCheck.isPresent() &&
                tokenCheck.get().getWriterId().equals(tokenDto.getWriterId())) {
            Iterable<Note> notes = noteRepository.findByWriterId(tokenDto.getWriterId());
            if (IterableUtils.size(notes) == 0)
                throw new NoNotesForWriterException(tokenDto.getWriterId());

            //HttpHeaders responseHeaders = new HttpHeaders();
            //responseHeaders.set("Content-Encoding", "gzip");

            String s = "{\"notes\":[";
            for (Note note : notes) {
                s += note.toJson();
                s += ",";
            }
            s = s.substring(0, s.length() - 1);
            s += "]}";
            tokenCheck.get().updateLastUsed();
            tokenRepository.updateToken(tokenCheck.get().getLastUsed(), tokenCheck.get().getWriterId());
            return ResponseEntity.ok()
                    //.headers(responseHeaders)
                    .body(s);
        }
        return ResponseEntity.ok().body("Token is not correct!");
    }
}