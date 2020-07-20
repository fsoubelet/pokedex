"""
Model classes for the 'Games' endpoint objects. Available endpoints are:
- Generations (https://pokeapi.co/api/v2/generation/{id or name}/)
- Pokedexes (https://pokeapi.co/api/v2/pokedex/{id or name}/)
- Version (https://pokeapi.co/api/v2/version/{id or name}/)
- Version Groups (https://pokeapi.co/api/v2/version-group/{id or name}/)
"""

from typing import List, Optional

from pydantic import BaseModel

from pokedex.models.commons import Description, Name, NamedAPIResource


class Generation(BaseModel):
    """
    A generation is a grouping of the Pokémon games that separates them based on the Pokémon they
    include. In each generation, a new set of Pokémon, Moves, Abilities and Types that did not
    exist in the previous generation are released.
    """

    id: int
    name: str
    abilities: List[NamedAPIResource]
    names: List[Name]
    main_region: Optional[NamedAPIResource]
    moves: List[NamedAPIResource]
    pokemon_species: List[NamedAPIResource]
    types: List[NamedAPIResource]
    version_groups: List[NamedAPIResource]


class PokemonEntry(BaseModel):
    entry_number: int
    pokemon_species: Optional[NamedAPIResource]


class Pokedex(BaseModel):
    """
    A Pokédex is a handheld electronic encyclopedia device; one which is capable of recording and
    retaining information of the various Pokémon in a given region with the exception of the
    national dex and some smaller dexes related to portions of a region.
    """

    id: int
    name: str
    is_main_series: bool
    descriptions: List[Description]
    names: List[Name]
    pokemon_entries: List[PokemonEntry]
    region: Optional[NamedAPIResource]
    version_groups: List[NamedAPIResource]


class Version(BaseModel):
    """Versions of the games, e.g., Red, Blue or Yellow."""

    id: int
    name: str
    names: List[Name]
    version_group: Optional[NamedAPIResource]


class VersionGroup(BaseModel):
    """Version groups categorize highly similar versions of the games."""

    id: int
    name: str
    order: int
    generation: Optional[NamedAPIResource]
    move_learn_methods: List[NamedAPIResource]
    pokedexes: List[NamedAPIResource]
    regions: List[NamedAPIResource]
    versions: List[NamedAPIResource]
