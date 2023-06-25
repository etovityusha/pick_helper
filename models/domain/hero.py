from pydantic import BaseModel, Field


class Hero(BaseModel):
    identity: int = Field(alias="id")
    title: str
