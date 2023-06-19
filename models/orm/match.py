from sqlalchemy.orm import Mapped, mapped_column

from enums.parsing_status import ParsingStatusEnum
from models.orm.base import BaseORM


class MatchORM(BaseORM):
    __tablename__ = "match"

    title: Mapped[str] = mapped_column(unique=True)
    parsing_status: Mapped[ParsingStatusEnum]
