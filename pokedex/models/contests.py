from typing import List

from pydantic import BaseModel

from pokedex.models import basics
from pokedex.models import berries
from pokedex.models import commons
from pokedex.models import moves


class ContestType(BaseModel):
    id: int
    name: str
    berry_flavor: berries.BerryFlavor
    names: List[ContestName]


class ContestName(BaseModel):
    name: str
    color: str
    language: basics.Language


class ContestEffect(BaseModel):
    id: int
    appeal: int
    jam: int
    effect_entries: List[commons.Effect]
    flavor_text_entries: List[commons.FlavorText]


class SuperContestEffect(BaseModel):
    id: int
    appeal: int
    flavor_text_entries: List[commons.FlavorText]
    moves: List[moves.Move]
