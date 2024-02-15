"""Catalogue of datasets available for use in the LUDA system."""

from luda.constants import Mission
from luda.dataset import Dataset

CATALOGUE = {
    "data-001": Dataset(name="data-001", data=[1, 2, 3], mission=Mission.DIGITAL),
    "data-002": Dataset(name="data-002", data=[4, 5, 6], mission=Mission.LEADERSHIP),
    "data-003": Dataset(name="data-003", data=[7, 8, 9], mission=Mission.TRANSPORT),
}
