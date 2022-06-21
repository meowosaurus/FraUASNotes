package de.frauas.server.Controller;

import de.frauas.server.DTOs.TokenDto;
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

    @PostMapping("/addWriter")
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

    @GetMapping("/getWriter")
    String getWriter(@RequestBody TokenDto tokenDto)
            throws UserNotFoundException {
        Optional<Token> tokenCheck = tokenRepository.findByToken(tokenDto.getToken());
        if(tokenCheck.isPresent() &&
                tokenCheck.get().getWriterId().equals(tokenDto.getWriterId())) {
            writerRepository.findByWriterId(tokenDto.getWriterId())
                    .orElseThrow(() -> new UserNotFoundException(tokenDto.getWriterId()));
            tokenCheck.get().updateLastUsed();
            tokenRepository.updateToken(tokenCheck.get().getLastUsed(), tokenCheck.get().getWriterId());
            return writerRepository.findByWriterId(tokenDto.getWriterId()).get().toJson();
        }
        return "{\"Reply\":\"Token is not correct!\"}";
    }
}