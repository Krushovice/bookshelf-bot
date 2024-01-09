import datetime
from typing import Annotated
from sqlalchemy import ForeignKey, text
from .db import Base, str_255
from sqlalchemy.orm import relationship, Mapped, mapped_column


intpk = Annotated[int, mapped_column(primary_key=True)]
creaded_at = Annotated[datetime.datetime,
                       mapped_column(
                           server_default=text("TIMEZONE('utc',now())"))]
updated_at = Annotated[datetime.datetime,
                       mapped_column(
                           server_default=text("TIMEZONE('utc',now())"),
                           onupdate=datetime.datetime.utcnow)]


class Reader(Base):
    __tablename__ = 'readers'

    id: Mapped[intpk]
    first_name: Mapped[str_255]
    last_name: Mapped[str_255]
    username: Mapped[str] = mapped_column(unique=True)
    books: Mapped[list["Book"]] = relationship(
        back_populates="reader",
        # primaryjoin="and_(Reader.id == Book.reader_id)",
        # order_by="Book.id.desc()",
    )


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[intpk]
    name: Mapped[str_255]
    author: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str_255] = mapped_column(nullable=True)
    genre: Mapped[str] = mapped_column(nullable=True)
    creaded_at: Mapped[creaded_at]
    updated_at: Mapped[updated_at]
    reader_id: Mapped[int] = mapped_column(ForeignKey("readers.id",
                                                      ondelete="CASCADE"))

    reader: Mapped["Reader"] = relationship(
        back_populates="books",
    )
