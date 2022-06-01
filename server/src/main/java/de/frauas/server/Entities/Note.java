package de.frauas.server.Entities;

import de.frauas.server.Entities.Writer;

import javax.persistence.*;

@Entity
public class Note {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long noteId;
    private String title;
    private String note;
    private Long writerId;

    public Note(){}

    public Note(String title, String note, Long writerId){
        this.title = title;
        this.note = note;
        this.writerId = writerId;
    }

    public Long getId() {
        return noteId;
    }

    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Long getWriterId() {
        return writerId;
    }

    public void setWriterId(Long writerId) {
        this.writerId = writerId;
    }

}