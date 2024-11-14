# from fastapi import APIRouter, Depends, HTTPException

# from models.task import Task
# import data.task as service

# router = APIRouter(prefix = "/tasks")

# @router.get("/", response_model=list[Task])
# def get_all(session: Session = Depends(get_session)) -> list[Task]:
#     return service.get_all(session)

# @router.get("/{task_id}", response_model=Task)
# def get_one(task_id: int, session: Session = Depends(get_session)) -> Task:
#     """Endpoint to get a task by its ID."""
#     task = service.get_one(task_id, session)
#     if task is None:
#         raise HTTPException(status_code=404, detail="Task not found.")
#     return task

# @router.post("/", response_model=Task)
# def create(task: Task, session: Session = Depends(get_session)) -> Task:
#     return service.create(task, session)

# @router.patch("/{task_id}", response_model=Task)
# def modify(task_id: int, task_data: Task, session: Session = Depends(get_session)) -> Task:
#     """Endpoint to partially update a task."""
#     updated_task = service.modify(task_id, task_data, session)
#     if updated_task is None:
#         raise HTTPException(status_code=404, detail="Task not found.")
#     return updated_task

# @router.put("/")
# def replace(task: Task) -> Task:
#     return service.replace(task)

# @router.delete("/{task_id}")
# def delete(task_id: int, session: Session = Depends(get_session)) -> dict:
#     task = session.get(Task, task_id)

#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found.")

#     service.delete(task_id, session)

#     return {"detail": "Task deleted successfully"}
