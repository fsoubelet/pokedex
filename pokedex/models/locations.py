from typing import List

from pydantic import BaseModel

from pokedex.models import basics
from pokedex.models import commons
from pokedex.models import encounters
from pokedex.models import games
from pokedex.models import pokemon


class Location(BaseModel):
    id: int
    name: str
    region: Region
    names: List[basics.Name]
    game_indices: List[commons.GenerationGameIndex]
    areas: List[LocationArea]


class LocationArea(BaseModel):
    id: int
    name: str
    game_index: int
    encounter_method_rates: List[EncounterMethodRate]
    location: Location
    names: List[basics.Name]
    pokemon_encounters: List[PokemonEncounter]


class EncounterMethodRate(BaseModel):
    encounter_method: encounters.EncounterMethod
    version_details: List[EncounterVersionDetails]


class EncounterVersionDetails(BaseModel):
    rate: int
    version: games.Version


class PokemonEncounter(BaseModel):
    pokemon: pokemon.Pokemon
    version_details: List[commons.VersionEncounterDetail]


class PalParkArea(BaseModel):
    id: int
    name: str
    names: List[basics.Name]
    pokemon_encounters: List[PalParkEncounterSpecies]


class PalParkEncounterSpecies(BaseModel):
    base_score: int
    rate: int
    pokemon_species: pokemon.PokemonSpecies


class Region(BaseModel):
    id: int
    locations: List[Location]
    name: str
    names: List[basics.Name]
    main_generation: games.Generation
    pokedexes: List[games.Pokedex]
    version_groups: List[games.VersionGroup]
