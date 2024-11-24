# взаимодействие с бд
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from src.task_tracker.schemas import CreateTaskSchema, ResponseTaskSchema, UpdateTaskSchema
from src.task_tracker.models import Tasks, Comment
from sqlalchemy import select
from sqlalchemy.orm import selectinload


class TaskRepository():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_task(self, task_data: CreateTaskSchema) -> Tasks:
        task = Tasks( # модель задач и берем из схемы str ниже 3 строки
            title = task_data.title,
            description = task_data.description,
            status = task_data.status
        ) # заготовка для создания задачи
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)

        return task
# ниже заготовка получения задачи
    async def get_task(self, task_id: int) -> Tasks | None:
        query = select(Tasks).where(Tasks.id == task_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_task_comment(self, task_id: int) -> Tasks | None:
        query = (select(Tasks)
                 .options(selectinload(Tasks.comments))
                 .where(Tasks.id == task_id)
                 )
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_tasks(self) -> list[dict[str, Any]]:
        query = select(Tasks)
        result = await self.session.execute(query)
        return [
            task.__dict__ for task in
            result.scalars().all()
        ]

    # async def get_task_with_comments(self) -> ResponseTaskSchema:
    async def get_task_with_comments(self):
        query = select(Tasks).options(selectinload(Tasks.comments))
        result = await self.session.execute(query)
        data = result.scalars().all()
        return data

    async def update_by_id(self, task_data: UpdateTaskSchema, task_id: int):
        query = select(Tasks).where(Tasks.id == task_id)
        result = await self.session.execute(query)
        task = result.scalar_one_or_none()
        task.title = task_data.title
        task.description = task_data.description
        task.status = task_data.status
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def delete_by_id(self, task_id: int) -> Tasks:
        query = select(Tasks).where(Tasks.id == task_id)
        result = await self.session.execute(query)
        task = result.scalar_one_or_none()
        await self.session.delete(task)
        await self.session.commit()
        return task

    # async def update_by_id(self, task_id: int) -> Tasks:
    #     query = select(Tasks).where(Tasks.id == task_id)
    #     result = await self.session.execute(query)
    #     task = result.scalar_one_or_none()
    #     await self.session.upd_(task)
    #     await self.session.commit()
    #     return task