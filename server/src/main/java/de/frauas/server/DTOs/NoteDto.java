package de.frauas.server.DTOs;

import java.io.Serializable;
import java.util.Objects;

public class NoteDto implements Serializable {
    private final Long id;
    private final String note;
    private final String title;
    private final Long writerId;

    public NoteDto(Long id, String note, String title, Long writerId) {
        this.id = id;
        this.note = note;
        this.title = title;
        this.writerId = writerId;
    }

    public Long getId() {
        return id;
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
        return Objects.equals(this.id, entity.id) &&
                Objects.equals(this.note, entity.note) &&
                Objects.equals(this.title, entity.title) &&
                Objects.equals(this.writerId, entity.writerId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, note, title, writerId);
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() + "(" +
                "id = " + id + ", " +
                "note = " + note + ", " +
                "title = " + title + ", " +
                "writer = " + writerId + ")";
    }
}
