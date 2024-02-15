from __future__ import annotations

from enum import Enum


class Mission(Enum):
    @staticmethod
    def from_str(name: str) -> Mission:
        return Mission[name.upper()]

    def __str__(self) -> str:
        return self.name

    LIVING = "living-standards"
    RESEARCH = "research"
    TRANSPORT = "transport"
    DIGITAL = "digital"
    EDUCATION = "education"
    SKILLS = "skills"
    HEALTH = "health"
    WELLBEING = "wellbeing"
    PRIDE = "pride"
    HOUSING = "housing"
    CRIME = "crime"
    LEADERSHIP = "leadership"
