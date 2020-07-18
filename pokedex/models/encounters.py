from typing import Dict, List

from pydantic import BaseModel

from pokedex.models import basics


class EncounterMethod(BaseModel):
    id: int
    name: str
    order: int
    names: List[basics.Name]


class EncounterCondition(BaseModel):
    id: int
    name: str
    names: List[basics.Name]
    values: List[Dict]


class EncounterConditionValue(BaseModel):
    id: int
    name: str
    condition: EncounterCondition
    names: List[basics.Name]
