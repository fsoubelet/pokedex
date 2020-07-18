from typing import List, Optional

from pydantic import BaseModel

from pokedex.models.commons import (
    APIResource,
    Description,
    Effect,
    FlavorText,
    GenerationGameIndex,
    Name,
    NamedAPIResource,
    VerboseEffect,
    VersionEncounterDetail,
    VersionGameIndex,
)


class AbilityEffectChange(BaseModel):
    effect_entries: List[Effect]
    version_group: NamedAPIResource


class AbilityFlavorText(BaseModel):
    flavor_text: str
    language: NamedAPIResource
    version_group: NamedAPIResource


class AbilityPokemon(BaseModel):
    is_hidden: bool
    slot: int
    pokemon: NamedAPIResource


class Ability(BaseModel):
    id: int
    name: str
    is_main_series: bool
    generation: NamedAPIResource
    names: List[Name]
    effect_entries: List[VerboseEffect]
    effect_changes: List[AbilityEffectChange]
    flavor_text_entries: List[AbilityFlavorText]
    pokemon: List[AbilityPokemon]


class Characteristic(BaseModel):
    id: int
    gene_modulo: int
    possible_values: List[int]


class EggGroup(BaseModel):
    id: int
    name: str
    names: List[Name]
    pokemon_species: List[NamedAPIResource]


class PokemonSpeciesGender(BaseModel):
    rate: int
    pokemon_species: NamedAPIResource


class Gender(BaseModel):
    id: int
    name: str
    pokemon_species_details: List[PokemonSpeciesGender]
    required_for_evolution: List[NamedAPIResource]


class GrowthRateExperienceLevel(BaseModel):
    level: int
    experience: int


class GrowthRate(BaseModel):
    id: int
    name: str
    formula: str
    descriptions: List[Description]
    levels: List[GrowthRateExperienceLevel]
    pokemon_species: List[NamedAPIResource]


class NatureStatChange(BaseModel):
    max_change: int
    pokeathlon_stat: NamedAPIResource


class MoveBattleStylePreference(BaseModel):
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: NamedAPIResource


class Nature(BaseModel):
    id: int
    name: str
    decreased_stat: NamedAPIResource
    increased_stat: NamedAPIResource
    hates_flavor: NamedAPIResource
    likes_flavor: NamedAPIResource
    pokeathlon_stat_changes: List[NatureStatChange]
    move_battle_style_preferences: List[MoveBattleStylePreference]
    names: List[Name]


class NaturePokeathlonStatAffect(BaseModel):
    max_change: int
    nature: NamedAPIResource


class NaturePokeathlonStatAffectSets(BaseModel):
    increase: List[NaturePokeathlonStatAffect]
    decrease: List[NaturePokeathlonStatAffect]


class PokeathlonStat(BaseModel):
    id: int
    name: str
    names: List[Name]
    affecting_natures: NaturePokeathlonStatAffectSets


class PokemonAbility(BaseModel):
    is_hidden: bool
    slot: int
    ability: NamedAPIResource


class PokemonHeldItemVersion(BaseModel):
    version: NamedAPIResource
    rarity: int


class PokemonHeldItem(BaseModel):
    item: NamedAPIResource
    version_details: List[PokemonHeldItemVersion]


class PokemonType(BaseModel):
    slot: int
    type: NamedAPIResource


class PokemonMoveVersion(BaseModel):
    move_learn_method: NamedAPIResource
    version_group: NamedAPIResource
    level_learned_at: int


class PokemonMove(BaseModel):
    move: NamedAPIResource
    version_group_details: List[PokemonMoveVersion]


class PokemonSprites(BaseModel):
    front_default: Optional[str]
    front_shiny: Optional[str]
    front_female: Optional[str]
    front_shiny_female: Optional[str]
    back_default: Optional[str]
    back_shiny: Optional[str]
    back_female: Optional[str]
    back_shiny_female: Optional[str]


class PokemonStat(BaseModel):
    stat: NamedAPIResource
    effort: int
    base_stat: int


