import abc

from sqlalchemy import insert
from sqlalchemy.orm import Session

from models.domain.hero import Hero
from models.orm.hero import HeroORM
from repositories.base import AlchemyGenericRepository


class HeroRepo(abc.ABC):
    @abc.abstractmethod
    def create(self, id_: int, title: str) -> None:
        pass


class AlchemyHeroRepo(HeroRepo, AlchemyGenericRepository[Hero]):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Hero, HeroORM)

    def create(self, id_: int, title: str) -> None:
        stmt = insert(self._orm_model).values({"id": id_, "title": title})
        self._session.execute(stmt)
