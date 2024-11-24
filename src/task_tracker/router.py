# для создания эндпоинтов, что-то похожее на урлы джанги и вьюшки
from fastapi import (Query, Path, Body, APIRouter, Depends)
from src.task_tracker.schemas import CreateTaskSchema, CreateCommentSchema
from src.task_tracker.service import TaskService, CommentService # в роуты уже тянем сервис с выполнением его
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.orm.database import get_async_session
from src.task_tracker.schemas import ResponseTaskSchema, ResponseCommentSchema, UpdateTaskSchema

router = APIRouter(
    prefix='/tasks', # так будет начинаться эндпоинт
    tags=['TAsks'] # название подраздела
)


# @app.get('/{item_id}/{paas_str}') так было изначально в main
@router.post(
    '',
    description='create task',
    response_model=ResponseTaskSchema,
    status_code=201
)
async def create_task_handler(
        # item_id: int=Path(), было изначально потом убрали
        # query: str|None=Query(None), было изначально потом убрали
        # item: Item = Body() убрали, изначально было вместе return
        task: CreateTaskSchema,
        session: AsyncSession = Depends(get_async_session)
):
    task_service = TaskService(session=session)
    return await task_service.create(task)
    # return item
    # return {
        # 'Hello': 'World', было изначально потом убрали
        # 'item_id': item_id, было изначально потом убрали
        # 'query': query, было изначально потом убрали
        # 'id': item.id, заменено return item
        # 'title': item.title, заменено return item
        # 'description': item.description заменено return item
    # }

@router.put(
    '/{task_id}',
    description='update task',
    response_model=UpdateTaskSchema,
    status_code=200
)
async def update_task_handler(
        task: UpdateTaskSchema,
        task_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    task_service = TaskService(session=session)
    return await task_service.update(task=task, task_id=task_id)



# @router.get(
#     '',
#     description='test demo endpoint'
# )
# def get_task_handler(
#         # item_id: int=Path(),
#         query: str|None=Query(None)
# ):
#     # from src.task_tracker.models import Tasks
#     # from src.core.orm.base import create_db_and_tables
#     # create_db_and_tables()
#     return {
#         'Hello': 'World',
#         # 'item_id': item_id,
#         'query': query
#     }
@router.get(
    '',
    description='get all task',
    status_code=200
)
async def get_tasks_handler(
        session: AsyncSession = Depends(get_async_session)
):
    task_service = TaskService(session=session)
    return await task_service.get_all()

@router.get(
    '/comment_all',
    description='get all task with comments',
    status_code=200
)
async def get_tasks_handler(
        session: AsyncSession = Depends(get_async_session)
):
    task_service = TaskService(session=session)
    return await task_service.get_all_comments()

@router.get(
    '/{task_id}/comment_all',
    description='get task with comments',
    status_code=200
)
async def get_tasks_handler(
        task_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    task_service = TaskService(session=session)
    return await task_service.get_with_comment(task_id=task_id)

@router.get(
    '/{task_id}',
    description='get task',
    response_model=ResponseTaskSchema,
    status_code=200
)
async def get_task_handler(
        task_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    task_service = TaskService(session=session)
    return await task_service.get(task_id=task_id)

@router.delete(
    '/{task_id}',
    description='delete task',
    status_code=204
)
async def delete_task_handler(
        task_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    task_service = TaskService(session=session)
    return await task_service.delete(task_id=task_id)


@router.post(
    '/comments',
    description='create comment',
    response_model=ResponseCommentSchema,
    status_code=201
)
async def create_comment_handler(
        comment: CreateCommentSchema,
        session: AsyncSession = Depends(get_async_session)
):
    comment_service =CommentService(session=session)
    return await comment_service.create(comment)