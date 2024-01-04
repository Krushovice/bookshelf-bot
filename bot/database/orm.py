from sqlalchemy import Integer, and_, or_, select, insert, text
from db import Base, async_engine, async_session_factory
from models import Reader, Book


class AsyncOrm:

    @staticmethod
    async def create_tables():
        async with async_engine.begin as conn:
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
    async def select_reader(user_id: int):
        async with async_session_factory() as session:
            query = (
                select(
                    Reader.first_name, Reader.last_name)
                .select_from(Reader)
                .filter(Reader.reader_id == user_id)
                )
            print(query.compile(compile_kwargs={'literal_binds': True}))
            res = await session.execute(query)
            result = res.all()
            return result

    @staticmethod
    async def insert_books(reader_id: int, book_names: list):
        async with async_session_factory() as session:
            books = [Book(name=book_name) for book_name in book_names]
            session.add_all(books)
            await session.commit()

    @staticmethod
    async def select_books(user_id: int):
        async with async_session_factory() as session:
            query = (
                select(
                    Book.name)
                .select_from(Book)
                .filter(Book.reader_id == user_id)
                )
            print(query.compile(compile_kwargs={'literal_binds': True}))
            res = await session.execute(query)
            result = res.all()
            # Извлечение имен книг из результатов запроса
            book_names = [book.name for book in result]

            return book_names  # Возвращаем список имен книг

    @staticmethod
    async def update_reader(reader_id: int, **kwargs):
        async with async_session_factory() as session:
            reader = await session.get(Reader, reader_id)
            for key, value in kwargs.items():
                setattr(reader, key, value)
            await session.refresh(reader)
            await session.commit()
