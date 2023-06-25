from sqlalchemy.orm import Mapped

from models.orm.base import BaseORM


class UserORM(BaseORM):
    __tablename__ = "user"

    nickname: Mapped[str]
    pass_hash: Mapped[str]
