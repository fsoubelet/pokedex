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
    use_before: List[NamedAPIResource]
    use_after: List[NamedAPIResource]


class ContestComboSets(BaseModel):
    normal: ContestComboDetail
    super: ContestComboDetail


class MoveFlavorText(BaseModel):
    flavor_text: str
    language: NamedAPIResource
    version_group: NamedAPIResource


class MoveMetaData(BaseModel):
    ailment: NamedAPIResource
    category: NamedAPIResource
    min_hits: int
    max_hits: int
    min_turns: int
    max_turns: int
    drain: int
    healing: int
    crit_rate: int
    ailment_chance: int
    flinch_chance: int
    stat_chance: int


class PastMoveStatValues(BaseModel):
    accuracy: int
    effect_chance: int
    power: int
    pp: int
    effect_entries: List[VerboseEffect]
    type: NamedAPIResource
    version_group: NamedAPIResource


class MoveStatChange(BaseModel):
    change: int
    stat: NamedAPIResource


class Move(BaseModel):
    id: int
    name: str
    accuracy: int
    effect_chance: int
    pp: int
    priority: int
    power: int
    contest_combos: ContestComboSets
    contest_type: NamedAPIResource
    contest_effect: APIResource
    damage_class: NamedAPIResource
    effect_entries: List[VerboseEffect]
    effect_changes: List[AbilityEffectChange]
    flavor_text_entries: List[MoveFlavorText]
    generation: NamedAPIResource
    machines: List[MachineVersionDetail]
    meta: MoveMetaData
    names: List[Name]
    past_values: List[PastMoveStatValues]
    stat_changes: List[MoveStatChange]
    super_contest_effect: APIResource
    target: NamedAPIResource
    type: NamedAPIResource


class MoveAilment(BaseModel):
    id: int
    name: str
    moves: List[NamedAPIResource]
    names: List[Name]


class MoveBattleStyle(BaseModel):
    id: int
    name: str
    names: List[Name]


class ModelName(BaseModel):
    id: int
    name: str
    moves: List[NamedAPIResource]
    descriptions: List[Description]


class MoveDamageClass(BaseModel):
    id: int
    name: str
    descriptions: List[Description]
    moves: List[NamedAPIResource]
    names: List[Name]


class MoveLearnMethod(BaseModel):
    id: int
    name: str
    descriptions: List[Description]
    names: List[Name]
    version_groups: List[NamedAPIResource]


class MoveTarget(BaseModel):
    id: int
    name: str
    descriptions: List[Description]
    moves: List[NamedAPIResource]
    names: List[Name]
