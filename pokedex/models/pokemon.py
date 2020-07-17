from typing import List

from pydantic import BaseModel

from pokedex.models.basics import Language, Name
from pokedex.models.berries import BerryFlavor
from pokedex.models.commons import (
    Description,
    Effect,
    FlavorText,
    GenerationGameIndex,
    VerboseEffect,
    VersionEncounterDetail,
    VersionGameIndex,
)
from pokedex.models.evolution import EvolutionChain
from pokedex.models.games import Generation, Pokedex, Version, VersionGroup
from pokedex.models.items import Item
from pokedex.models.locations import LocationArea, PalParkArea
from pokedex.models.moves import Move, MoveBattleStyle, MoveDamageClass, MoveLearnMethod


class Ability(BaseModel):
    id: int
    name: str
    is_main_series: bool
    generation: Generation
    names: List[Name]
    effect_entries: List[VerboseEffect]
    effect_changes: List[AbilityEffectChange]
    flavor_text_entries: List[AbilityFlavorText]
    pokemon: List[AbilityPokemon]


class AbilityEffectChange(BaseModel):
    effect_entries: List[Effect]
    version_group: VersionGroup


class AbilityFlavorText(BaseModel):
    flavor_text: str
    language: Language
    version_group: VersionGroup


class AbilityPokemon(BaseModel):
    is_hidden: bool
    slot: int
    pokemon: Pokemon


class Characteristic(BaseModel):
    id: int
    gene_modulo: int
    possible_values: List[int]


class EggGroup(BaseModel):
    id: int
    name: str
    names: List[Name]
    pokemon_species: List[PokemonSpecies]


class Gender(BaseModel):
    id: int
    name: str
    pokemon_species_details: List[PokemonSpeciesGender]
    required_for_evolution: List[PokemonSpecies]


class PokemonSpeciesGender(BaseModel):
    rate: int
    pokemon_species: PokemonSpecies


class GrowthRate(BaseModel):
    id: int
    name: str
    formula: str
    descriptions: List[Description]
    levels: List[GrowthRateExperienceLevel]
    pokemon_species: List[PokemonSpecies]


class GrowthRateExperienceLevel(BaseModel):
    level: int
    experience: int


class Nature(BaseModel):
    id: int
    name: str
    decreased_stat: Stat
    increased_stat: Stat
    hates_flavor: BerryFlavor
    likes_flavor: BerryFlavor
    pokeathlon_stat_changes: List[NatureStatChange]
    move_battle_style_preferences: List[MoveBattleStylePreference]
    names: List[Name]


class NatureStatChange(BaseModel):
    max_change: int
    pokeathlon_stat: PokeathlonStat


class MoveBattleStylePreference(BaseModel):
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: MoveBattleStyle


class PokeathlonStat(BaseModel):
    id: int
    name: str
    names: List[Name]
    affecting_natures: NaturePokeathlonStatAffectSets


class NaturePokeathlonStatAffectSets(BaseModel):
    increase: List[NaturePokeathlonStatAffect]
    decrease: List[NaturePokeathlonStatAffect]


class NaturePokeathlonStatAffect(BaseModel):
    max_change: int
    nature: Nature


class Pokemon(BaseModel):
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[PokemonAbility]
    forms: List[PokemonForm]
    game_indices: List[VersionGameIndex]
    held_items: List[PokemonHeldItem]
    location_area_encounters: str
    moves: List[PokemonMove]
    sprites: PokemonSprites
    species: PokemonSpecies
    stats: List[PokemonStat]
    types: List[PokemonType]


class PokemonAbility(BaseModel):
    is_hidden: bool
    slot: int
    ability: Ability


class PokemonType(BaseModel):
    slot: int
    type: Type


class PokemonHeldItem(BaseModel):
    item: Item
    version_details: List[PokemonHeldItemVersion]


class PokemonHeldItemVersion(BaseModel):
    version: Version
    rarity: int


class PokemonMove(BaseModel):
    move: Move
    version_group_details: List[PokemonMoveVersion]


