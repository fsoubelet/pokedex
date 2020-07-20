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

from typing import List, Optional

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
    use_before: Optional[List[NamedAPIResource]]
    use_after: Optional[List[NamedAPIResource]]


class ContestComboSets(BaseModel):
    normal: ContestComboDetail
    super: ContestComboDetail


class MoveFlavorText(BaseModel):
    flavor_text: str
    language: Optional[NamedAPIResource]
    version_group: Optional[NamedAPIResource]


class MoveMetaData(BaseModel):
    ailment: Optional[NamedAPIResource]
    category: Optional[NamedAPIResource]
    min_hits: Optional[int]
    max_hits: Optional[int]
    min_turns: Optional[int]
    max_turns: Optional[int]
    drain: int
    healing: int
    crit_rate: int
    ailment_chance: int
    flinch_chance: int
    stat_chance: int


class PastMoveStatValues(BaseModel):
    accuracy: Optional[int]
    effect_chance: Optional[int]
    power: Optional[int]
    pp: Optional[int]
    effect_entries: List[VerboseEffect]
    type: Optional[NamedAPIResource]
    version_group: Optional[NamedAPIResource]


class MoveStatChange(BaseModel):
    change: int
    stat: Optional[NamedAPIResource]


class Move(BaseModel):
    """
    Moves are the skills of Pokémon in battle. In battle, a Pokémon uses one move each turn. Some
    moves (including those learned by Hidden Machine) can be used outside of battle as well,
    usually for the purpose of removing obstacles or exploring new areas.
    """

    id: int
    name: str
    accuracy: Optional[int]
    effect_chance: Optional[int]
    pp: int
    priority: int
    power: Optional[int]
    contest_combos: Optional[ContestComboSets]
    contest_type: Optional[NamedAPIResource]
    contest_effect: Optional[APIResource]
    damage_class: Optional[NamedAPIResource]
    effect_entries: List[VerboseEffect]
    effect_changes: List[AbilityEffectChange]
    flavor_text_entries: List[MoveFlavorText]
    generation: Optional[NamedAPIResource]
    machines: List[MachineVersionDetail]
    meta: MoveMetaData
    names: List[Name]
    past_values: List[PastMoveStatValues]
    stat_changes: List[MoveStatChange]
    super_contest_effect: Optional[APIResource]
    target: Optional[NamedAPIResource]
    type: Optional[NamedAPIResource]


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
