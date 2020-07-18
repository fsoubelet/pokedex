from typing import List

from pydantic import BaseModel

from pokedex.models.commons import Name, NamedAPIResource


class EncounterMethod(BaseModel):
    id: int
    name: str
    order: int
    names: List[Name]


class EncounterCondition(BaseModel):
    id: int
    name: str
    names: List[Name]
    values: List[NamedAPIResource]


class EncounterConditionValue(BaseModel):
    id: int
    name: str
    condition: NamedAPIResource
    names: List[Name]
