from typing import List

from pydantic import BaseModel

from pokedex.models.basics import Name
from pokedex.models.commons import GenerationGameIndex, VersionEncounterDetail
from pokedex.models.encounters import EncounterMethod
from pokedex.models.games import Generation, Pokedex, Version, VersionGroup
from pokedex.models.pokemon import Pokemon, PokemonSpecies


class Location(BaseModel):
    id: int
    name: str
    region: Region
    names: List[Name]
    game_indices: List[GenerationGameIndex]
    areas: List[LocationArea]


class LocationArea(BaseModel):
    id: int
    name: str
    game_index: int
    encounter_method_rates: List[EncounterMethodRate]
    location: Location
    names: List[Name]
    pokemon_encounters: List[PokemonEncounter]


class EncounterMethodRate(BaseModel):
    encounter_method: EncounterMethod
    version_details: List[EncounterVersionDetails]


class EncounterVersionDetails(BaseModel):
    rate: int
    version: Version


class PokemonEncounter(BaseModel):
    pokemon: Pokemon
    version_details: List[VersionEncounterDetail]


class PalParkArea(BaseModel):
    id: int
    name: str
    names: List[Name]
    pokemon_encounters: List[PalParkEncounterSpecies]


class PalParkEncounterSpecies(BaseModel):
    base_score: int
    rate: int
    pokemon_species: PokemonSpecies


class Region(BaseModel):
    id: int
    locations: List[Location]
    name: str
    names: List[Name]
    main_generation: Generation
    pokedexes: List[Pokedex]
    version_groups: List[VersionGroup]
