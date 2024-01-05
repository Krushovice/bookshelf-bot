from sqlalchemy import Integer, and_, or_, select, insert, text
from sqlalchemy.orm import aliased, selectinload
from .db import Base, async_engine, async_session_factory
from .models import Reader, Book


class AsyncOrm:

    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_reader(username: str, first_name: str, last_name: str):
        async with async_session_factory() as session:
            reader = Reader(username=username,
                            first_name=first_name,
                            last_name=last_name)
            session.add(reader)
            await session.commit()

    @staticmethod
    async def select_reader_by_id(user_id: int, **kwargs):
        r = aliased(Reader)

        async with async_session_factory() as session:
            query = (
                select(
                    r.first_name, r.last_name)
                .select_from(r)
                .filter(r.reader_id == user_id)
                )
            print(query.compile(compile_kwargs={'literal_binds': True}))
            res = await session.execute(query)
            result = res.one()
            return result[0]

    @staticmethod
    async def select_reader_by_username(**kwargs):
        r = aliased(Reader)
        async with async_session_factory() as session:
            query = (
                select(
                    r.id)
                .select_from(r)
                .filter(r.username == kwargs['username'])
                )
            print(query.compile(compile_kwargs={'literal_binds': True}))
            res = await session.execute(query)
            result = res.one()
            return result[0]

    @staticmethod
    async def select_readers_by_selectin():
        async with async_session_factory() as session:
            query = (
                select(Reader)
                .options(selectinload(Reader.books))
                )
            print(query.compile(compile_kwargs={'literal_binds': True}))
            res = await session.execute(query)
            result = res.unique().scalars().all()
            return result

    @staticmethod
    async def insert_books(reader_id: int, book_names: list):
        async with async_session_factory() as session:
            books = [Book(name=book_name, reader_id=reader_id) for book_name in book_names] # noqa
            session.add_all(books)
            await session.commit()

    @staticmethod
    async def select_books(user_id: int):
        # Задаем удонобное имя переменной для работы с ORM
        b = aliased(Book)
        async with async_session_factory() as session:
            query = (
                select(
                    b.name)
                .select_from(b)
                .filter(b.reader_id == user_id)
                )
            print(query.compile(compile_kwargs={'literal_binds': True}))
            res = await session.execute(query)
            result = res.all()
            # Извлечение имен книг из результатов запроса
            book_names = [b.name for book in result]
            return book_names

    @staticmethod
    async def update_reader(reader_id: int, **kwargs):
        async with async_session_factory() as session:
            reader = await session.get(Reader, reader_id)
            for key, value in kwargs.items():
                setattr(reader, key, value)
            await session.refresh(reader)
            await session.commit()
