from fastapi import APIRouter, HTTPException

from app.db import read_db_metric
from luda.constants import Mission
from luda.data import CATALOGUE
from luda.dataset import Dataset

router = APIRouter(
    prefix="/missions",
)


@router.get("/")
def read_root() -> list[Dataset]:
    return CATALOGUE


@router.get("/{mission}")
def read_mission(mission: Mission) -> list[Dataset]:
    return [dataset for dataset in CATALOGUE if dataset.mission == mission]


@router.get("/{mission}/{dataset_id}")
def read_item(mission: Mission, dataset_id: str) -> Dataset:
    dataset = read_db_metric(dataset_id)
    if dataset.mission != mission:
        raise HTTPException(status_code=404, detail="Item not found")

    return dataset
