from luda.constants import Mission
from luda.data.catalogue import load_catalogue
from luda.dataset import Dataset


def read_db_metric(dataset_id: str) -> Dataset:
    CATALOGUE = load_catalogue()

    for category in CATALOGUE:
        for variable in category.variables:
            for metric in variable.metrics:
                if metric.slug == dataset_id:
                    return Dataset(
                        name=metric.slug,
                        data=[1, 2, 3],
                        mission=Mission(category.slug),
                    )

    raise ValueError("Metric not found")
