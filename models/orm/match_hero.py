from typing import List

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from enums.position import PositionEnum
from models.orm.base import BaseORM
from models.orm.hero import HeroORM
from models.orm.match import MatchORM


class MatchHeroORM(BaseORM):
    __tablename__ = "match_hero"

    match_id: Mapped[int] = mapped_column(ForeignKey("match.id"))
    match: Mapped[HeroORM] = relationship(backref="heroes")

    hero_id: Mapped[int] = mapped_column(ForeignKey("hero.id"))
    hero: Mapped[MatchORM] = relationship(backref="matches")

    position: Mapped[PositionEnum]
    gold_m: Mapped[List[int]] = mapped_column(ARRAY(Integer))
