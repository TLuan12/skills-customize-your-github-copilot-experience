from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


tasks = [
    {"id": 1, "title": "Write code", "description": "Finish the assignment", "done": False},
    {"id": 2, "title": "Review notes", "description": "Check lesson summary", "done": True},
]


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    done: bool = False


class Task(TaskCreate):
    id: int


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


# TODO: Add GET /tasks
# TODO: Add POST /tasks
# TODO: Add GET /tasks/{task_id}
# TODO: Add PUT /tasks/{task_id}
# TODO: Add DELETE /tasks/{task_id}
