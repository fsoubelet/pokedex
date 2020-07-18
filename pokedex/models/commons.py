"""
Model classes for the 'Utility' objects.
"""

from typing import List

from pydantic import BaseModel


class NamedAPIResource(BaseModel):
    name: str
    url: str


class Name(BaseModel):
    name: str
    language: NamedAPIResource


class Language(BaseModel):
    """Languages for translations of API resource information."""

    id: int
    name: str
    official: bool
    iso639: str
    iso3166: str
    names: List[Name]


class APIResource(BaseModel):
    url: str


class Description(BaseModel):
    description: str
    language: NamedAPIResource


class Effect(BaseModel):
    effect: str
    language: NamedAPIResource


class Encounter(BaseModel):
    min_level: int
    max_level: int
    condition_values: List[NamedAPIResource]
    chance: int
    method: NamedAPIResource


class FlavorText(BaseModel):
    flavor_text: str
    language: NamedAPIResource
    version: NamedAPIResource


class GenerationGameIndex(BaseModel):
    game_index: int
    generation: NamedAPIResource


class MachineVersionDetail(BaseModel):
    machine: APIResource
    version_group: NamedAPIResource


class VerboseEffect(BaseModel):
    effect: str
    short_effect: str
    language: NamedAPIResource


class VersionEncounterDetail(BaseModel):
    version: NamedAPIResource
    max_chance: int
    encounter_details: List[Encounter]


class VersionGameIndex(BaseModel):
    game_index: int
    version: NamedAPIResource


class VersionGroupFlavorText(BaseModel):
    text: str
    language: NamedAPIResource
    version_group: NamedAPIResource
