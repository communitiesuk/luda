from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.core import NotFoundError, get_db
from app.db.missions import read_db_mission
from app.lib.constants import Mission
from app.lib.data.catalogue import ContentStore
from app.lib.data.models.core import Category, Metric

router = APIRouter(
    prefix="/missions",
)


@router.get("/")
def read_root() -> list[Category]:
    """Root endpoint for the missions API."""
    store = ContentStore()
    return store.categories


@router.get("/{mission}")
def read_mission(mission: Mission, db: Session = Depends(get_db)) -> Mission:
    """List all metrics for a given mission."""
    try:
        db_mission = read_db_mission(mission, db)
    except NotFoundError as e:
        raise HTTPException(status_code=404) from e
    return Mission(**db_mission.__dict__)


@router.get("/{mission}/{dataset_id}")
def read_item(dataset_id: str) -> Metric:
    """Retrieve metric object for a given dataset id."""
    store = ContentStore()
    m = store[dataset_id]

    if m is None:
        raise HTTPException(status_code=404, detail="Metric not found")

    return m
