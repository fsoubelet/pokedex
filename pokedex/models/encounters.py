"""
Model classes for the 'Encounters' endpoint objects. Available endpoints are:
- Encounter Methods (https://pokeapi.co/api/v2/encounter-method/{id or name}/)
- Encounter Conditions (https://pokeapi.co/api/v2/encounter-condition/{id or name}/)
- Encounter Condition Values (https://pokeapi.co/api/v2/encounter-condition-value/{id or name}/)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from pokedex.models.commons import Name, NamedAPIResource


class EncounterMethod(BaseModel):
    """
    Methods by which the player might can encounter Pokémon in the wild, e.g., walking in tall
    grass.
    """

    id: int
    name: str
    order: int
    names: list[Name]


class EncounterCondition(BaseModel):
    """Conditions which affect what pokemon might appear in the wild, e.g., day or night."""

    id: int
    name: str
    names: list[Name]
    values: list[NamedAPIResource]


class EncounterConditionValue(BaseModel):
    """
    Encounter condition values are the various states that an encounter condition can have, i.e.,
    time of day can be either day or night.
    """

    id: int
    name: str
    condition: NamedAPIResource | None
    names: list[Name]
