"""Dataset model for LUDA."""

from typing import Sequence

from pydantic import BaseModel

from luda.constants import Mission


class Dataset(BaseModel):
    """LUDA dataset model."""

    name: str
    data: Sequence[float]
    mission: Mission
