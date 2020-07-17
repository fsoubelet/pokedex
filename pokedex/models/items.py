from typing import List

from pydantic import BaseModel

from pokedex.models.basics import Name
from pokedex.models.commons import (
    Description,
    Effect,
    GenerationGameIndex,
    MachineVersionDetail,
    VerboseEffect,
    VersionGroupFlavorText,
)
from pokedex.models.evolution import EvolutionChain
from pokedex.models.games import Version
from pokedex.models.pokemon import Pokemon


class Item(BaseModel):
    id: int
    name: str
    cost: int
    fling_power: int
    fling_effect: ItemFlingEffect
    attributes: List[ItemAttribute]
    category: ItemCategory
    effect_entries: List[VerboseEffect]
    flavor_text_entries: List[VersionGroupFlavorText]
    game_indices: List[GenerationGameIndex]
    names: List[Name]
    sprites: ItemSprites
    held_by_pokemon: List[ItemHolderPokemon]
    baby_trigger_for: EvolutionChain
    machines: List[MachineVersionDetail]


class ItemSprites(BaseModel):
    default: str


class ItemHolderPokemon(BaseModel):
    pokemon: Pokemon
    version_details: List[ItemHolderPokemonVersionDetail]


class ItemHolderPokemonVersionDetail(BaseModel):
    rarity: int
    version: Version


class ItemAttribute(BaseModel):
    id: int
    name: str
    items: List[Item]
    names: List[Name]
    descriptions: List[Description]


class ItemCategory(BaseModel):
    id: int
    name: str
    items: List[Item]
    names: List[Name]
    pocket: ItemPocket


class ItemFlingEffect(BaseModel):
    id: int
    name: str
    effect_entries: List[Effect]
    items: List[Item]


class ItemPocket(BaseModel):
    id: int
    name: str
    categories: List[ItemCategory]
    names: List[Name]
