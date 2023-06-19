from services.uow import AlchemyUnitOfWork
from services.db import session_factory
from services.seeding import HeroesSeedService

uow = AlchemyUnitOfWork(session_factory("postgresql://postgres@localhost:5432/dota"))
HeroesSeedService(uow).seed()
