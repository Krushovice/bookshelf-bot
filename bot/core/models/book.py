import datetime
from typing import TYPE_CHECKING
from typing import Annotated
from sqlalchemy import ForeignKey, text
from .base import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column

if TYPE_CHECKING:
    from bot.core.models.reader import Reader

intpk = Annotated[int, mapped_column(primary_key=True)]
str_255 = Annotated[str, 255]
creaded_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc',now())"),
    ),
]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc',now())"),
        onupdate=datetime.datetime.utcnow,
    ),
]


class Book(Base):
    __tablename__ = "books"

    id: Mapped[intpk]
    name: Mapped[str_255]
    author: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str_255] = mapped_column(nullable=True)
    genre: Mapped[str] = mapped_column(nullable=True)
    creaded_at: Mapped[creaded_at]
    updated_at: Mapped[updated_at]
    reader_id: Mapped[int] = mapped_column(
        ForeignKey("readers.id", ondelete="CASCADE"),
    )

    reader: Mapped["Reader"] = relationship(
        back_populates="books",
    )
