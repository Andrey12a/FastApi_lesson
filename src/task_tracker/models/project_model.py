from src.core.orm.base import Base
from datetime import datetime
from sqlalchemy import DateTime, String, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated: Mapped[datetime] = mapped_column(DateTime, nullable=True)