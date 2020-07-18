from typing import List

from pydantic import BaseModel

from pokedex.models import basics
from pokedex.models import items
from pokedex.models import locations
from pokedex.models import moves
from pokedex.models import pokemon


class EvolutionChain(BaseModel):
    id: int
    baby_trigger_item: items.Item
    chain: ChainLink


class ChainLink(BaseModel):
    is_baby: bool
    species: pokemon.PokemonSpecies
    evolution_details: List[EvolutionDetail]
    evolves_to: List[ChainLink]


class EvolutionDetail(BaseModel):
    item: items.Item
    trigger: EvolutionTrigger
    gender: int
    held_item: items.Item
    known_move: moves.Move
    known_move_type: pokemon.Type
    location: locations.Location
    min_level: int
    min_happiness: int
    min_beauty: int
    min_affection: int
    needs_overworld_rain: bool
    party_species: pokemon.PokemonSpecies
    party_type: pokemon.Type
    relative_physical_stats: int
    time_of_day: str
    trade_species: pokemon.PokemonSpecies
    turn_upside_down: bool


class EvolutionTrigger(BaseModel):
    id: int
    name: str
    names: List[basics.Name]
    pokemon_species: List[pokemon.PokemonSpecies]
