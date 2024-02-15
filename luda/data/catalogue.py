"""Catalogue of datasets available for use in the LUDA system."""

import json

from luda.data.models.core import Category


def load_catalogue() -> list[Category]:
    with open("data/datasets.json", encoding="utf-8") as file:
        payload = json.load(file)
        return [Category(**c) for c in payload]
