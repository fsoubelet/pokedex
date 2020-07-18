from typing import List

from pydantic import BaseModel

from pokedex.models.commons import Description, Name, NamedAPIResource


class Generation(BaseModel):
    id: int
    name: str
    abilities: List[NamedAPIResource]
    names: List[Name]
    main_region: NamedAPIResource
    moves: List[NamedAPIResource]
    pokemon_species: List[NamedAPIResource]
    types: List[NamedAPIResource]
    version_groups: List[NamedAPIResource]


class PokemonEntry(BaseModel):
    entry_number: int
    pokemon_species: NamedAPIResource


class Pokedex(BaseModel):
    id: int
    name: str
    is_main_series: bool
    descriptions: List[Description]
    names: List[Name]
    pokemon_entries: List[PokemonEntry]
    region: NamedAPIResource
    version_groups: List[NamedAPIResource]


class Version(BaseModel):
    id: int
    name: str
    names: List[Name]
    version_group: NamedAPIResource


class VersionGroup(BaseModel):
    id: int
    name: str
    order: int
    generation: NamedAPIResource
    move_learn_methods: List[NamedAPIResource]
    pokedexes: List[NamedAPIResource]
    regions: List[NamedAPIResource]
    versions: List[NamedAPIResource]
