"""
Model classes for the 'Contests' endpoint objects. Available endpoints are:
- Contest Types (https://pokeapi.co/api/v2/contest-type/{id or name}/)
- Contest Effects (https://pokeapi.co/api/v2/contest-effect/{id}/)
- Super Contest Effects (https://pokeapi.co/api/v2/super-contest-effect/{id}/)
"""
from __future__ import annotations

from pydantic import BaseModel

from pokedex.models.commons import Effect, FlavorText, NamedAPIResource


class ContestName(BaseModel):
    name: str
    color: str
    language: NamedAPIResource | None


class ContestType(BaseModel):
    """
    Contest types are categories judges used to weigh a Pokémon's condition in Pokémon contests.
    """

    id: int
    name: str
    berry_flavor: NamedAPIResource | None
    names: list[ContestName]


class ContestEffect(BaseModel):
    """Contest effects refer to the effects of moves when used in contests."""

    id: int
    appeal: int
    jam: int
    effect_entries: list[Effect]
    flavor_text_entries: list[FlavorText]


class SuperContestEffect(BaseModel):
    """Super contest effects refer to the effects of moves when used in super contests."""

    id: int
    appeal: int
    flavor_text_entries: list[FlavorText]
    moves: list[NamedAPIResource]
