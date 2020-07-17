from typing import List

from pydantic import BaseModel

from pokedex.models.basics import Name
from pokedex.models.contests import ContestType
from pokedex.models.items import Item
from pokedex.models.pokemon import Type


class Berry(BaseModel):
    id: int
    name: str
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    size: int
    smoothness: int
    soil_dryness: int
    firmness: BerryFirmness
    flavors: List[BerryFlavorMap]
    item: Item
    natural_gift_type: Type


class BerryFlavorMap(BaseModel):
    potency: int
    flavor: BerryFlavor


class BerryFirmness(BaseModel):
    id: int
    name: str
    berries: List[Berry]
    names: List[Name]


class BerryFlavor(BaseModel):
    id: int
    name: str
    berries: List[FlavorBerryMap]
    contest_type: ContestType
    names: List[Name]


class FlavorBerryMap(BaseModel):
    potency: int
    berry: Berry
