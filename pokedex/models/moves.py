"""
Model classes for the 'Moves' endpoint objects. Available endpoints are:
- Moves (https://pokeapi.co/api/v2/move/{id or name}/)
- Move Ailments (https://pokeapi.co/api/v2/move-ailment/{id or name}/)
- Move Battle Styles (https://pokeapi.co/api/v2/move-battle-style/{id or name}/)
- Move Categories (https://pokeapi.co/api/v2/move-category/{id or name}/)
- Move Damage Classes (https://pokeapi.co/api/v2/move-damage-class/{id or name}/)
- Move Learn Methods (https://pokeapi.co/api/v2/move-learn-method/{id or name}/)
- Move Targets (https://pokeapi.co/api/v2/move-target/{id or name}/)
"""
from __future__ import annotations

from typing import List

from pydantic import BaseModel

from pokedex.models.commons import (
    APIResource,
    Description,
    MachineVersionDetail,
    Name,
    NamedAPIResource,
    VerboseEffect,
)
from pokedex.models.pokemon import AbilityEffectChange


class ContestComboDetail(BaseModel):
    use_before: List[NamedAPIResource] | None
    use_after: List[NamedAPIResource] | None


class ContestComboSets(BaseModel):
    normal: ContestComboDetail
    super: ContestComboDetail


class MoveFlavorText(BaseModel):
    flavor_text: str
    language: NamedAPIResource | None
    version_group: NamedAPIResource | None


class MoveMetaData(BaseModel):
    ailment: NamedAPIResource | None
    category: NamedAPIResource | None
    min_hits: int | None
    max_hits: int | None
    min_turns: int | None
    max_turns: int | None
    drain: int
    healing: int
    crit_rate: int
    ailment_chance: int
    flinch_chance: int
    stat_chance: int


class PastMoveStatValues(BaseModel):
    accuracy: int | None
    effect_chance: int | None
    power: int | None
    pp: int | None
    effect_entries: List[VerboseEffect]
    type: NamedAPIResource | None
    version_group: NamedAPIResource | None


class MoveStatChange(BaseModel):
    change: int
    stat: NamedAPIResource | None


class Move(BaseModel):
    """
    Moves are the skills of Pokémon in battle. In battle, a Pokémon uses one move each turn. Some
    moves (including those learned by Hidden Machine) can be used outside of battle as well,
    usually for the purpose of removing obstacles or exploring new areas.
    """

    id: int
    name: str
    accuracy: int | None
    effect_chance: int | None
    pp: int
    priority: int
    power: int | None
    contest_combos: ContestComboSets | None
    contest_type: NamedAPIResource | None
    contest_effect: APIResource | None
    damage_class: NamedAPIResource | None
    effect_entries: List[VerboseEffect]
    effect_changes: List[AbilityEffectChange]
    flavor_text_entries: List[MoveFlavorText]
    generation: NamedAPIResource | None
    machines: List[MachineVersionDetail]
    meta: MoveMetaData
    names: List[Name]
    past_values: List[PastMoveStatValues]
    stat_changes: List[MoveStatChange]
    super_contest_effect: APIResource | None
    target: NamedAPIResource | None
    type: NamedAPIResource | None


class MoveAilment(BaseModel):
    """Move Ailments are status conditions caused by moves used during battle."""

    id: int
    name: str
    moves: List[NamedAPIResource]
    names: List[Name]


class MoveBattleStyle(BaseModel):
    """Styles of moves when used in the Battle Palace."""

    id: int
    name: str
    names: List[Name]


class ModelName(BaseModel):
    """Very general categories that loosely group move effects."""

    id: int
    name: str
    moves: List[NamedAPIResource]
    descriptions: List[Description]


class MoveDamageClass(BaseModel):
    """Damage classes moves can have, e.g. physical, special, or non-damaging."""

    id: int
    name: str
    descriptions: List[Description]
    moves: List[NamedAPIResource]
    names: List[Name]


class MoveLearnMethod(BaseModel):
    """Methods by which Pokémon can learn moves."""

    id: int
    name: str
    descriptions: List[Description]
    names: List[Name]
    version_groups: List[NamedAPIResource]


class MoveTarget(BaseModel):
    """
    Targets moves can be directed at during battle. Targets can be Pokémon, environments or even
    other moves.
    """

    id: int
    name: str
    descriptions: List[Description]
    moves: List[NamedAPIResource]
    names: List[Name]
