from .init import conn, curs
from models.task import Task


curs.execute("CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY, name TEXT, description TEXT)")


def row_to_model(row: tuple) -> Task:
    id, name, description = row

    return Task(id=id, name=name, description=description)

def model_to_dict(task: Task) -> dict:
    
    return task.dict() if task else None

def get_all() -> list[Task]:
    """ Return all tasks """
    qry = "SELECT * FROM task"
    curs.execute(qry)
    rows = list(curs.fetchall())

    return [row_to_model(row) for row in rows]

def get_one(id: int) -> Task:
    qry = "SELECT * FROM task WHERE id=:id"
    params = {"id": id}
    curs.execute(qry, params)
    row = curs.fetchone()
    print(row)
    
    return row_to_model(row)

def get_one_by_name(name: str) -> Task:
    qry = "SELECT * FROM task WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    
    return row_to_model(row)

def create(task: Task):
    """Add a task"""
    qry = "INSERT INTO task (name, description) VALUES (:name, :description)"
    params = model_to_dict(task)
    curs.execute(qry, params)
    return get_one(task.id)

def modify(task: Task) -> Task:
    """Partially modify a task"""
    qry = """UPDATE task SET task=:task, name=:name, description=:description WHERE id=:id"""
    params = model_to_dict(task)
    _ = curs.execute(qry, params)
    return get_one(task.id)

def replace(task: Task) -> Task:
    """Completely replace a task"""
    return task

def delete(task: Task):
    """Delete a task; return None if it existed"""
    qry = "delete FROM task WHERE id = :id"
    params = {"id": task.id}
    res = curs.execute(qry, params)
    return bool(res)
