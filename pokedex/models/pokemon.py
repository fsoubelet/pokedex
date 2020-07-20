"""
Model classes for the 'Pokémon' endpoint objects. Available endpoints are:
- Abilities (https://pokeapi.co/api/v2/ability/{id or name}/)
- Characteristics (https://pokeapi.co/api/v2/characteristic/{id}/)
- Egg Groups (https://pokeapi.co/api/v2/egg-group/{id or name}/)
- Genders (https://pokeapi.co/api/v2/gender/{id or name}/)
- Growth Rates (https://pokeapi.co/api/v2/growth-rate/{id or name}/)
- Natures (https://pokeapi.co/api/v2/nature/{id or name}/)
- Pokeathlon Stats (https://pokeapi.co/api/v2/pokeathlon-stat/{id or name}/)
- Pokemon (https://pokeapi.co/api/v2/pokemon/{id or name}/)
- Pokemon Colors (https://pokeapi.co/api/v2/pokemon-color/{id or name}/)
- Pokemon Forms (https://pokeapi.co/api/v2/pokemon-form/{id or name}/)
- Pokemon Habitats (https://pokeapi.co/api/v2/pokemon-habitat/{id or name}/)
- Pokemon Shapes (https://pokeapi.co/api/v2/pokemon-shape/{id or name}/)
- Pokemon Species (https://pokeapi.co/api/v2/pokemon-species/{id or name}/)
- Stats (https://pokeapi.co/api/v2/stat/{id or name}/)
- Types (https://pokeapi.co/api/v2/type/{id or name}/)
"""

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
    version_group: Optional[NamedAPIResource]


class AbilityFlavorText(BaseModel):
    flavor_text: str
    language: Optional[NamedAPIResource]
    version_group: Optional[NamedAPIResource]


class AbilityPokemon(BaseModel):
    is_hidden: bool
    slot: int
    pokemon: Optional[NamedAPIResource]


class Ability(BaseModel):
    """
    Abilities provide passive effects for Pokémon in battle or in the overworld. Pokémon have
    multiple possible abilities but can have only one ability at a time.
    """

    id: int
    name: str
    is_main_series: bool
    generation: Optional[NamedAPIResource]
    names: List[Name]
    effect_entries: List[VerboseEffect]
    effect_changes: List[AbilityEffectChange]
    flavor_text_entries: List[AbilityFlavorText]
    pokemon: List[AbilityPokemon]


class Characteristic(BaseModel):
    """
    Characteristics indicate which stat contains a Pokémon's highest IV. A Pokémon's
    Characteristic is determined by the remainder of its highest IV divided by 5 (gene_modulo).
    """

    id: int
    gene_modulo: int
    possible_values: List[int]


class EggGroup(BaseModel):
    """
    Egg Groups are categories which determine which Pokémon are able to interbreed. Pokémon may
    belong to either one or two Egg Groups.
    """

    id: int
    name: str
    names: List[Name]
    pokemon_species: List[NamedAPIResource]


class PokemonSpeciesGender(BaseModel):
    rate: int
    pokemon_species: Optional[NamedAPIResource]


class Gender(BaseModel):
    """
    Genders were introduced in Generation II for the purposes of breeding Pokémon but can also
    result in visual differences or even different evolutionary lines.
    """

    id: int
    name: str
    pokemon_species_details: List[PokemonSpeciesGender]
    required_for_evolution: List[NamedAPIResource]


class GrowthRateExperienceLevel(BaseModel):
    level: int
    experience: int


class GrowthRate(BaseModel):
    """Growth rates are the speed with which Pokémon gain levels through experience."""

    id: int
    name: str
    formula: str
    descriptions: List[Description]
    levels: List[GrowthRateExperienceLevel]
    pokemon_species: List[NamedAPIResource]


class NatureStatChange(BaseModel):
    max_change: int
    pokeathlon_stat: Optional[NamedAPIResource]


class MoveBattleStylePreference(BaseModel):
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: Optional[NamedAPIResource]


class Nature(BaseModel):
    """Natures influence how a Pokémon's stats grow."""

    id: int
    name: str
    decreased_stat: Optional[NamedAPIResource]
    increased_stat: Optional[NamedAPIResource]
    hates_flavor: Optional[NamedAPIResource]
    likes_flavor: Optional[NamedAPIResource]
    pokeathlon_stat_changes: List[NatureStatChange]
    move_battle_style_preferences: List[MoveBattleStylePreference]
    names: List[Name]


class NaturePokeathlonStatAffect(BaseModel):
    max_change: int
    nature: Optional[NamedAPIResource]


class NaturePokeathlonStatAffectSets(BaseModel):
    increase: List[NaturePokeathlonStatAffect]
    decrease: List[NaturePokeathlonStatAffect]


class PokeathlonStat(BaseModel):
    """
    Pokeathlon Stats are different attributes of a Pokémon's performance in Pokéathlons. In
    Pokéathlons, competitions happen on different courses; one for each of the different
    Pokéathlon stats.
    """

    id: int
    name: str
    names: List[Name]
    affecting_natures: NaturePokeathlonStatAffectSets


class PokemonAbility(BaseModel):
    is_hidden: bool
    slot: int
    ability: Optional[NamedAPIResource]


class PokemonHeldItemVersion(BaseModel):
    version: Optional[NamedAPIResource]
    rarity: int


class PokemonHeldItem(BaseModel):
    item: Optional[NamedAPIResource]
    version_details: List[PokemonHeldItemVersion]


