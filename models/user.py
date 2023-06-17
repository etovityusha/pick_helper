from sqlalchemy.orm import Mapped

from models.base import BaseORM


class User(BaseORM):
    __tablename__ = "user"

    nickname: Mapped[str]
    pass_hash: Mapped[str]
