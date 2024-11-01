from fastapi import APIRouter

from models.task import Task

router = APIRouter(prefix = "/tasks")

TASKS = [
    {"id": 1, "title": "Task 1 title", "owner": "Owner 1", "description": "Task 1 description", "category": "math"},
    {"id": 2, "title": "Task 2 title", "owner": "Owner 2", "description": "Task 2 description", "category": "history"},
    {"id": 3, "title": "Task 3 title", "owner": "Owner 1", "description": "Task 3 description", "category": "math"},
]

# Get all tasks
@router.get("/")
async def get_tasks():

    return { "tasks": TASKS }


# Get single task
@router.get("/{task_id}")
async def get_task(task_id: int):
    for task in TASKS:
        print(task)
        if task.get("id") == task_id:

            return {"task": task}

    return {"message": "The task is not found."}


# Create a task
@router.post("/")
async def create_task(task: Task):
    TASKS.append(task)

    return {"message": "Taks has been added."} 


# Update single task
@router.put("/{task_id}")
async def update_task(task_id: int, task_obj: Task):
    for task in TASKS:
        if task.get("id") == task_id:
            task.id = task_id
            task.name = task_obj.name
            task.description = task_obj.description

            return {"task": task}

    return {"message": "The task is not deleted."}


# Delete single task
@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in TASKS:
        if task.id == task_id:
            TASKS.remove(task)

            return {"message": "The task has been deleted."}

    return {"message": "The task is not deleted."}