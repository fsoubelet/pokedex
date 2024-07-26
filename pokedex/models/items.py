"""
Model classes for the 'Items' endpoint objects. Available endpoints are:
- Item (https://pokeapi.co/api/v2/item/{id or name}/)
- Item Attributes (https://pokeapi.co/api/v2/item-attribute/{id or name}/)
- Item Categories (https://pokeapi.co/api/v2/item-category/{id or name}/)
- Item Fling Effects (https://pokeapi.co/api/v2/item-fling-effect/{id or name}/)
- Item Pockets (https://pokeapi.co/api/v2/item-pocket/{id or name}/)
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
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
    version: NamedAPIResource | None


class ItemHolderPokemon(BaseModel):
    pokemon: NamedAPIResource | None
    version_details: list[ItemHolderPokemonVersionDetail]


class Item(BaseModel):
    """
    An item is an object in the games which the player can pick up, keep in their bag, and use in
    some manner. They have various uses, including healing, powering up, helping catch Pokémon,
    or to access a new area.
    """

    id: int
    name: str
    cost: int
    fling_power: int | None
    fling_effect: NamedAPIResource | None
    attributes: list[NamedAPIResource]
    category: NamedAPIResource | None
    effect_entries: list[VerboseEffect]
    flavor_text_entries: list[VersionGroupFlavorText]
    game_indices: list[GenerationGameIndex]
    names: list[Name]
    sprites: ItemSprites
    held_by_pokemon: list[ItemHolderPokemon]
    baby_trigger_for: APIResource | None
    machines: list[MachineVersionDetail]


class ItemAttribute(BaseModel):
    """
    Item attributes define particular aspects of items, e.g. "usable in battle" or "consumable".
    """

    id: int
    name: str
    items: list[NamedAPIResource]
    names: list[Name]
    descriptions: list[Description]


class ItemCategory(BaseModel):
    """Item categories determine where items will be placed in the players bag."""

    id: int
    name: str
    items: list[NamedAPIResource]
    names: list[Name]
    pocket: NamedAPIResource | None


class ItemFlingEffect(BaseModel):
    """The various effects of the move "Fling" when used with different items."""

    id: int
    name: str
    effect_entries: list[Effect]
    items: list[NamedAPIResource]


class ItemPocket(BaseModel):
    """Pockets within the players bag used for storing items by category."""

    id: int
    name: str
    categories: list[NamedAPIResource]
    names: list[Name]
