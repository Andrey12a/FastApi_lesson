from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.task_tracker.router import router as tasks_router
from src.auth.router import router as auth_router

app = FastAPI()
app.include_router(tasks_router)
app.include_router(auth_router)
app.mount("/", StaticFiles(directory="public", html=True))
