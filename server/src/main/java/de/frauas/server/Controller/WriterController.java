package de.frauas.server.Controller;

import de.frauas.server.DTOs.WriterDto;
import de.frauas.server.Entities.Token;
import de.frauas.server.Exceptions.EmailAlreadyExistsException;
import de.frauas.server.Exceptions.UserNameTakenException;
import de.frauas.server.Exceptions.UserNotFoundException;
import de.frauas.server.Repositories.TokenRepository;
import de.frauas.server.Repositories.WriterRepository;
import de.frauas.server.Entities.Writer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
public class WriterController {
    @Autowired
    private WriterRepository writerRepository;
    @Autowired
    private TokenRepository tokenRepository;

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

    @GetMapping("/getWriter/token={token}/writerId={writerId}")
    String getWriterById(@PathVariable("token") Long token, @PathVariable("writerId") Long writerId)
            throws UserNotFoundException {
        Optional<Token> tokenCheck = tokenRepository.findByToken(token);
        if(tokenCheck.isPresent() &&
                tokenCheck.get().getWriterId().equals(writerId)) {
            writerRepository.findById(writerId)
                    .orElseThrow(() -> new UserNotFoundException(writerId));
            tokenCheck.get().updateLastUsed();
            tokenRepository.updateToken(tokenCheck.get().getLastUsed(), tokenCheck.get().getWriterId());
            return writerRepository.findById(writerId).get().toJson();
        }
        return "{\"Reply\":\"Token is not correct!\"}";
    }

    @GetMapping("/getWriter/token={token}/userName={userName}")
    String getWriterByUserName(@PathVariable("token") Long token, @PathVariable("userName") String userName)
            throws UserNotFoundException {
        Optional<Token> tokenCheck = tokenRepository.findByToken(token);
        if(tokenCheck.isPresent()){
            Writer writer = writerRepository.findByUserName(userName)
                    .orElseThrow(() -> new UserNotFoundException(userName));
            if(tokenCheck.get().getWriterId().equals(writer.getWriterId())) {
                tokenCheck.get().updateLastUsed();
                tokenRepository.updateToken(tokenCheck.get().getLastUsed(), tokenCheck.get().getWriterId());
                return writer.toJson();
            }
        }
        return "{\"Reply\":\"Token is not correct!\"}";
    }

    @GetMapping("/getWriter/token={token}/email={email}")
    String getWriterByEmail(@PathVariable("token") Long token, @PathVariable("email") String email)
            throws UserNotFoundException {
        Optional<Token> tokenCheck = tokenRepository.findByToken(token);
        if (tokenCheck.isPresent()){
            Writer writer = writerRepository.findByEmail(email)
                .orElseThrow(() -> new UserNotFoundException(email));
            if(tokenCheck.get().getWriterId().equals(writer.getWriterId())) {
                tokenCheck.get().updateLastUsed();
                tokenRepository.updateToken(tokenCheck.get().getLastUsed(), tokenCheck.get().getWriterId());
                return writerRepository.findByEmail(email).get().toJson();
            }
        }
        return "{\"Reply\":\"Token is not correct!\"}";
    }
}