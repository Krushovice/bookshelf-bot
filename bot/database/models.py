from sqlalchemy import (
    Column, Integer, VARCHAR, TIMESTAMP, ForeignKey
    )
from sqlalchemy.ext.declarative import declarative_base as Base
from sqlalchemy.orm import relationship


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False,
                unique=True,
                primary_key=True,
                autoincrement=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)


class Reader(BaseModel):
    __tablename__ = 'readers'

    first_name = Column(VARCHAR(255), nullable=False)
    last_name = Column(VARCHAR(255), nullable=False)
    username = Column(VARCHAR(255), unique=True, nullable=False)
    books = relationship('Book', backref='reader')


class Book(BaseModel):
    __tablename__ = 'books'

    name = Column(VARCHAR(255),
                  nullable=False,
                  unique=True)
    author = Column(VARCHAR(255),
                    nullable=False
                    )
    category = Column(VARCHAR(255),
                      nullable=False
                      )
    reader_id = Column(Integer,
                       ForeignKey('readers.id',
                                  ondelete='CASCADE'),
                       nullable=False,
                       index=True
                       )
