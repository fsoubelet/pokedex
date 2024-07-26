"""
Model classes for the 'Berries' endpoint objects. Available endpoints are:
- Berries (https://pokeapi.co/api/v2/berry/{id or name}/)
- Berry Firmnesses (https://pokeapi.co/api/v2/berry-firmness/{id or name}/)
- Berry Flavors (https://pokeapi.co/api/v2/berry-flavor/{id or name}/)
"""

from __future__ import annotations

from pydantic import BaseModel

from pokedex.models.commons import Name, NamedAPIResource


class BerryFlavorMap(BaseModel):
    potency: int
    flavor: NamedAPIResource | None


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
    firmness: NamedAPIResource | None
    flavors: list[BerryFlavorMap]
    item: NamedAPIResource | None
    natural_gift_type: NamedAPIResource | None


class BerryFirmness(BaseModel):
    """Berries can be soft or hard."""

    id: int
    name: str
    berries: list[NamedAPIResource]
    names: list[Name]


class FlavorBerryMap(BaseModel):
    potency: int
    berry: NamedAPIResource | None


class BerryFlavor(BaseModel):
    """
    Flavors determine whether a Pokémon will benefit or suffer from eating a berry based on their
    nature.
    """

    id: int
    name: str
    berries: list[FlavorBerryMap]
    contest_type: NamedAPIResource | None
    names: list[Name]
