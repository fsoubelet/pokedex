"""
Model classes for the 'Items' endpoint objects. Available endpoints are:
- Item (https://pokeapi.co/api/v2/item/{id or name}/)
- Item Attributes (https://pokeapi.co/api/v2/item-attribute/{id or name}/)
- Item Categories (https://pokeapi.co/api/v2/item-category/{id or name}/)
- Item Fling Effects (https://pokeapi.co/api/v2/item-fling-effect/{id or name}/)
- Item Pockets (https://pokeapi.co/api/v2/item-pocket/{id or name}/)
"""

from typing import List, Optional

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
    version: Optional[NamedAPIResource]


class ItemHolderPokemon(BaseModel):
    pokemon: Optional[NamedAPIResource]
    version_details: List[ItemHolderPokemonVersionDetail]


class Item(BaseModel):
    """
    An item is an object in the games which the player can pick up, keep in their bag, and use in
    some manner. They have various uses, including healing, powering up, helping catch Pokémon,
    or to access a new area.
    """

    id: int
    name: str
    cost: int
    fling_power: Optional[int]
    fling_effect: Optional[NamedAPIResource]
    attributes: List[NamedAPIResource]
    category: Optional[NamedAPIResource]
    effect_entries: List[VerboseEffect]
    flavor_text_entries: List[VersionGroupFlavorText]
    game_indices: List[GenerationGameIndex]
    names: List[Name]
    sprites: ItemSprites
    held_by_pokemon: List[ItemHolderPokemon]
    baby_trigger_for: Optional[APIResource]
    machines: List[MachineVersionDetail]


class ItemAttribute(BaseModel):
    """
    Item attributes define particular aspects of items, e.g. "usable in battle" or "consumable".
    """

    id: int
    name: str
    items: List[NamedAPIResource]
    names: List[Name]
    descriptions: List[Description]


class ItemCategory(BaseModel):
    """Item categories determine where items will be placed in the players bag."""

    id: int
    name: str
    items: List[NamedAPIResource]
    names: List[Name]
    pocket: Optional[NamedAPIResource]


class ItemFlingEffect(BaseModel):
    """The various effects of the move "Fling" when used with different items."""

    id: int
    name: str
    effect_entries: List[Effect]
    items: List[NamedAPIResource]


class ItemPocket(BaseModel):
    """Pockets within the players bag used for storing items by category."""

    id: int
    name: str
    categories: List[NamedAPIResource]
    names: List[Name]
