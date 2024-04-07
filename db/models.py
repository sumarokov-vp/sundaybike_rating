# Standard Library
from datetime import (
    datetime,
    timedelta,
)
from decimal import Decimal

# Third Party Stuff
from sqlalchemy import (
    DECIMAL,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Interval,
    String,
    Table,
    UniqueConstraint,
    text as sql_alchemy_text,
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
    enabled: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=sql_alchemy_text("true")
    )


class Athlete(Base):
    __tablename__ = "athletes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    sex_id: Mapped[int] = mapped_column(
        ForeignKey("sex.id", ondelete="SET NULL"), nullable=False
    )
    sex: Mapped[Sex] = relationship(foreign_keys=[sex_id])
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="RESTRICT"),
        nullable=False,
        server_default=sql_alchemy_text("3"),
    )
    category: Mapped["Category"] = relationship(foreign_keys=[category_id])

    __table_args__ = (UniqueConstraint("name", name="name_uniq"),)


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(90), nullable=False)


class AthleteCategory(Base):
    __tablename__ = "athlete_categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=sql_alchemy_text("now()"),
    )
    start: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    end: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    athlete_id: Mapped[int] = mapped_column(
        ForeignKey("athletes.id", ondelete="CASCADE"), nullable=False
    )
    athlete: Mapped[Athlete] = relationship(foreign_keys=[athlete_id])
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="RESTRICT"), nullable=False
    )
    category: Mapped[Category] = relationship(foreign_keys=[category_id])

    __table_args__ = (UniqueConstraint("athlete_id", name="athlete_uniq"),)


class RaceClass(Base):
    __tablename__ = "race_classes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(90))
    multiplier: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=True)
    a_category_percentage: Mapped[Decimal] = mapped_column(
        DECIMAL(10, 2), nullable=True
    )


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


class CategoryResult(Base):
    __tablename__ = "category_results"
    id: Mapped[int] = mapped_column(primary_key=True)
    result_id: Mapped[int] = mapped_column(
        ForeignKey("race_results.id", ondelete="CASCADE"),
        nullable=False,
    )
    result: Mapped["RaceResult"] = relationship(foreign_keys=[result_id])
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="RESTRICT"),
        nullable=False,
    )
    category: Mapped["Category"] = relationship(foreign_keys=[category_id])
    place: Mapped[int] = mapped_column(Integer, nullable=True)
    points: Mapped[int] = mapped_column(Integer, nullable=True)


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
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(90), unique=True, primary_key=True)
    replace_name: Mapped[str] = mapped_column(String(90))


class SeasonReport(Base):
    metadata = Base.metadata
    season_points_view = Table(
        "season_points",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("season", Integer),
        Column("sex_id", Integer, ForeignKey("sex.id")),
        Column("category_id", Integer, ForeignKey("categories.id")),
        Column("athlete_id", Integer, ForeignKey("athletes.id")),
        Column("rank", Integer),
        Column("points", Integer),
    )

    __table__ = season_points_view
    id = season_points_view.c.id
    sex_id = season_points_view.c.sex_id
    sex: Mapped["Sex"] = relationship(foreign_keys=[sex_id])
    season = season_points_view.c.season
    category_id = season_points_view.c.category_id
    category: Mapped["Category"] = relationship(
        foreign_keys=[season_points_view.c.category_id]
    )
    athlete_id = season_points_view.c.athlete_id
    athlete: Mapped["Athlete"] = relationship(
        foreign_keys=[season_points_view.c.athlete_id]
    )
    rank = season_points_view.c.rank
    points = season_points_view.c.points


class RaceReport(Base):
    race_points_view = Table(
        "race_points",
        Base.metadata,
        Column("id", Integer, primary_key=True),
        Column("season", Integer),
        Column("sex_id", Integer, ForeignKey("sex.id")),
        Column("category_id", Integer, ForeignKey("categories.id")),
        Column("athlete_id", Integer, ForeignKey("athletes.id")),
        Column("race_id", Integer, ForeignKey("races.id")),
        Column("race_rank", Integer),
        Column("race_points", Integer),
        Column("result_time", Interval),
    )

    __table__ = race_points_view
    id = race_points_view.c.id
    sex_id = race_points_view.c.sex_id
    sex: Mapped["Sex"] = relationship(foreign_keys=[sex_id])
    season = race_points_view.c.season
    category_id = race_points_view.c.category_id
    category: Mapped["Category"] = relationship(
        foreign_keys=[race_points_view.c.category_id]
    )
    athlete_id = race_points_view.c.athlete_id
    athlete: Mapped["Athlete"] = relationship(
        foreign_keys=[race_points_view.c.athlete_id]
    )
    race_id = race_points_view.c.race_id
    race: Mapped["Race"] = relationship(
        foreign_keys=[race_id],
    )
    rank = race_points_view.c.race_rank
    points = race_points_view.c.race_points
    result_time = race_points_view.c.result_time
