from typing import List

from pydantic import BaseModel

from pokedex.models.berries import BerryFlavor
from pokedex.models.commons import Effect, FlavorText
from pokedex.models.basics import Language
from pokedex.models.moves import Move


class ContestType(BaseModel):
    id: int
    name: str
    berry_flavor: BerryFlavor
    names: List[ContestName]


class ContestName(BaseModel):
    name: str
    color: str
    language: Language


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
    moves: List[Move]
