from fastapi import FastAPI, Depends
from database import Base, engine, get_db
from sqlalchemy.orm import Session

from models.task import Task

app = FastAPI()

# Create the tables on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root(db: Session = Depends(get_db)):
    return {"message": "Vroum vroum API"}

tasks = []

# Get all tasks
@app.get("/tasks/")
async def get_tasks():

    return { "tasks": tasks }


# Get single task
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return {"task": task}
    return {"message": "The task is not found."}


# Create a task
@app.post("/tasks/")
async def create_task(task: Task):
    tasks.append(task)

    return {"message": "Taks has been added."} 


# Update single task
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task_obj: Task):
    for task in tasks:
        if task.id == task_id:
            tasks.id = task_id
            tasks.name = task_obj.name
            tasks.description = task_obj.description

            return {"task": task}
    return {"message": "The task is not deleted."}


# Delete single task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)

            return {"message": "The task has been deleted."}
    return {"message": "The task is not deleted."}

# BOOKS
BOOKS = [
    {"id": 1, "title": "Book 1 title", "author": "Author 1", "description": "Book 1 description", "category": "math"},
    {"id": 2, "title": "Book 2 title", "author": "Author 2", "description": "Book 2 description", "category": "history"},
    {"id": 3, "title": "Book 3 title", "author": "Author 1", "description": "Book 3 description", "category": "math"},
]

@app.get("/books/")
async def get_books():

    return { "books": BOOKS }

@app.get("/books/{book_id:int}")
async def get_book_by_id(book_id: int):
    for book in BOOKS:
        if book.get("id") == book_id:
            return {"book": book}

    return {"message": "The book is not found."}

@app.get("/books/{book_title:str}")
async def get_book_by_title(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return {"book": book}

    return {"message": "The book is not found."}
