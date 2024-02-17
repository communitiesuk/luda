from fastapi import APIRouter, HTTPException

from app.lib.constants import Mission
from app.lib.data.catalogue import ContentStore
from app.lib.data.models.core import Category, Metric

router = APIRouter(
    prefix="/missions",
)


@router.get("/")
def read_root() -> list[Category]:
    store = ContentStore()
    return store.categories


@router.get("/{mission}")
def read_mission(mission: Mission) -> list[Metric]:
    store = ContentStore()

    for variable in store.variables:
        if variable.slug == mission.value:
            return variable.metrics

    raise HTTPException(status_code=404, detail="Mission not found")


@router.get("/{mission}/{dataset_id}")
def read_item(mission: Mission, dataset_id: str) -> Metric:
    store = ContentStore()
    m = store[dataset_id]

    if m is None:
        raise HTTPException(status_code=404, detail="Metric not found")

    return m
