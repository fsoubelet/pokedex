"""
Model classes for the 'Berries' endpoint objects. Available endpoints are:
- Berries (https://pokeapi.co/api/v2/berry/{id or name}/)
- Berry Firmnesses (https://pokeapi.co/api/v2/berry-firmness/{id or name}/)
- Berry Flavors (https://pokeapi.co/api/v2/berry-flavor/{id or name}/)
"""

from typing import List, Optional

from pydantic import BaseModel

from pokedex.models.commons import Name, NamedAPIResource


class BerryFlavorMap(BaseModel):
    potency: int
    flavor: Optional[NamedAPIResource]


class Berry(BaseModel):
    """
    Berries are small fruits that can provide HP and status condition restoration,
    stat enhancement, and even damage negation when eaten by Pokémon.
    """

    id: int
    name: str
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    size: int
    smoothness: int
    soil_dryness: int
    firmness: Optional[NamedAPIResource]
    flavors: List[BerryFlavorMap]
    item: Optional[NamedAPIResource]
    natural_gift_type: Optional[NamedAPIResource]


class BerryFirmness(BaseModel):
    """Berries can be soft or hard."""

    id: int
    name: str
    berries: List[NamedAPIResource]
    names: List[Name]


class FlavorBerryMap(BaseModel):
    potency: int
    berry: Optional[NamedAPIResource]


class BerryFlavor(BaseModel):
    """
    Flavors determine whether a Pokémon will benefit or suffer from eating a berry based on their
    nature.
    """

    id: int
    name: str
    berries: List[FlavorBerryMap]
    contest_type: Optional[NamedAPIResource]
    names: List[Name]
