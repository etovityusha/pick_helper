from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, Type

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.types import DomainModel, ORMModel


class GenericRepository(Generic[DomainModel], ABC):
    @abstractmethod
    def get_by_id(self, id_: int) -> DomainModel | None:
        raise NotImplementedError()


class AlchemyGenericRepository(GenericRepository[DomainModel]):
    def __init__(self, session: Session, domain_model: DomainModel, orm_model: ORMModel) -> None:
        self._session = session
        self._domain_model = domain_model
        self._orm_model = orm_model

    def _construct_get_stmt(self, id_: int):
        return select(self._orm_model).where(self._orm_model.id == id_)

    def get_by_id(self, id_: int) -> DomainModel | None:
        stmt = self._construct_get_stmt(id_)
        return self._domain_model.from_orm(self._session.execute(stmt).first())
