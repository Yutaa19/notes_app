import uuid
import enum
from datetime import datetime, timezone
from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey, Text


class NoteStatus(str, enum.Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    PROTECTED = "protected"
    
class Note(Base):
    __tablename__ = "notes"
    id : Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id : Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), nullable=False)
    title : Mapped[str] = mapped_column(String(255))
    slug : Mapped[str] = mapped_column(String(255))
    content : Mapped[str] = mapped_column(Text, nullable=False)
    status : Mapped[NoteStatus] = mapped_column(default=NoteStatus.PUBLIC)
    password_hash : Mapped[str] = mapped_column(String(255), nullable=True)
    password_hint : Mapped[str] = mapped_column(String(255), nullable=True)
    created_at : Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )
    update_at : Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )
    delete_at : Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True
    )

    users: Mapped["User"] = relationship(back_populates="notes")
    likes: Mapped[list["Likes"]] = relationship(back_populates="note")