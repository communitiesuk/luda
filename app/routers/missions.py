from fastapi import APIRouter, HTTPException

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
def read_mission(mission: Mission) -> list[Metric]:
    """List all metrics for a given mission."""
    store = ContentStore()

    for variable in store.variables:
        if variable.slug == mission.value:
            return variable.metrics

    raise HTTPException(status_code=404, detail="Mission not found")


@router.get("/{mission}/{dataset_id}")
def read_item(dataset_id: str) -> Metric:
    """Retrieve metric object for a given dataset id."""
    store = ContentStore()
    m = store[dataset_id]

    if m is None:
        raise HTTPException(status_code=404, detail="Metric not found")

    return m
