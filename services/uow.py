import abc
from typing import Callable

from sqlalchemy.orm import Session

from models.domain.hero import Hero
from models.orm import HeroORM
from repositories.hero_repo import HeroRepo, AlchemyHeroRepo


class UnitOfWork(abc.ABC):
    hero_repo: HeroRepo

    def __enter__(self) -> "UnitOfWork":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.rollback()

    @abc.abstractmethod
    def commit(self) -> None:
        pass

    @abc.abstractmethod
    def rollback(self) -> None:
        pass


class AlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory: Callable[[], Session]) -> None:
        self._session_factory = session_factory

    def __enter__(self):
        self._session = self._session_factory()
        self.hero_repo = AlchemyHeroRepo(self._session, domain_model=Hero, orm_model=HeroORM)
        return super().__enter__()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
