"""
Model classes for the 'Utility' objects.
"""
from __future__ import annotations

from pydantic import BaseModel


class NamedAPIResource(BaseModel):
    name: str
    url: str


class Name(BaseModel):
    name: str
    language: NamedAPIResource | None


class Language(BaseModel):
    """Languages for translations of API resource information."""

    id: int
    name: str
    official: bool
    iso639: str
    iso3166: str
    names: list[Name]


class APIResource(BaseModel):
    url: str


class Description(BaseModel):
    description: str
    language: NamedAPIResource | None


class Effect(BaseModel):
    effect: str
    language: NamedAPIResource | None


class Encounter(BaseModel):
    min_level: int
    max_level: int
    condition_values: list[NamedAPIResource]
    chance: int
    method: NamedAPIResource | None


class FlavorText(BaseModel):
    flavor_text: str
    language: NamedAPIResource | None
    version: NamedAPIResource | None


class GenerationGameIndex(BaseModel):
    game_index: int
    generation: NamedAPIResource | None


class MachineVersionDetail(BaseModel):
    machine: APIResource
    version_group: NamedAPIResource | None


class VerboseEffect(BaseModel):
    effect: str
    short_effect: str
    language: NamedAPIResource | None


class VersionEncounterDetail(BaseModel):
    version: NamedAPIResource | None
    max_chance: int
    encounter_details: list[Encounter]


class VersionGameIndex(BaseModel):
    game_index: int
    version: NamedAPIResource | None


class VersionGroupFlavorText(BaseModel):
    text: str
    language: NamedAPIResource | None
    version_group: NamedAPIResource | None
