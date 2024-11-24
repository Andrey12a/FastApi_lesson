# сервисный слой для взаимодействия интерфейса и базы данных
# и обработки взаимодействия возможных ошибок
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from src.task_tracker.repositories.task_repository import TaskRepository # тут создаем и получаем задачу
from src.task_tracker.repositories.comment_repository import CommentRepository # тут создаем и получаем задачу
from src.task_tracker.schemas import CreateTaskSchema, CreateCommentSchema, UpdateTaskSchema, ResponseTaskSchema
from src.task_tracker.models import Tasks, Comment


class TaskService():
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = TaskRepository(session=session) # создает либо отдает задачу на основе модуля repository

    async def create(self, task: CreateTaskSchema) -> Tasks:
        return await self.repository.create_task(task_data=task) # это репозиторий с методом создать задачу и со схемой внутри
# в репозитории подготовили тут, выполнили создать и получить задачу
    async def get(self, task_id: int) -> Tasks | None:
        return await self.repository.get_task(task_id=task_id) # а тут выполнили, получили задачу

    async def get_with_comment(self, task_id: int) -> Tasks | None:
        return await self.repository.get_task_comment(task_id=task_id)

    async def get_all(self) -> list[dict[str, Any]]:
        return await self.repository.get_tasks()

    # async def get_all_comments(self) -> ResponseTaskSchema:
    async def get_all_comments(self):
        return await self.repository.get_task_with_comments()

    async def update(self, task_id: int, task: UpdateTaskSchema):
        return await self.repository.update_by_id(task_data=task, task_id=task_id)

    async def delete(self, task_id: int) -> Tasks | None:
        return await self.repository.delete_by_id(task_id=task_id)


class CommentService():
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = CommentRepository(session=session) # создает либо отдает задачу на основе модуля repository

    async def create(self, comment: CreateCommentSchema) -> Comment:
        return await self.repository.create_comment(comment_data=comment) # это репозиторий с методом создать задачу и со схемой внутри
# в репозитории подготовили тут, выполнили создать и получить задачу
    async def get(self, comment_id: int) -> Comment | None:
        return await self.repository.get_comment(comment_id=comment_id) # а тут выполнили, получили задачу

    async def get_all(self) -> list[dict[str, Any]]:
        return await self.repository.get_comments()

    async def delete(self, comment_id: int) -> Comment | None:
        return await self.repository.delete_by_id(comment_id=comment_id)
