from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
# from .models import Reader, Book
from bot.config_data.config_reader import Config, load_config


class CreateDatabase():
    ''' Инициализируем движок базы данных '''
    def __init__(self, *args, **kwargs):
        self.metadata = MetaData()
        self.config: Config = load_config()
        self.engine = create_engine(self.config.database_url, echo=True)

    def create_session(self, *args, **kwargs):
        self.Session = sessionmaker(bind=self.engine)
        self.Session.configure(bind=self.engine)
        self.session = self.Session()
        return self.session

    def create_tables(self, *args, **kwargs):
        try:
            self.metadata.create_all(self.engine)
        except Exception as e:
            # Обработка исключения при создании таблиц
            print(f"Ошибка при создании таблиц: {e}")
