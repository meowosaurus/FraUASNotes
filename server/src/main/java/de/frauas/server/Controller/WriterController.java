package de.frauas.server.Controller;

import de.frauas.server.DTOs.WriterDto;
import de.frauas.server.Exceptions.EmailAlreadyExistsException;
import de.frauas.server.Exceptions.UserNameTakenException;
import de.frauas.server.Exceptions.UserNotFoundException;
import de.frauas.server.Repositories.WriterRepository;
import de.frauas.server.Entities.Writer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
public class WriterController {
    @Autowired
    private WriterRepository writerRepository;

    @PostMapping("/addWriter")
    ResponseEntity<String> newWriter(@RequestBody WriterDto writerDto)
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
        return ResponseEntity.ok().body("Writer: " +
                writerRepository.save(writer).getUserName() +
                " created successfully!");
    }

    @GetMapping("/getAllWriter")
    Iterable<Writer> getAllWriter() {
        return writerRepository.findAll();
    }

    @GetMapping("/getWriter/id={id}")
    Optional<Writer> getWriterById(@PathVariable("id") Long id)
            throws UserNotFoundException {
        writerRepository.findById(id)
                .orElseThrow(() -> new UserNotFoundException(id));
        return writerRepository.findById(id);
    }

    @GetMapping("/getWriter/userName={userName}")
    Optional<Writer> getWriterByUserName(@PathVariable("userName") String userName)
            throws UserNotFoundException {
        writerRepository.findByUserName(userName)
                .orElseThrow(() -> new UserNotFoundException(userName));
        return writerRepository.findByUserName(userName);
    }

    @GetMapping("/getWriter/email={email}")
    Optional<Writer> getWriterByEmail(@PathVariable("email") String email)
            throws UserNotFoundException {
        writerRepository.findByEmail(email)
                .orElseThrow(() -> new UserNotFoundException(email));
        return writerRepository.findByEmail(email);
    }


}