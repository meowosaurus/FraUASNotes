package de.frauas.server.DTOs;

import java.io.Serializable;
import java.util.Objects;

public class NoteDto implements Serializable {
    private final Long noteId;
    private final String note;
    private final String title;
    private final Long writerId;

    public NoteDto(Long noteId, String note, String title, Long writerId) {
        this.noteId = noteId;
        this.note = note;
        this.title = title;
        this.writerId = writerId;
    }

    public Long getNoteId() {
        return noteId;
    }

    public String getNote() {
        return note;
    }

    public String getTitle() {
        return title;
    }

    public Long getWriterId() {
        return writerId;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        NoteDto entity = (NoteDto) o;
        return Objects.equals(this.noteId, entity.noteId) &&
                Objects.equals(this.note, entity.note) &&
                Objects.equals(this.title, entity.title) &&
                Objects.equals(this.writerId, entity.writerId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(noteId, note, title, writerId);
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() + "(" +
                "noteId = " + noteId + ", " +
                "note = " + note + ", " +
                "title = " + title + ", " +
                "writer = " + writerId + ")";
    }
}
