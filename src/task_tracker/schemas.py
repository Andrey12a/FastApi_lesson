# создание схем пайдэнтик модель
from pydantic import BaseModel
from datetime import datetime


# class Item(BaseModel): # схема для валидации
#     id: int
#     title: str
#     description: str

class BaseCommentsSchema(BaseModel):
    comment: str
    rating: int | None = None

class CreateCommentSchema(BaseCommentsSchema):
    task_id: int

class ResponseCommentSchema(BaseCommentsSchema):
    id: int
    created: datetime
    updated: datetime | None = None


class BaseTasksSchema(BaseModel):
    title: str
    description: str
    status: str

class CreateTaskSchema(BaseTasksSchema):
    ...

class ResponseTaskSchema(BaseTasksSchema):
    id: int
    created: datetime
    updated: datetime | None = None
    comments: list[ResponseCommentSchema] | None = None

class UpdateTaskSchema(BaseTasksSchema):
    ...
