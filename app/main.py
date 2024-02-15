from typing import Optional

from fastapi import FastAPI

from luda.data import CATALOGUE
from luda.dataset import Dataset

app = FastAPI()


@app.get("/")
def read_root():
    return "LUDA is live."


@app.get("/datasets/{id}")
def get_dataset(id: str) -> Optional[Dataset]:
    return CATALOGUE.get(id)
