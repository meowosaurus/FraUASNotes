package de.frauas.server.Entities;

import org.hibernate.annotations.Parameter;
import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;

@Entity
public class Note {
    @Id
    @GeneratedValue(generator = "sequence-generator_note")
    @GenericGenerator(
            name = "sequence-generator_note",
            strategy = "org.hibernate.id.enhanced.SequenceStyleGenerator",
            parameters = {
                    @Parameter(name = "sequence_name", value = "note_sequence")
            }
    )
    private Long noteId;
    @Column(unique = true)
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

    public String toJson(){
        return "{\"noteId\":" + noteId + "," +
                "\"title\":\"" + title + "\"," +
                "\"note\":\"" + note + "\"," +
                "\"writerId\":" + writerId + "}";
    }
}