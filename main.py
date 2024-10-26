from fastapi import FastAPI
from models.task import Task

app = FastAPI()

@app.get("/")
async def root():
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


# Delete single task
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