from pydantic import BaseModel


class Creature(BaseModel):
    name: str
    country: str
    description: str
    area: str
    aka: str
