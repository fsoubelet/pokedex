from typing import List

from pydantic import BaseModel

from pokedex.models.commons import (
    APIResource,
    Description,
    Effect,
    GenerationGameIndex,
    MachineVersionDetail,
    Name,
    NamedAPIResource,
    VerboseEffect,
    VersionGroupFlavorText,
)


class ItemSprites(BaseModel):
    default: str


class ItemHolderPokemonVersionDetail(BaseModel):
    rarity: int
    version: NamedAPIResource


class ItemHolderPokemon(BaseModel):
    pokemon: NamedAPIResource
    version_details: List[ItemHolderPokemonVersionDetail]


class Item(BaseModel):
    id: int
    name: str
    cost: int
    fling_power: int
    fling_effect: NamedAPIResource
    attributes: List[NamedAPIResource]
    category: NamedAPIResource
    effect_entries: List[VerboseEffect]
    flavor_text_entries: List[VersionGroupFlavorText]
    game_indices: List[GenerationGameIndex]
    names: List[Name]
    sprites: ItemSprites
    held_by_pokemon: List[ItemHolderPokemon]
    baby_trigger_for: APIResource
    machines: List[MachineVersionDetail]


class ItemAttribute(BaseModel):
    id: int
    name: str
    items: List[NamedAPIResource]
    names: List[Name]
    descriptions: List[Description]


class ItemCategory(BaseModel):
    id: int
    name: str
    items: List[NamedAPIResource]
    names: List[Name]
    pocket: NamedAPIResource


class ItemFlingEffect(BaseModel):
    id: int
    name: str
    effect_entries: List[Effect]
    items: List[NamedAPIResource]


class ItemPocket(BaseModel):
    id: int
    name: str
    categories: List[NamedAPIResource]
    names: List[Name]
