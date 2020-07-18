from typing import List

from pydantic import BaseModel

from pokedex.models import basics
from pokedex.models import contests
from pokedex.models import items
from pokedex.models import pokemon


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
    item: items.Item
    natural_gift_type: pokemon.Type


class FlavorBerryMap(BaseModel):
    potency: int
    berry: Berry


class BerryFlavorMap(BaseModel):
    potency: int
    flavor: BerryFlavor


class BerryFirmness(BaseModel):
    id: int
    name: str
    berries: List[Berry]
    names: List[basics.Name]


class BerryFlavor(BaseModel):
    id: int
    name: str
    berries: List[FlavorBerryMap]
    contest_type: contests.ContestType
    names: List[basics.Name]
