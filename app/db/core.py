from typing import Any, Generator

from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

DATABASE_URL = "sqlite:///data/test.db"


class NotFoundError(Exception):
    """Raised when an item is not found in the database."""


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


def get_db() -> Generator[Session, Any, None]:
    """Get a database session."""
    database = session_local()
    try:
        yield database
    finally:
        database.close()
