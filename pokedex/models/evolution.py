"""
Model classes for the 'Evolution' endpoint objects. Available endpoints are:
- Evolution Chains (https://pokeapi.co/api/v2/evolution-chain/{id}/)
- Evolution Triggers (https://pokeapi.co/api/v2/evolution-trigger/{id or name}/)
"""

from typing import Dict, List, Optional

from pydantic import BaseModel

from pokedex.models.commons import Name, NamedAPIResource


class EvolutionDetail(BaseModel):
    item: Optional[NamedAPIResource]
    trigger: Optional[NamedAPIResource]
    gender: int
    held_item: Optional[NamedAPIResource]
    known_move: Optional[NamedAPIResource]
    known_move_type: Optional[NamedAPIResource]
    location: Optional[NamedAPIResource]
    min_level: int
    min_happiness: int
    min_beauty: int
    min_affection: int
    needs_overworld_rain: bool
    party_species: Optional[NamedAPIResource]
    party_type: Optional[NamedAPIResource]
    relative_physical_stats: int
    time_of_day: str
    trade_species: Optional[NamedAPIResource]
    turn_upside_down: bool


class ChainLink(BaseModel):
    is_baby: bool
    species: Optional[NamedAPIResource]
    evolution_details: List[EvolutionDetail]
    evolves_to: List[Dict]  # technically is List[ChainLink] but that would NameError


class EvolutionChain(BaseModel):
    """
    Evolution chains are essentially family trees. They start with the lowest stage within a
    family and detail evolution conditions for each as well as Pokémon they can evolve into up
    through the hierarchy.
    """

    id: int
    baby_trigger_item: Optional[NamedAPIResource]
    chain: ChainLink


class EvolutionTrigger(BaseModel):
    """Evolution triggers are the events and conditions that cause a Pokémon to evolve."""

    id: int
    name: str
    names: List[Name]
    pokemon_species: List[NamedAPIResource]
