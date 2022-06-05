package de.frauas.server.Utils;

import de.frauas.server.Entities.Token;
import de.frauas.server.Repositories.TokenRepository;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;

import java.util.Date;
import java.util.List;

@Configuration
@EnableScheduling
public class RemoveToken {
    private final TokenRepository tokenRepository;

    public RemoveToken(TokenRepository tokenRepository){
        this.tokenRepository = tokenRepository;
    }

    @Scheduled(fixedDelay = 60_000) //Complete task every 60 seconds
    public void deleteOldTokens(){
        List<Token> tokens = tokenRepository.findAll();
        for(Token token : tokens){
            // 1_800_000L -> 30 minutes
            if(token.getLastUsed().getTime() + 1_800_000L <= new Date().getTime()){
                tokenRepository.deleteTokenByWriterId(token.getWriterId());
                System.out.println("Deleted a token!");
            }
        }
    }
}
