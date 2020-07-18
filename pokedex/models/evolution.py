from typing import List

from pydantic import BaseModel

from pokedex.models.commons import Name, NamedAPIResource


class EvolutionDetail(BaseModel):
    item: NamedAPIResource
    trigger: NamedAPIResource
    gender: int
    held_item: NamedAPIResource
    known_move: NamedAPIResource
    known_move_type: NamedAPIResource
    location: NamedAPIResource
    min_level: int
    min_happiness: int
    min_beauty: int
    min_affection: int
    needs_overworld_rain: bool
    party_species: NamedAPIResource
    party_type: NamedAPIResource
    relative_physical_stats: int
    time_of_day: str
    trade_species: NamedAPIResource
    turn_upside_down: bool


class ChainLink(BaseModel):
    is_baby: bool
    species: NamedAPIResource
    evolution_details: List[EvolutionDetail]
    evolves_to: List[ChainLink]


class EvolutionChain(BaseModel):
    id: int
    baby_trigger_item: NamedAPIResource
    chain: ChainLink


class EvolutionTrigger(BaseModel):
    id: int
    name: str
    names: List[Name]
    pokemon_species: List[NamedAPIResource]