class Pokemon(BaseModel):
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[PokemonAbility]
    forms: List[NamedAPIResource]
    game_indices: List[VersionGameIndex]
    held_items: List[PokemonHeldItem]
    location_area_encounters: str
    moves: List[PokemonMove]
    sprites: PokemonSprites
    species: NamedAPIResource
    stats: List[PokemonStat]
    types: List[PokemonType]


class LocationAreaEncounter(BaseModel):
    location_area: NamedAPIResource
    version_details: List[VersionEncounterDetail]


class PokemonColor(BaseModel):
    id: int
    name: str
    names: List[Name]
    pokemon_species: List[NamedAPIResource]


class PokemonFormSprites(BaseModel):
    front_default: str
    front_shiny: str
    back_default: str
    back_shiny: str


class PokemonForm(BaseModel):
    id: int
    name: str
    order: int
    form_order: int
    is_default: bool
    is_battle_only: bool
    is_mega: bool
    form_name: str
    pokemon: NamedAPIResource
    sprites: PokemonFormSprites
    version_group: NamedAPIResource
    names: List[Name]
    form_names: List[Name]


class PokemonHabitat(BaseModel):
    id: int
    name: str
    names: List[Name]
    pokemon_species: List[NamedAPIResource]


class AwesomeName(BaseModel):
    awesome_name: str
    language: NamedAPIResource


class PokemonShape(BaseModel):
    id: int
    name: str
    awesome_names: List[AwesomeName]
    names: List[Name]
    pokemon_species: List[NamedAPIResource]


class PokemonSpeciesDexEntry(BaseModel):
    entry_number: int
    pokedex: NamedAPIResource


class PalParkEncounterArea(BaseModel):
    base_score: int
    rate: int
    area: NamedAPIResource


class Genus(BaseModel):
    genus: str
    language: NamedAPIResource


class PokemonSpeciesVariety(BaseModel):
    is_default: bool
    pokemon: NamedAPIResource


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
    growth_rate: NamedAPIResource
    pokedex_numbers: List[PokemonSpeciesDexEntry]
    egg_groups: List[NamedAPIResource]
    color: NamedAPIResource
    shape: NamedAPIResource
    evolves_from_species: NamedAPIResource
    evolution_chain: APIResource
    habitat: NamedAPIResource
    generation: NamedAPIResource
    names: List[Name]
    pal_park_encounters: List[PalParkEncounterArea]
    flavor_text_entries: List[FlavorText]
    form_descriptions: List[Description]
    genera: List[Genus]
    varieties: List[PokemonSpeciesVariety]


class MoveStatAffect(BaseModel):
    change: int
    move: NamedAPIResource


class MoveStatAffectSets(BaseModel):
    increase: MoveStatAffect
    decrease: MoveStatAffect


class NatureStatAffectSets(BaseModel):
    increase: List[NamedAPIResource]
    decrease: List[NamedAPIResource]


class Stat(BaseModel):
    id: int
    name: str
    game_index: int
    is_battle_only: bool
    affecting_moves: MoveStatAffectSets
    affecting_natures: NatureStatAffectSets
    characteristics: List[APIResource]
    move_damage_class: NamedAPIResource
    names: List[Name]


class TypeRelations(BaseModel):
    no_damage_to: List[NamedAPIResource]
    half_damage_to: List[NamedAPIResource]
    double_damage_to: List[NamedAPIResource]
    no_damage_from: List[NamedAPIResource]
    half_damage_from: List[NamedAPIResource]
    double_damage_from: List[NamedAPIResource]


class TypePokemon(BaseModel):
    slot: int
    pokemon: NamedAPIResource


class Type(BaseModel):
    id: int
    name: str
    damage_relations: TypeRelations
    game_indices: List[GenerationGameIndex]
    generation: NamedAPIResource
    move_damage_class: NamedAPIResource
    names: List[Name]
    pokemon: List[TypePokemon]
    moves: List[NamedAPIResource]
