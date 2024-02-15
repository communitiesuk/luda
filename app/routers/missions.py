from fastapi import APIRouter, HTTPException

from app.db import read_db_metric
from luda.constants import Mission
from luda.data.catalogue import load_catalogue
from luda.data.models.core import Category, Metric
from luda.dataset import Dataset

router = APIRouter(
    prefix="/missions",
)


@router.get("/")
def read_root() -> list[Category]:
    return load_catalogue()


@router.get("/{mission}")
def read_mission(mission: Mission) -> list[Metric]:
    CATALOGUE = load_catalogue()
    return [
        Metric(slug=metric.slug)
        for category in CATALOGUE
        if category.slug == mission
        for variable in category.variables
        for metric in variable.metrics
    ]


@router.get("/{mission}/{dataset_id}")
def read_item(mission: Mission, dataset_id: str) -> Dataset:
    dataset = read_db_metric(dataset_id)
    if dataset.mission != mission:
        raise HTTPException(status_code=404, detail="Item not found")

    return dataset
