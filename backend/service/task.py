from models.task import Task
import data.task as data


def get_all() -> list[Task]:
    return data.get_all()

def get_one(id: int) -> Task | None:
    return data.get_one(id)

def get_one_by_name(name: str) -> Task | None:
    return data.get_one_by_name(name)

def create(task: Task) -> Task:
    return data.create(task)

def replace(id, task: Task) -> Task:
    return data.replace(id, task)

def modify(id, task: Task) -> Task:
    return data.modify(id, task)

def delete(id, task: Task) -> bool:
    return data.delete(id)