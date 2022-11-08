from fastapi import FastAPI
from app.ToDo.tasks import main as task_main

app = FastAPI()


app.include_router(task_main.router)