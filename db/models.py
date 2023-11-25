# Standard Library
from datetime import (
    datetime,
    timedelta,
)
from decimal import Decimal
from typing import List

# Third Party Stuff
import sqlalchemy as sa
from sqlalchemy import (
    DECIMAL,
    BigInteger,
    Boolean,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    Interval,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    """
    Base model
    Using by alembic to acces all child models
    """


class Sex(Base):
    __tablename__ = "sex"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(90))


class Athlete(Base):
    __tablename__ = "athletes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    sex_id: Mapped[int] = mapped_column(
        ForeignKey("sex.id", ondelete="SET NULL"), nullable=False
    )
    sex: Mapped[Sex] = relationship(foreign_keys=[sex_id])


class RaceClass(Base):
    __tablename__ = "race_classes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(90))
    multiplier: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=True)


class Race(Base):
    __tablename__ = "races"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(90))
    race_class_id: Mapped[int] = mapped_column(
        ForeignKey("race_classes.id", ondelete="RESTRICT"), nullable=True
    )
    race_class: Mapped[RaceClass] = relationship(
        foreign_keys=[race_class_id],
    )
    date_start: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class RaceResult(Base):
    __tablename__ = "race_results"
    id: Mapped[int] = mapped_column(primary_key=True)
    athlete_id: Mapped[int] = mapped_column(
        ForeignKey("athletes.id", ondelete="RESTRICT"), nullable=False
    )
    athlete: Mapped["Athlete"] = relationship(foreign_keys=[athlete_id])
    race_id: Mapped[int] = mapped_column(
        ForeignKey("races.id", ondelete="CASCADE"), nullable=False
    )
    race: Mapped["Race"] = relationship(foreign_keys=[race_id])
    bib_number: Mapped[str] = mapped_column(String(90))
    result_time: Mapped[timedelta] = mapped_column(Interval)
    result_place: Mapped[int] = mapped_column(Integer, nullable=True)
    result_points: Mapped[int] = mapped_column(Integer, nullable=True)

    __table_args__ = (
        UniqueConstraint("athlete_id", "race_id", name="athlete_race_uniq"),
    )


class PointsForPlace(Base):
    __tablename__ = "points_for_place"
    id: Mapped[int] = mapped_column(primary_key=True)
    place: Mapped[int] = mapped_column(Integer, nullable=False)
    points: Mapped[int] = mapped_column(Integer, nullable=False)
    sex_id: Mapped[int] = mapped_column(
        ForeignKey("sex.id", ondelete="RESTRICT"),
        nullable=True,
    )
    sex: Mapped["Sex"] = relationship(
        foreign_keys=[sex_id],
    )


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(90))


class ReplaceName(Base):
    __tablename__ = "replace_name"
    name: Mapped[str] = mapped_column(String(90), unique=True, primary_key=True)
    replace_name: Mapped[str] = mapped_column(String(90))
