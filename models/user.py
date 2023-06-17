from sqlalchemy.orm import Mapped

from models.base import BaseORM


class User(BaseORM):
    __tablename__ = "user"

    nickname: Mapped[str | None]
    pass_hash: Mapped[str | None]
