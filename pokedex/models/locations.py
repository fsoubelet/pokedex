from typing import List

from pydantic import BaseModel

from pokedex.models.commons import (
    GenerationGameIndex,
    Name,
    NamedAPIResource,
    VersionEncounterDetail,
)


class Location(BaseModel):
    id: int
    name: str
    region: NamedAPIResource
    names: List[Name]
    game_indices: List[GenerationGameIndex]
    areas: List[NamedAPIResource]


class EncounterVersionDetails(BaseModel):
    rate: int
    version: NamedAPIResource


class EncounterMethodRate(BaseModel):
    encounter_method: NamedAPIResource
    version_details: List[EncounterVersionDetails]


class PokemonEncounter(BaseModel):
    pokemon: NamedAPIResource
    version_details: List[VersionEncounterDetail]


class LocationArea(BaseModel):
    id: int
    name: str
    game_index: int
    encounter_method_rates: List[EncounterMethodRate]
    location: NamedAPIResource
    names: List[Name]
    pokemon_encounters: List[PokemonEncounter]


class PalParkEncounterSpecies(BaseModel):
    base_score: int
    rate: int
    pokemon_species: NamedAPIResource


class PalParkArea(BaseModel):
    id: int
    name: str
    names: List[Name]
    pokemon_encounters: List[PalParkEncounterSpecies]


class Region(BaseModel):
    id: int
    locations: List[NamedAPIResource]
    name: str
    names: List[Name]
    main_generation: NamedAPIResource
    pokedexes: List[NamedAPIResource]
    version_groups: List[NamedAPIResource]
