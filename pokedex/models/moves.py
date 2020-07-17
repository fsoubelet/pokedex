from typing import List

from pydantic import BaseModel

from pokedex.models.basics import Language, Name
from pokedex.models.commons import Description, MachineVersionDetail, VerboseEffect
from pokedex.models.contests import ContestEffect, ContestType, SuperContestEffect
from pokedex.models.games import Generation, VersionGroup
from pokedex.models.pokemon import AbilityEffectChange, Stat, Type


class Move(BaseModel):
    id: int
    name: str
    accuracy: int
    effect_chance: int
    pp: int
    priority: int
    power: int
    contest_combos: ContestComboSets
    contest_type: ContestType
    contest_effect: ContestEffect
    damage_class: MoveDamageClass
    effect_entries: List[VerboseEffect]
    effect_changes: List[AbilityEffectChange]
    flavor_text_entries: List[MoveFlavorText]
    generation: Generation
    machines: List[MachineVersionDetail]
    meta: MoveMetaData
    names: List[Name]
    past_values: List[PastMoveStatValues]
    stat_changes: List[MoveStatChange]
    super_contest_effect: SuperContestEffect
    target: MoveTarget
    type: Type


class ContestComboSets(BaseModel):
    normal: ContestComboDetail
    super: ContestComboDetail


class ContestComboDetail(BaseModel):
    use_before: List[Move]
    use_after: List[Move]


class MoveFlavorText(BaseModel):
    flavor_text: str
    language: Language
    version_group: VersionGroup


class MoveMetaData(BaseModel):
    ailment: MoveAilment
    category: MoveCategory
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


class MoveStatChange(BaseModel):
    change: int
    stat: Stat


class PastMoveStatValues(BaseModel):
    accuracy: int
    effect_chance: int
    power: int
    pp: int
    effect_entries: List[VerboseEffect]
    type: Type
    version_group: VersionGroup


class MoveAilment(BaseModel):
    id: int
    name: str
    moves: List[Move]
    names: List[Name]


class MoveBattleStyle(BaseModel):
    id: int
    name: str
    names: List[Name]


class ModelName(BaseModel):
    id: int
    name: str
    moves: List[Move]
    descriptions: List[Description]


class MoveDamageClass(BaseModel):
    id: int
    name: str
    descriptions: List[Description]
    moves: List[Move]
    names: List[Name]


class MoveLearnMethod(BaseModel):
    id: int
    name: str
    descriptions: List[Description]
    names: List[Name]
    version_groups: List[VersionGroup]


class MoveTarget(BaseModel):
    id: int
    name: str
    descriptions: List[Description]
    moves: List[Move]
    names: List[Name]
