from typing import List

from pydantic import BaseModel

from pokedex.models.basics import Name
from pokedex.models.items import Item
from pokedex.models.locations import Location
from pokedex.models.moves import Move
from pokedex.models.pokemon import PokemonSpecies, Type


class EvolutionChain(BaseModel):
    id: int
    baby_trigger_item: Item
    chain: ChainLink


class ChainLink(BaseModel):
    is_baby: bool
    species: PokemonSpecies
    evolution_details: List[EvolutionDetail]
    evolves_to: List[ChainLink]


class EvolutionDetail(BaseModel):
    item: Item
    trigger: EvolutionTrigger
    gender: int
    held_item: Item
    known_move: Move
    known_move_type: Type
    location: Location
    min_level: int
    min_happiness: int
    min_beauty: int
    min_affection: int
    needs_overworld_rain: bool
    party_species: PokemonSpecies
    party_type: Type
    relative_physical_stats: int
    time_of_day: str
    trade_species: PokemonSpecies
    turn_upside_down: bool


class EvolutionTrigger(BaseModel):
    id: int
    name: str
    names: List[Name]
    pokemon_species: List[PokemonSpecies]
