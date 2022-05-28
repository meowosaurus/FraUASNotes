package de.frauas.server;

import org.springframework.web.bind.annotation.*;

@RestController
public class ServerRestController
{
    @PostMapping(value = "/registerUserPost",
                 consumes = "application/json",
                 produces = "application/json")
    @ResponseBody
    public String registerUserPost(@RequestBody NewUserData data)
    {
        return "New User with username " + data.username + ", with password " + data.password
                + ", with email " + data.email + " and prename " + data.prename + " signed up!";
    }

    @PostMapping(value = "/uploadNotePost",
                 consumes = "application/json",
                 produces = "application/json")
    @ResponseBody
    public String uploadNotePost(@RequestBody NoteData data)
    {
        return "Note " + data.name + " with content: '" + data.xml + "' uploaded!";
    }

    @PostMapping(value = "/checkUserLoginPost",
                 consumes = "application/json",
                 produces = "application/json")
    @ResponseBody
    public String checkUserLoginPost(@RequestBody UserData data)
    {
        return "User " + data.username + " logged in with password " + data.password + "!";
    }

    @PostMapping(value = "/loadNotesPost",
                 consumes = "application/json",
                 produces = "application/json")
    @ResponseBody
    public String loadNotesPost(@RequestBody String json)
    {
        return json;
    }
}
