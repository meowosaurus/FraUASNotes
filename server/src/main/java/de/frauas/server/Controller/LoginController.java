package de.frauas.server.Controller;

import de.frauas.server.DTOs.LoginDto;
import de.frauas.server.Entities.Token;
import de.frauas.server.Entities.Writer;
import de.frauas.server.Repositories.NoteRepository;
import de.frauas.server.Repositories.TokenRepository;
import de.frauas.server.Repositories.WriterRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Objects;
import java.util.Optional;

@RestController
public class LoginController {

    @Autowired
    private NoteRepository noteRepository;
    @Autowired
    private WriterRepository writerRepository;
    @Autowired
    private TokenRepository tokenRepository;

    @GetMapping("/login")
    String login(@RequestBody LoginDto loginDto) {
        String password = writerRepository.findPasswordByUserName(loginDto.getUserName());
        String passwordCheck = loginDto.getPassword();
        if(Objects.equals(password, passwordCheck)) {
            Optional<Writer> writer = writerRepository.findByUserName(loginDto.getUserName());
            //check if token exists
            Optional<Token> tokenCheck = tokenRepository.findByWriterId(writer.get().getWriterId());
            if(tokenCheck.isPresent()){
                tokenRepository.deleteTokenByWriterId(tokenCheck.get().getWriterId());
            }

            Token token = new Token(writer.get().getWriterId());
            tokenRepository.save(token);
            Optional<Token>tokenReturn = tokenRepository.findByWriterId(writer.get().getWriterId());
            System.out.println(tokenReturn.get().toJson());
            return tokenReturn.get().toJson();
        }
        return "{\"Reply\":\"Password is wrong!\"}";
    }
}
