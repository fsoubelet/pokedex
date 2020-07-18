from typing import List

from pydantic import BaseModel

from pokedex.models import encounters, games, machines


class Language(BaseModel):
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
    language: Language


class Effect(BaseModel):
    effect: str
    language: Language


class Encounter(BaseModel):
    min_level: int
    max_level: int
    condition_values: List[encounters.EncounterConditionValue]
    chance: int
    method: encounters.EncounterMethod


class FlavorText(BaseModel):
    flavor_text: str
    language: Language
    version: games.Version


class GenerationGameIndex(BaseModel):
    game_index: int
    generation: games.Generation


class MachineVersionDetail(BaseModel):
    machine: machines.Machine
    version_group: games.VersionGroup


class Name(BaseModel):
    name: str
    language: Language


class NamedAPIResource(BaseModel):
    name: str
    url: str


class VerboseEffect(BaseModel):
    effect: str
    short_effect: str
    language: Language


class VersionEncounterDetail(BaseModel):
    version: games.Version
    max_chance: int
    encounter_details: List[Encounter]


class VersionGameIndex(BaseModel):
    game_index: int
    version: games.Version


class VersionGroupFlavorText(BaseModel):
    text: str
    language: Language
    version_group: games.VersionGroup
