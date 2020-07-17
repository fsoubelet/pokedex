from typing import List

from pydantic import BaseModel

from pokedex.models.basics import Name
from pokedex.models.commons import Description
from pokedex.models.locations import Region
from pokedex.models.moves import Move, MoveLearnMethod
from pokedex.models.pokemon import Ability, PokemonSpecies, Type


class Generation(BaseModel):
    id: int
    name: str
    abilities: List[Ability]
    names: List[Name]
    main_region: Region
    moves: List[Move]
    pokemon_species: List[PokemonSpecies]
    types: List[Type]
    version_groups: List[VersionGroup]


class Pokedex(BaseModel):
    id: int
    name: str
    is_main_series: bool
    descriptions: List[Description]
    names: List[Name]
    pokemon_entries: List[PokemonEntry]
    region: Region
    version_groups: List[VersionGroup]


class PokemonEntry(BaseModel):
    entry_number: int
    pokemon_species: PokemonSpecies


class Version(BaseModel):
    id: int
    name: str
    names: List[Name]
    version_group: VersionGroup


class VersionGroup(BaseModel):
    id: int
    name: str
    order: int
    generation: Generation
    move_learn_methods: List[MoveLearnMethod]
    pokedexes: List[Pokedex]
    regions: List[Region]
    versions: List[Version]
