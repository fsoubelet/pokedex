from typing import List

from pydantic import BaseModel

from pokedex.models import basics, commons, locations, moves, pokemon


class Generation(BaseModel):
    id: int
    name: str
    abilities: List[pokemon.Ability]
    names: List[basics.Name]
    main_region: locations.Region
    moves: List[moves.Move]
    pokemon_species: List[pokemon.PokemonSpecies]
    types: List[pokemon.Type]
    version_groups: List[VersionGroup]


class Pokedex(BaseModel):
    id: int
    name: str
    is_main_series: bool
    descriptions: List[commons.Description]
    names: List[basics.Name]
    pokemon_entries: List[PokemonEntry]
    region: locations.Region
    version_groups: List[VersionGroup]


class PokemonEntry(BaseModel):
    entry_number: int
    pokemon_species: pokemon.PokemonSpecies


class Version(BaseModel):
    id: int
    name: str
    names: List[basics.Name]
    version_group: VersionGroup


class VersionGroup(BaseModel):
    id: int
    name: str
    order: int
    generation: Generation
    move_learn_methods: List[moves.MoveLearnMethod]
    pokedexes: List[Pokedex]
    regions: List[locations.Region]
    versions: List[Version]
