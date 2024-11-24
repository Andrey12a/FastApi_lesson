from src.core.orm.base import Base
from datetime import datetime
from sqlalchemy import DateTime, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.const import TaskStatuses


class Tasks(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    status: Mapped[TaskStatuses] = mapped_column(String, nullable=False, default=TaskStatuses.new)
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    comments: Mapped[list['Comment']] = relationship(
        argument='Comment',
        back_populates='task',
        lazy='selectin' # продолжение коммента
    )
    tags_list: Mapped[list['Tag']] = relationship(
        argument='TaskTag',
        # secondary='TaskTag', узнать про ошибку и подробнее как работают связи таблиц в фасте
        back_populates='task',
        lazy='selectin' # продолжение, похоже на оптимизацию из джанги, и в джанге разобрать это более детально(напоминание!)
    )