"""
Model classes for the 'Locations' endpoint objects. Available endpoints are:
- Locations (https://pokeapi.co/api/v2/location/{id or name}/)
- Location Areas (https://pokeapi.co/api/v2/location-area/{id or name}/)
- Pal Park Areas (https://pokeapi.co/api/v2/pal-park-area/{id or name}/)
- Regions (https://pokeapi.co/api/v2/region/{id or name}/)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
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
    region: NamedAPIResource | None
    names: list[Name]
    game_indices: list[GenerationGameIndex]
    areas: list[NamedAPIResource]


class EncounterVersionDetails(BaseModel):
    rate: int
    version: NamedAPIResource | None


class EncounterMethodRate(BaseModel):
    encounter_method: NamedAPIResource | None
    version_details: list[EncounterVersionDetails]


class PokemonEncounter(BaseModel):
    pokemon: NamedAPIResource | None
    version_details: list[VersionEncounterDetail]


class LocationArea(BaseModel):
    """
    Location areas are sections of areas, such as floors in a building or cave. Each area has its
    own set of possible Pokémon encounters.
    """

    id: int
    name: str
    game_index: int
    encounter_method_rates: list[EncounterMethodRate]
    location: NamedAPIResource | None
    names: list[Name]
    pokemon_encounters: list[PokemonEncounter]


class PalParkEncounterSpecies(BaseModel):
    base_score: int
    rate: int
    pokemon_species: NamedAPIResource | None


class PalParkArea(BaseModel):
    """
    Areas used for grouping Pokémon encounters in Pal Park. They're like habitats that are
    specific to Pal Park.
    """

    id: int
    name: str
    names: list[Name]
    pokemon_encounters: list[PalParkEncounterSpecies]


class Region(BaseModel):
    """
    A region is an organized area of the Pokémon world. Most often, the main difference between
    regions is the species of Pokémon that can be encountered within them.
    """

    id: int
    locations: list[NamedAPIResource]
    name: str
    names: list[Name]
    main_generation: NamedAPIResource | None
    pokedexes: list[NamedAPIResource]
    version_groups: list[NamedAPIResource]
