import json

from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

from app.lib.constants import Mission

DATABASE_URL = "sqlite:///app/data/test.db"


class Base(DeclarativeBase):
    """Base class for all database models."""


class DBMission(Base):
    """Database model for LUDA mission."""

    __tablename__ = "missions"

    slug: Mapped[str] = mapped_column(primary_key=True, index=True)


class DBMetric(Base):
    """Database model for LUDA metrics."""

    __tablename__ = "metrics"

    slug: Mapped[str] = mapped_column(primary_key=True)
    mission: Mapped[str] = mapped_column(ForeignKey("missions.slug"))


engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def populate_db(session: Session) -> None:
    """Populate the database with some initial data."""
    for m in Mission.__members__.values():
        if session.query(DBMission).filter_by(slug=m.value).first() is None:
            session.add(DBMission(slug=m.value))

    session.commit()


def get_db_mission(session: Session, slug: str) -> DBMission:
    """Query the database for a user by their username."""
    u = session.query(DBMission).filter_by(slug=slug).first()
    if u is None:
        raise ValueError(f"Mission with slug {slug} not found.")  # noqa: EM102
    return u


def get_all_missions(session: Session) -> list[DBMission]:
    """Query the database for all users."""
    return session.query(DBMission).all()


def main() -> None:
    """Seed the database with some initial data."""
    session = session_local()
    populate_db(session)

    all_users = get_all_missions(session)
    print(  # noqa: T201
        json.dumps([u.__dict__ for u in all_users], indent=4, default=str)
    )

    example = get_db_mission(session, "living-standards")
    print(json.dumps(example.__dict__, indent=4, default=str))  # noqa: T201

    session.close()


if __name__ == "__main__":
    main()
