from typing import List

from pydantic import BaseModel

from pokedex.models.commons import Name, NamedAPIResource


class BerryFlavorMap(BaseModel):
    potency: int
    flavor: NamedAPIResource


class Berry(BaseModel):
    id: int
    name: str
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    size: int
    smoothness: int
    soil_dryness: int
    firmness: NamedAPIResource
    flavors: List[BerryFlavorMap]
    item: NamedAPIResource
    natural_gift_type: NamedAPIResource


class BerryFirmness(BaseModel):
    id: int
    name: str
    berries: List[NamedAPIResource]
    names: List[Name]


class FlavorBerryMap(BaseModel):
    potency: int
    berry: NamedAPIResource


class BerryFlavor(BaseModel):
    id: int
    name: str
    berries: List[FlavorBerryMap]
    contest_type: NamedAPIResource
    names: List[Name]
