from pydantic import BaseModel


class BaseConfig(BaseModel):
    class Config:
        orm_mode = True

class User(BaseConfig):
    id: int
    username: str
    email: str
