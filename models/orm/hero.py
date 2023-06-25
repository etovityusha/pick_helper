from sqlalchemy.orm import Mapped

from models.orm.base import BaseORM


class HeroORM(BaseORM):
    __tablename__ = "hero"

    title: Mapped[str]
