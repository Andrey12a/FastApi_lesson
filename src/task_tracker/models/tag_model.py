from src.core.orm.base import Base
from datetime import datetime
from sqlalchemy import DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TaskTag(Base):
    __tablename__ = 'task_tags'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, unique=True)
    task_id: Mapped[int] = mapped_column(ForeignKey('tasks.id'))
    tag_id: Mapped[int] = mapped_column(ForeignKey('tags.id'))
    task: Mapped[list['Tasks']] = relationship( # эту часть кода сразу написали закомментили
        argument='Tasks',
        back_populates='tags_list' # потом раскоментили когда были ошибки
    )

    tag: Mapped[list['Tag']] = relationship( # этот так же как и верхний кусок кода
        argument='Tag',
        back_populates='tasks_list'
    )


class Tag(Base):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    # tasks: Mapped['Tasks'] = relationship(
    #     argument='Tasks', коментили когда были ошибки в последний момент, после удаления каскадом
    #     secondary= 'TaskTag',
    #     back_populates='tags'
    # )
    tasks_list: Mapped['Tag'] = relationship(
        argument='TaskTag',
        back_populates='tag',
        lazy='selectin' # подгружает связанную таблицу task_tags, будет оптимизировать запросы
    )