class PokemonMoveVersion(BaseModel):
    move_learn_method: MoveLearnMethod
    version_group: VersionGroup
    level_learned_at: int


class PokemonStat(BaseModel):
    stat: Stat
    effort: int
    base_stat: int


class PokemonSprites(BaseModel):
    front_default: str
    front_shiny: str
    front_female: str
    front_shiny_female: str
    back_default: str
    back_shiny: str
    back_female: str
    back_shiny_female: str


class LocationAreaEncounter(BaseModel):
    location_area: LocationArea
    version_details: VersionEncounterDetail


class PokemonColor(BaseModel):
    id: int
    name: str
    names: List[Name]
    pokemon_species: List[PokemonSpecies]


class PokemonForm(BaseModel):
    id: int
    name: str
    order: int
    form_order: int
    is_default: bool
    is_battle_only: bool
    is_mega: bool
    form_name: str
    pokemon: Pokemon
    sprites: PokemonFormSprites
    version_group: VersionGroup
    names: List[Name]
    form_names: List[Name]


class PokemonFormSprites(BaseModel):
    front_default: str
    front_shiny: str
    back_default: str
    back_shiny: str


class PokemonHabitat(BaseModel):
    id: int
    name: str
    names: List[Name]
    pokemon_species: List[PokemonSpecies]


class PokemonShape(BaseModel):
    id: int
    name: str
    awesome_names: List[AwesomeName]
    names: List[Name]
    pokemon_species: List[PokemonSpecies]


class AwesomeName(BaseModel):
    awesome_name: str
    language: Language


class PokemonSpecies(BaseModel):
    id: int
    name: str
    order: int
    gender_rate: int
    capture_rate: int
    base_happiness: int
    is_baby: bool
    hatch_counter: int
    has_gender_differences: bool
    forms_switchable: bool
    growth_rate: GrowthRate
    pokedex_numbers: List[PokemonSpeciesDexEntry]
    egg_groups: List[EggGroup]
    color: PokemonColor
    shape: PokemonShape
    evolves_from_species: PokemonSpecies
    evolution_chain: EvolutionChain
    habitat: PokemonHabitat
    generation: Generation
    names: List[Name]
    pal_park_encounters: List[PalParkEncounterArea]
    flavor_text_entries: List[FlavorText]
    form_descriptions: List[Description]
    genera: List[Genus]
    varieties: List[PokemonSpeciesVariety]


class Genus(BaseModel):
    genus: str
    language: Language


class PokemonSpeciesDexEntry(BaseModel):
    entry_number: int
    pokedex: Pokedex


class PalParkEncounterArea(BaseModel):
    base_score: int
    rate: int
    area: PalParkArea


class PokemonSpeciesVariety(BaseModel):
    is_default: bool
    pokemon: Pokemon


class Stat(BaseModel):
    id: int
    name: str
    game_index: int
    is_battle_only: bool
    affecting_moves: MoveStatAffectSets
    affecting_natures: NatureStatAffectSets
    characteristics: List[Characteristic]
    move_damage_class: MoveDamageClass
    names: List[Name]


class MoveStatAffectSets(BaseModel):
    increase: MoveStatAffect
    decrease: MoveStatAffect


class MoveStatAffect(BaseModel):
    change: int
    move: Move


class NatureStatAffectSets(BaseModel):
    increase: Nature
    decrease: Nature


class Type(BaseModel):
    id: int
    name: str
    damage_relations: TypeRelations
    game_indices: List[GenerationGameIndex]
    generation: Generation
    move_damage_class: MoveDamageClass
    names: List[Name]
    pokemon: List[Pokemon]
    moves: List[Move]


class TypePokemon(BaseModel):
    slot: int
    pokemon: Pokemon


class TypeRelations(BaseModel):
    no_damage_to: List[Type]
    half_damage_to: List[Type]
    double_damage_to: List[Type]
    no_damage_from: List[Type]
    half_damage_from: List[Type]
    double_damage_from: List[Type]
