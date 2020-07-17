from typing import List

from pydantic import BaseModel

from pokedex.models.basics import Name


class EncounterMethod(BaseModel):
    id: int
    name: str
    order: int
    names: List[Name]


class EncounterCondition(BaseModel):
    id: int
    name: str
    names: List[Name]
    values: List[EncounterConditionValue]


class EncounterConditionValue(BaseModel):
    id: int
    name: str
    condition: EncounterCondition
    names: List[Name]
