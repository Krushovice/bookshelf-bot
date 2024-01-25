from typing import TYPE_CHECKING, Annotated
from .base import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column


if TYPE_CHECKING:
    from bot.core.models.book import Book

intpk = Annotated[int, mapped_column(primary_key=True)]
str_255 = Annotated[str, 255]


class Reader(Base):
    __tablename__ = "readers"

    id: Mapped[intpk]
    first_name: Mapped[str_255]
    last_name: Mapped[str_255]
    username: Mapped[str] = mapped_column(unique=True)
    books: Mapped[list["Book"]] = relationship(
        back_populates="reader",
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)
