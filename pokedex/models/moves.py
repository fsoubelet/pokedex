from typing import List

from pydantic import BaseModel

from pokedex.models import basics, commons, contests, games, pokemon


class Move(BaseModel):
    id: int
    name: str
    accuracy: int
    effect_chance: int
    pp: int
    priority: int
    power: int
    contest_combos: ContestComboSets
    contest_type: contests.ContestType
    contest_effect: contests.ContestEffect
    damage_class: MoveDamageClass
    effect_entries: List[commons.VerboseEffect]
    effect_changes: List[pokemon.AbilityEffectChange]
    flavor_text_entries: List[MoveFlavorText]
    generation: games.Generation
    machines: List[commons.MachineVersionDetail]
    meta: MoveMetaData
    names: List[basics.Name]
    past_values: List[PastMoveStatValues]
    stat_changes: List[MoveStatChange]
    super_contest_effect: contests.SuperContestEffect
    target: MoveTarget
    type: pokemon.Type


class ContestComboSets(BaseModel):
    normal: ContestComboDetail
    super: ContestComboDetail


class ContestComboDetail(BaseModel):
    use_before: List[Move]
    use_after: List[Move]


class MoveFlavorText(BaseModel):
    flavor_text: str
    language: basics.Language
    version_group: games.VersionGroup


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
    stat: pokemon.Stat


class PastMoveStatValues(BaseModel):
    accuracy: int
    effect_chance: int
    power: int
    pp: int
    effect_entries: List[commons.VerboseEffect]
    type: pokemon.Type
    version_group: games.VersionGroup


class MoveAilment(BaseModel):
    id: int
    name: str
    moves: List[Move]
    names: List[basics.Name]


class MoveBattleStyle(BaseModel):
    id: int
    name: str
    names: List[basics.Name]


class ModelName(BaseModel):
    id: int
    name: str
    moves: List[Move]
    descriptions: List[commons.Description]


class MoveDamageClass(BaseModel):
    id: int
    name: str
    descriptions: List[commons.Description]
    moves: List[Move]
    names: List[basics.Name]


class MoveLearnMethod(BaseModel):
    id: int
    name: str
    descriptions: List[commons.Description]
    names: List[basics.Name]
    version_groups: List[games.VersionGroup]


class MoveTarget(BaseModel):
    id: int
    name: str
    descriptions: List[commons.Description]
    moves: List[Move]
    names: List[basics.Name]
