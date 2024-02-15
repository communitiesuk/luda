from luda.data import CATALOGUE
from luda.dataset import Dataset


def read_db_metric(dataset_id: str) -> Dataset:
    for dataset in CATALOGUE:
        if dataset.name == dataset_id:
            return dataset

    raise ValueError("Metric not found")
