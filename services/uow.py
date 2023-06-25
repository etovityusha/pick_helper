import abc
from collections.abc import Callable
from types import TracebackType

from sqlalchemy.orm import Session

from repositories.hero_repo import AlchemyHeroRepo, HeroRepo


class UnitOfWork(abc.ABC):
    hero_repo: HeroRepo

    def __enter__(self) -> "UnitOfWork":
        return self

    def __exit__(self, exc_type: type[BaseException], exc_value: BaseException, traceback: TracebackType) -> None:
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

    def __enter__(self) -> "UnitOfWork":
        self._session = self._session_factory()
        self.hero_repo: HeroRepo = AlchemyHeroRepo(self._session)
        return super().__enter__()

    def commit(self) -> None:
        self._session.commit()

    def rollback(self) -> None:
        self._session.rollback()
