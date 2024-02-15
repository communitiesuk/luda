from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from luda.constants import Mission

app = FastAPI()


class Dataset(BaseModel):
    name: str
    data: float
    mission: Mission


@app.get("/")
def read_root():
    return "LUDA is live."


@app.get("/datasets/{dataset_id}")
def read_item(dataset_id: str, q: Optional[str] = None):
    return {"dataset_id": dataset_id, "q": q}
