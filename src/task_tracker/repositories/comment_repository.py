# взаимодействие с бд
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from src.task_tracker.schemas import CreateCommentSchema, ResponseTaskSchema
from src.task_tracker.models import Comment
from sqlalchemy import select


class CommentRepository():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_comment(self, comment_data: CreateCommentSchema) -> Comment:
        comment = Comment( # модель задач и берем из схемы str ниже 3 строки
            comment = comment_data.comment,
            rating = comment_data.rating,
            task_id = comment_data.task_id # получаем передаем задачу вместо фронта, а так это задача фонта передать
        ) # заготовка для создания задачи
        self.session.add(comment)
        await self.session.commit()
        await self.session.refresh(comment)

        return comment
# ниже заготовка получения задачи
    async def get_comment(self, comment_id: int) -> Comment:
        query = select(Comment).where(Comment.id == comment_id)
        result = await self.session.execute(query) # execute объект курсора
        return result.scalar_one_or_none()

    async def get_comments(self) -> list[dict[str, Any]]:
        query = select(Comment)
        result = await self.session.execute(query)
        return [
            comment.__dict__ for comment in
            result.scalars().all()
        ]

    async def delete_by_id(self, comment_id: int) -> Comment:
        query = select(Comment).where(Comment.id == comment_id)
        result = await self.session.execute(query)
        comment = result.scalar_one_or_none()
        await self.session.delete(comment)
        await self.session.commit()
        return comment