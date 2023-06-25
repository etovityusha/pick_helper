import abc

import httpx

from services.uow import UnitOfWork


class SeedService(abc.ABC):
    @abc.abstractmethod
    def seed(self) -> None:
        pass


class HeroesSeedService(SeedService):
    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow
        self.url = "https://api.opendota.com/api/heroes"

    def seed(self) -> None:
        client = httpx.Client()
        response = client.get(url=self.url)
        with self._uow as uow:
            for row in response.json():
                uow.hero_repo.create(id_=row["id"], title=row["localized_name"])
            uow.commit()
