"""Models for the LUDA data catalogue."""

from pydantic import BaseModel


class Metric(BaseModel):
    """LUDA metric model."""

    slug: str


class Variable(BaseModel):
    """LUDA variable model."""

    slug: str
    metrics: list[Metric]


class Category(BaseModel):
    """LUDA category model."""

    slug: str
    variables: list[Variable]
