from src.core.orm.base import Base
from datetime import datetime
from sqlalchemy import DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Comment(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, unique=True)
    comment: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=True)
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    task: Mapped['Tasks'] = relationship(
        argument='Tasks',
        back_populates='comments'
    )
    task_id: Mapped[int] = mapped_column(ForeignKey('tasks.id'))