class PokemonType(BaseModel):
    slot: int
    type: Optional[NamedAPIResource]


class PokemonMoveVersion(BaseModel):
    move_learn_method: Optional[NamedAPIResource]
    version_group: Optional[NamedAPIResource]
    level_learned_at: int


class PokemonMove(BaseModel):
    move: Optional[NamedAPIResource]
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
    stat: Optional[NamedAPIResource]
    effort: int
    base_stat: int


class Pokemon(BaseModel):
    """
    Pokémon are the creatures that inhabit the world of the Pokémon games. They can be caught
    using Pokéballs and trained by battling with other Pokémon. Each Pokémon belongs to a
    specific species but may take on a variant which makes it differ from other Pokémon of the
    same species, such as base stats, available abilities and typings.
    """

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
    species: Optional[NamedAPIResource]
    stats: List[PokemonStat]
    types: List[PokemonType]


class LocationAreaEncounter(BaseModel):
    location_area: Optional[NamedAPIResource]
    version_details: List[VersionEncounterDetail]


class PokemonColor(BaseModel):
    """
    Colors used for sorting Pokémon in a Pokédex. The color listed in the Pokédex is usually the
    color most apparent or covering each Pokémon's body. No orange category exists; Pokémon that
    are primarily orange are listed as red or brown.
    """

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
    """
    Some Pokémon may appear in one of multiple, visually different forms. These differences are
    purely cosmetic. For variations within a Pokémon species, which do differ in more than just
    visuals, the 'Pokémon' entity is used to represent such a variety.
    """

    id: int
    name: str
    order: int
    form_order: int
    is_default: bool
    is_battle_only: bool
    is_mega: bool
    form_name: str
    pokemon: Optional[NamedAPIResource]
    sprites: PokemonFormSprites
    version_group: Optional[NamedAPIResource]
    names: List[Name]
    form_names: List[Name]


class PokemonHabitat(BaseModel):
    """
    Habitats are generally different terrain Pokémon can be found in but can also be areas
    designated for rare or legendary Pokémon.
    """

    id: int
    name: str
    names: List[Name]
    pokemon_species: List[NamedAPIResource]


class AwesomeName(BaseModel):
    awesome_name: str
    language: Optional[NamedAPIResource]


class PokemonShape(BaseModel):
    """Shapes used for sorting Pokémon in a Pokédex."""

    id: int
    name: str
    awesome_names: List[AwesomeName]
    names: List[Name]
    pokemon_species: List[NamedAPIResource]


class PokemonSpeciesDexEntry(BaseModel):
    entry_number: int
    pokedex: Optional[NamedAPIResource]


class PalParkEncounterArea(BaseModel):
    base_score: int
    rate: int
    area: Optional[NamedAPIResource]


class Genus(BaseModel):
    genus: str
    language: Optional[NamedAPIResource]


class PokemonSpeciesVariety(BaseModel):
    is_default: bool
    pokemon: Optional[NamedAPIResource]


class PokemonSpecies(BaseModel):
    """
    A Pokémon Species forms the basis for at least one Pokémon. Attributes of a Pokémon species
    are shared across all varieties of Pokémon within the species. A good example is Wormadam;
    Wormadam is the species which can be found in three different varieties, Wormadam-Trash,
    Wormadam-Sandy and Wormadam-Plant.
    """

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
    growth_rate: Optional[NamedAPIResource]
    pokedex_numbers: List[PokemonSpeciesDexEntry]
    egg_groups: List[NamedAPIResource]
    color: Optional[NamedAPIResource]
    shape: Optional[NamedAPIResource]
    evolves_from_species: Optional[NamedAPIResource]
    evolution_chain: Optional[APIResource]
    habitat: Optional[NamedAPIResource]
    generation: Optional[NamedAPIResource]
    names: List[Name]
    pal_park_encounters: List[PalParkEncounterArea]
    flavor_text_entries: List[FlavorText]
    form_descriptions: List[Description]
    genera: List[Genus]
    varieties: List[PokemonSpeciesVariety]


class MoveStatAffect(BaseModel):
    change: Optional[int]
    move: Optional[NamedAPIResource]


class MoveStatAffectSets(BaseModel):
    increase: MoveStatAffect
    decrease: MoveStatAffect


class NatureStatAffectSets(BaseModel):
    increase: List[NamedAPIResource]
    decrease: List[NamedAPIResource]


class Stat(BaseModel):
    """
    Stats determine certain aspects of battles. Each Pokémon has a value for each stat which
    grows as they gain levels and can be altered momentarily by effects in battles.
    """

    id: int
    name: str
    game_index: int
    is_battle_only: bool
    affecting_moves: MoveStatAffectSets
    affecting_natures: NatureStatAffectSets
    characteristics: List[APIResource]
    move_damage_class: Optional[NamedAPIResource]
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
    pokemon: Optional[NamedAPIResource]


class Type(BaseModel):
    """
    Types are properties for Pokémon and their moves. Each type has three properties: which types
    of Pokémon it is super effective against, which types of Pokémon it is not very effective
    against, and which types of Pokémon it is completely ineffective against.
    """

    id: int
    name: str
    damage_relations: TypeRelations
    game_indices: List[GenerationGameIndex]
    generation: Optional[NamedAPIResource]
    move_damage_class: Optional[NamedAPIResource]
    names: List[Name]
    pokemon: List[TypePokemon]
    moves: List[NamedAPIResource]
