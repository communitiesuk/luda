"""Constant definitions for LUDA."""

from __future__ import annotations

from enum import Enum


class Mission(Enum):
    """The 12 Levelling Up Missions."""

    @staticmethod
    def from_str(name: str) -> Mission:
        return Mission[name.upper()]

    def __str__(self) -> str:
        return self.name

    LIVING_STANDARDS = "living-standards"
    RESEARCH_AND_DEVELOPMENT = "research-and-development"
    TRANSPORT = "transport"
    DIGITAL_CONNECTIVITY = "digital-connectivity"
    EDUCATION = "education"
    SKILLS = "skills"
    HEALTH = "health"
    WELLBEING = "wellbeing"
    PRIDE_IN_PLACE = "pride-in-place"
    HOUSING = "housing"
    CRIME = "crime"
    LOCAL_LEADERSHIP = "local-leadership"
