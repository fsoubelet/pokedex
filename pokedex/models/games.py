"""
Model classes for the 'Games' endpoint objects. Available endpoints are:
- Generations (https://pokeapi.co/api/v2/generation/{id or name}/)
- Pokedexes (https://pokeapi.co/api/v2/pokedex/{id or name}/)
- Version (https://pokeapi.co/api/v2/version/{id or name}/)
- Version Groups (https://pokeapi.co/api/v2/version-group/{id or name}/)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from pokedex.models.commons import Description, Name, NamedAPIResource


class Generation(BaseModel):
    """
    A generation is a grouping of the Pokémon games that separates them based on the Pokémon they
    include. In each generation, a new set of Pokémon, Moves, Abilities and Types that did not
    exist in the previous generation are released.
    """

    id: int
    name: str
    abilities: list[NamedAPIResource]
    names: list[Name]
    main_region: NamedAPIResource | None
    moves: list[NamedAPIResource]
    pokemon_species: list[NamedAPIResource]
    types: list[NamedAPIResource]
    version_groups: list[NamedAPIResource]


class PokemonEntry(BaseModel):
    entry_number: int
    pokemon_species: NamedAPIResource | None


class Pokedex(BaseModel):
    """
    A Pokédex is a handheld electronic encyclopedia device; one which is capable of recording and
    retaining information of the various Pokémon in a given region with the exception of the
    national dex and some smaller dexes related to portions of a region.
    """

    id: int
    name: str
    is_main_series: bool
    descriptions: list[Description]
    names: list[Name]
    pokemon_entries: list[PokemonEntry]
    region: NamedAPIResource | None
    version_groups: list[NamedAPIResource]


class Version(BaseModel):
    """Versions of the games, e.g., Red, Blue or Yellow."""

    id: int
    name: str
    names: list[Name]
    version_group: NamedAPIResource | None


class VersionGroup(BaseModel):
    """Version groups categorize highly similar versions of the games."""

    id: int
    name: str
    order: int
    generation: NamedAPIResource | None
    move_learn_methods: list[NamedAPIResource]
    pokedexes: list[NamedAPIResource]
    regions: list[NamedAPIResource]
    versions: list[NamedAPIResource]
