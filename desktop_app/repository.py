from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

"""
2. Создать подключение к базе данных
Выполнить импорт модуля с Python DB-API для реализации взаимодействия с СУБД SQLite.
Создать подключение к базе данных, путь к которой записан в переменную db_path.
Создать объект-курсор для выполнения операций с данными.
"""

PATH_DB = 'database.sqlite3'


class Repository:
    def __init__(self, path_db):
        self.engine = create_engine(f'sqlite:///{path_db}?check_same_thread=False')
        self.create_base()
        self.session = self.get_session()

    def create_base(self):
        base = declarative_base()
        base.metadata.create_all(self.engine)

    def get_session(self):
        session = sessionmaker(bind=self.engine)
        session = session()
        return session


if __name__ == '__main__':
    REP = Repository(PATH_DB)
