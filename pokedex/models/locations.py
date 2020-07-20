"""
Model classes for the 'Locations' endpoint objects. Available endpoints are:
- Locations (https://pokeapi.co/api/v2/location/{id or name}/)
- Location Areas (https://pokeapi.co/api/v2/location-area/{id or name}/)
- Pal Park Areas (https://pokeapi.co/api/v2/pal-park-area/{id or name}/)
- Regions (https://pokeapi.co/api/v2/region/{id or name}/)
"""

from typing import List, Optional

from pydantic import BaseModel

from pokedex.models.commons import (
    GenerationGameIndex,
    Name,
    NamedAPIResource,
    VersionEncounterDetail,
)


class Location(BaseModel):
    """
    Locations that can be visited within the games. Locations make up sizable portions of
    regions, like cities or routes.
    """

    id: int
    name: str
    region: Optional[NamedAPIResource]
    names: List[Name]
    game_indices: List[GenerationGameIndex]
    areas: List[NamedAPIResource]


class EncounterVersionDetails(BaseModel):
    rate: int
    version: Optional[NamedAPIResource]


class EncounterMethodRate(BaseModel):
    encounter_method: Optional[NamedAPIResource]
    version_details: List[EncounterVersionDetails]


class PokemonEncounter(BaseModel):
    pokemon: Optional[NamedAPIResource]
    version_details: List[VersionEncounterDetail]


class LocationArea(BaseModel):
    """
    Location areas are sections of areas, such as floors in a building or cave. Each area has its
    own set of possible Pokémon encounters.
    """

    id: int
    name: str
    game_index: int
    encounter_method_rates: List[EncounterMethodRate]
    location: Optional[NamedAPIResource]
    names: List[Name]
    pokemon_encounters: List[PokemonEncounter]


class PalParkEncounterSpecies(BaseModel):
    base_score: int
    rate: int
    pokemon_species: Optional[NamedAPIResource]


class PalParkArea(BaseModel):
    """
    Areas used for grouping Pokémon encounters in Pal Park. They're like habitats that are
    specific to Pal Park.
    """

    id: int
    name: str
    names: List[Name]
    pokemon_encounters: List[PalParkEncounterSpecies]


class Region(BaseModel):
    """
    A region is an organized area of the Pokémon world. Most often, the main difference between
    regions is the species of Pokémon that can be encountered within them.
    """

    id: int
    locations: List[NamedAPIResource]
    name: str
    names: List[Name]
    main_generation: Optional[NamedAPIResource]
    pokedexes: List[NamedAPIResource]
    version_groups: List[NamedAPIResource]
