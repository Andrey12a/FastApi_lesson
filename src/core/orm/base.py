# базовые команды для создания таблиц
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from src.core.orm.database import sync_engine
# from sqlalchemy.orm import DeclarativeBase


Base: DeclarativeMeta = declarative_base()
# class Base(DeclarativeBase):
#     ...


def create_db_and_tables():
    Base.metadata.create_all(sync_engine)