from pydantic import BaseModel


class User(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Task(BaseModel):
    body: str
    is_active: bool

    class Config:
        orm_mode = True
