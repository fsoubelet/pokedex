from typing import List

from pydantic import BaseModel

from pokedex.models.commons import Effect, FlavorText, NamedAPIResource


class ContestName(BaseModel):
    name: str
    color: str
    language: NamedAPIResource


class ContestType(BaseModel):
    id: int
    name: str
    berry_flavor: NamedAPIResource
    names: List[ContestName]


class ContestEffect(BaseModel):
    id: int
    appeal: int
    jam: int
    effect_entries: List[Effect]
    flavor_text_entries: List[FlavorText]


class SuperContestEffect(BaseModel):
    id: int
    appeal: int
    flavor_text_entries: List[FlavorText]
    moves: List[NamedAPIResource]
