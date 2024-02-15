"""Catalogue of datasets available for use in the LUDA system."""

from luda.constants import Mission
from luda.dataset import Dataset

CATALOGUE = [
    Dataset(name="data-001", data=[1, 2, 3], mission=Mission.DIGITAL),
    Dataset(name="data-002", data=[4, 5, 6], mission=Mission.LEADERSHIP),
    Dataset(name="data-003", data=[7, 8, 9], mission=Mission.TRANSPORT),
    Dataset(name="data-004", data=[3, 6, 9], mission=Mission.DIGITAL),
]
