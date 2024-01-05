from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
    )
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from sqlalchemy import String
from typing import Annotated
from bot.config_data.config_reader import settings


async_engine = create_async_engine(
            url=settings.database_url,
            echo=True)

async_session_factory = async_sessionmaker(async_engine)

str_255 = Annotated[str, 255]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_255: String(255)
    }

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx >= self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__}({', '.join(cols)})>"
