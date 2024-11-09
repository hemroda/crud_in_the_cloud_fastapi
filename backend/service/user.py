from models.user import User
import data.user as data


def get_all() -> list[User]:
    return data.get_all()

def get_one(id: int) -> User | None:
    return data.get_one(id)

def create(user: User) -> User:
    return data.create(user)

def replace(id, user: User) -> User:
    return data.replace(id, user)

def modify(id, user: User) -> User:
    return data.modify(id, user)

def delete(id, user: User) -> bool:
    return data.delete(id)
