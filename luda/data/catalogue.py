"""Catalogue of datasets available for use in the LUDA system."""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from luda.data import models


@dataclass
class ContentStore:
    """Catalogue of datasets available for use in LUDA."""

    categories: list[models.Category] = field(init=False)

    def __post_init__(self) -> None:
        with open(Path.cwd() / "data" / "datasets.json", encoding="utf8") as file:
            data = json.load(file)
            self.categories = [models.Category(**c) for c in data]

    @property
    def variables(self) -> list[models.Variable]:
        return [v for c in self.categories for v in c.variables]

    @property
    def metrics(self) -> list[models.Metric]:
        return [m for c in self.categories for v in c.variables for m in v.metrics]

    def __getitem__(self, slug: str) -> Optional[models.Metric]:
        for metric in self.metrics:
            if metric.slug == slug:
                return metric

        return None

    def __str__(self) -> str:
        slugs = [c.slug for c in self.categories]
        return f"{self.__class__.__name__}({', '.join(slugs)})"
