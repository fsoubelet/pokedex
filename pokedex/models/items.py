from typing import List

from pydantic import BaseModel

from pokedex.models import basics, commons, evolution, games, pokemon


class Item(BaseModel):
    id: int
    name: str
    cost: int
    fling_power: int
    fling_effect: ItemFlingEffect
    attributes: List[ItemAttribute]
    category: ItemCategory
    effect_entries: List[commons.VerboseEffect]
    flavor_text_entries: List[commons.VersionGroupFlavorText]
    game_indices: List[commons.GenerationGameIndex]
    names: List[basics.Name]
    sprites: ItemSprites
    held_by_pokemon: List[ItemHolderPokemon]
    baby_trigger_for: evolution.EvolutionChain
    machines: List[commons.MachineVersionDetail]


class ItemSprites(BaseModel):
    default: str


class ItemHolderPokemon(BaseModel):
    pokemon: pokemon.Pokemon
    version_details: List[ItemHolderPokemonVersionDetail]


class ItemHolderPokemonVersionDetail(BaseModel):
    rarity: int
    version: games.Version


class ItemAttribute(BaseModel):
    id: int
    name: str
    items: List[Item]
    names: List[basics.Name]
    descriptions: List[commons.Description]


class ItemCategory(BaseModel):
    id: int
    name: str
    items: List[Item]
    names: List[basics.Name]
    pocket: ItemPocket


class ItemFlingEffect(BaseModel):
    id: int
    name: str
    effect_entries: List[commons.Effect]
    items: List[Item]


class ItemPocket(BaseModel):
    id: int
    name: str
    categories: List[ItemCategory]
    names: List[basics.Name]
