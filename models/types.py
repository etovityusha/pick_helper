from typing import TypeVar

from pydantic import BaseModel

from models.orm import BaseORM

DomainModel = TypeVar("DomainModel", bound=BaseModel)
ORMModel = TypeVar("ORMModel", bound=BaseORM)
