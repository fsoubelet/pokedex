"""
Model classes for the 'Contests' endpoint objects. Available endpoints are:
- Contest Types (https://pokeapi.co/api/v2/contest-type/{id or name}/)
- Contest Effects (https://pokeapi.co/api/v2/contest-effect/{id}/)
- Super Contest Effects (https://pokeapi.co/api/v2/super-contest-effect/{id}/)
"""

from typing import List

from pydantic import BaseModel

from pokedex.models.commons import Effect, FlavorText, NamedAPIResource


class ContestName(BaseModel):
    name: str
    color: str
    language: NamedAPIResource


class ContestType(BaseModel):
    """
    Contest types are categories judges used to weigh a Pokémon's condition in Pokémon contests.
    """

    id: int
    name: str
    berry_flavor: NamedAPIResource
    names: List[ContestName]


class ContestEffect(BaseModel):
    """Contest effects refer to the effects of moves when used in contests."""

    id: int
    appeal: int
    jam: int
    effect_entries: List[Effect]
    flavor_text_entries: List[FlavorText]


class SuperContestEffect(BaseModel):
    """Super contest effects refer to the effects of moves when used in super contests."""

    id: int
    appeal: int
    flavor_text_entries: List[FlavorText]
    moves: List[NamedAPIResource]
