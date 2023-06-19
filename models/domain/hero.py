from pydantic import BaseModel


class Hero(BaseModel):
    id: int
    title: str
