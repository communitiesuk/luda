from typing import Sequence

from pydantic import BaseModel

from luda.constants import Mission


class Dataset(BaseModel):
    name: str
    data: Sequence[float]
    mission: Mission
