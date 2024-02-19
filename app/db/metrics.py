from sqlalchemy.orm import Session

from app.db.core import DBMetric, NotFoundError


def read_db_metric(slug: str, session: Session) -> DBMetric:
    """Reads a metric by its id."""
    db_metric = session.query(DBMetric).filter(DBMetric.slug == slug).first()
    if db_metric is None:
        raise NotFoundError(f"Metric with id {slug} not found.")  # noqa: EM102
    return db_metric
