from models.task import Task


_tasks = [
    Task(id=1,
        name="Learn Python",
        description="Master vanilla Python up to OOP."
        ),
    Task(id=2,
        name="Learn FastAPI",
        description="Leearn to create robust APIs."
        ),
    ]


def get_all() -> list[Task]:
    """ Return all tasks """
    return _tasks

def get_one(id: int) -> Task | None:
    for _task in _tasks:
        if _task.id == int(id):
            return _task
    return None

def get_one_by_name(name: str) -> Task | None:
    for _task in _tasks:
        if _task.name == name:
            return _task
    return None

def create(task: Task) -> Task:
    """Add a task"""
    return task

def modify(task: Task) -> Task:
    """Partially modify a task"""
    return task

def replace(task: Task) -> Task:
    """Completely replace a task"""
    return task

def delete(name: str) -> bool:
    """Delete a task; return None if it existed"""
    return None
