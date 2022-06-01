package de.frauas.server.Controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.google.gson.Gson;
import de.frauas.server.DTOs.LoginDto;
import de.frauas.server.Entities.Writer;
import de.frauas.server.Repositories.NoteRepository;
import de.frauas.server.Repositories.WriterRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
public class LoginController {

    @Autowired
    private NoteRepository noteRepository;
    @Autowired
    private WriterRepository writerRepository;

    @GetMapping("/login")
    String login(@RequestBody LoginDto loginDto) throws JsonProcessingException {
        if(writerRepository.findPasswordByUserName(loginDto.getUserName())
            == loginDto.getPassword());

        Optional<Writer> writer = writerRepository.findByUserName(loginDto.getUserName());
        //System.out.println(writer.toString());

        return writer.get().toJson();
    }
}
