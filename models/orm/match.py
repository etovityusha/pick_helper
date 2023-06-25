from sqlalchemy.orm import Mapped, mapped_column

from enums.parsing_status import ParsingStatusEnum
from enums.team import FactionEnum
from models.orm.base import BaseORM


class MatchORM(BaseORM):
    __tablename__ = "match"

    title: Mapped[str] = mapped_column(unique=True)
    winner_faction: Mapped[FactionEnum]
    parsing_status: Mapped[ParsingStatusEnum]
