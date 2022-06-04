package de.frauas.server.Controller;

import de.frauas.server.DTOs.WriterDto;
import de.frauas.server.Exceptions.EmailAlreadyExistsException;
import de.frauas.server.Exceptions.UserNameTakenException;
import de.frauas.server.Exceptions.UserNotFoundException;
import de.frauas.server.Repositories.WriterRepository;
import de.frauas.server.Entities.Writer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class WriterController {
    @Autowired
    private WriterRepository writerRepository;

    @GetMapping("/addWriter")
    String newWriter(@RequestBody WriterDto writerDto)
            throws UserNameTakenException, EmailAlreadyExistsException {
        writerRepository.findByUserName(writerDto.getUserName()).ifPresent(
                arg -> {throw new UserNameTakenException(writerDto.getUserName());});

        writerRepository.findByEmail(writerDto.getEmail()).ifPresent(
                arg -> {throw new EmailAlreadyExistsException(writerDto.getEmail());});

        Writer writer = new Writer(
                writerDto.getUserName(),
                writerDto.getFirstName(),
                writerDto.getEmail(),
                writerDto.getPassword());
        writerRepository.save(writer);
        return writerRepository.findByUserName(
                writerDto.getUserName()).
                get().toJson();
    }

    @GetMapping("/getAllWriter")
    String getAllWriter() {
        Iterable<Writer> writers = writerRepository.findAll();
        String s = "{\"writers\":[";
        for(Writer writer: writers) {
            s += writer.toJson();
            s += ",";
        }
        s = s.substring(0, s.length() - 1);
        s += "]}";
        System.out.println(s);
        return s;
    }

    @GetMapping("/getWriter/id={id}")
    String getWriterById(@PathVariable("id") Long id)
            throws UserNotFoundException {
        writerRepository.findById(id)
                .orElseThrow(() -> new UserNotFoundException(id));
        return writerRepository.findById(id).get().toJson();
    }

    @GetMapping("/getWriter/userName={userName}")
    String getWriterByUserName(@PathVariable("userName") String userName)
            throws UserNotFoundException {
        writerRepository.findByUserName(userName)
                .orElseThrow(() -> new UserNotFoundException(userName));
        return writerRepository.findByUserName(userName).get().toJson();
    }

    @GetMapping("/getWriter/email={email}")
    String getWriterByEmail(@PathVariable("email") String email)
            throws UserNotFoundException {
        writerRepository.findByEmail(email)
                .orElseThrow(() -> new UserNotFoundException(email));
        return writerRepository.findByEmail(email).get().toJson();
    }


}