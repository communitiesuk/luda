from typing import Optional

from sqlalchemy.orm import Session

from app.db.core import DBMetric, DBMission, NotFoundError
from app.lib.constants import Mission


def read_db_mission(mission: Mission, session: Session) -> Optional[DBMission]:
    """Reads a mission by its id."""
    db_item = session.query(DBMission).filter(DBMission.slug == mission.value).first()
    if db_item is None:
        raise NotFoundError(f"Item with id {mission.value} not found.")  # noqa: EM102
    return db_item


def read_db_metrics_for_mission(mission: Mission, session: Session) -> list[DBMetric]:
    """Reads all metrics for a mission."""
    return session.query(DBMetric).filter(DBMission.slug == mission.value).all()
