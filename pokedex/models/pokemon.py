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

from __future__ import annotations

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
    effect_entries: list[Effect]
    version_group: NamedAPIResource | None


class AbilityFlavorText(BaseModel):
    flavor_text: str
    language: NamedAPIResource | None
    version_group: NamedAPIResource | None


class AbilityPokemon(BaseModel):
    is_hidden: bool
    slot: int
    pokemon: NamedAPIResource | None


class Ability(BaseModel):
    """
    Abilities provide passive effects for Pokémon in battle or in the overworld. Pokémon have
    multiple possible abilities but can have only one ability at a time.
    """

    id: int
    name: str
    is_main_series: bool
    generation: NamedAPIResource | None
    names: list[Name]
    effect_entries: list[VerboseEffect]
    effect_changes: list[AbilityEffectChange]
    flavor_text_entries: list[AbilityFlavorText]
    pokemon: list[AbilityPokemon]


class Characteristic(BaseModel):
    """
    Characteristics indicate which stat contains a Pokémon's highest IV. A Pokémon's
    Characteristic is determined by the remainder of its highest IV divided by 5 (gene_modulo).
    """

    id: int
    gene_modulo: int
    possible_values: list[int]


class EggGroup(BaseModel):
    """
    Egg Groups are categories which determine which Pokémon are able to interbreed. Pokémon may
    belong to either one or two Egg Groups.
    """

    id: int
    name: str
    names: list[Name]
    pokemon_species: list[NamedAPIResource]


class PokemonSpeciesGender(BaseModel):
    rate: int
    pokemon_species: NamedAPIResource | None


class Gender(BaseModel):
    """
    Genders were introduced in Generation II for the purposes of breeding Pokémon but can also
    result in visual differences or even different evolutionary lines.
    """

    id: int
    name: str
    pokemon_species_details: list[PokemonSpeciesGender]
    required_for_evolution: list[NamedAPIResource]


class GrowthRateExperienceLevel(BaseModel):
    level: int
    experience: int


class GrowthRate(BaseModel):
    """Growth rates are the speed with which Pokémon gain levels through experience."""

    id: int
    name: str
    formula: str
    descriptions: list[Description]
    levels: list[GrowthRateExperienceLevel]
    pokemon_species: list[NamedAPIResource]


class NatureStatChange(BaseModel):
    max_change: int
    pokeathlon_stat: NamedAPIResource | None


class MoveBattleStylePreference(BaseModel):
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: NamedAPIResource | None


class Nature(BaseModel):
    """Natures influence how a Pokémon's stats grow."""

    id: int
    name: str
    decreased_stat: NamedAPIResource | None
    increased_stat: NamedAPIResource | None
    hates_flavor: NamedAPIResource | None
    likes_flavor: NamedAPIResource | None
    pokeathlon_stat_changes: list[NatureStatChange]
    move_battle_style_preferences: list[MoveBattleStylePreference]
    names: list[Name]


class NaturePokeathlonStatAffect(BaseModel):
    max_change: int
    nature: NamedAPIResource | None


class NaturePokeathlonStatAffectSets(BaseModel):
    increase: list[NaturePokeathlonStatAffect]
    decrease: list[NaturePokeathlonStatAffect]


class PokeathlonStat(BaseModel):
    """
    Pokeathlon Stats are different attributes of a Pokémon's performance in Pokéathlons. In
    Pokéathlons, competitions happen on different courses; one for each of the different
    Pokéathlon stats.
    """

    id: int
    name: str
    names: list[Name]
    affecting_natures: NaturePokeathlonStatAffectSets


class PokemonAbility(BaseModel):
    is_hidden: bool
    slot: int
    ability: NamedAPIResource | None


class PokemonHeldItemVersion(BaseModel):
    version: NamedAPIResource | None
    rarity: int


class PokemonHeldItem(BaseModel):
    item: NamedAPIResource | None
    version_details: list[PokemonHeldItemVersion]


class PokemonType(BaseModel):
    slot: int
    type: NamedAPIResource | None


class PokemonMoveVersion(BaseModel):
    move_learn_method: NamedAPIResource | None
    version_group: NamedAPIResource | None
    level_learned_at: int


class PokemonMove(BaseModel):
    move: NamedAPIResource | None
    version_group_details: list[PokemonMoveVersion]


class PokemonSprites(BaseModel):
    front_default: str | None
    front_shiny: str | None
    front_female: str | None
    front_shiny_female: str | None
    back_default: str | None
    back_shiny: str | None
    back_female: str | None
    back_shiny_female: str | None


class PokemonStat(BaseModel):
    stat: NamedAPIResource | None
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
    abilities: list[PokemonAbility]
    forms: list[NamedAPIResource]
    game_indices: list[VersionGameIndex]
    held_items: list[PokemonHeldItem]
    location_area_encounters: str
    moves: list[PokemonMove]
    sprites: PokemonSprites
    species: NamedAPIResource | None
    stats: list[PokemonStat]
    types: list[PokemonType]


class LocationAreaEncounter(BaseModel):
    location_area: NamedAPIResource | None
    version_details: list[VersionEncounterDetail]


class PokemonColor(BaseModel):
    """
    Colors used for sorting Pokémon in a Pokédex. The color listed in the Pokédex is usually the
    color most apparent or covering each Pokémon's body. No orange category exists; Pokémon that
    are primarily orange are listed as red or brown.
    """

    id: int
    name: str
    names: list[Name]
    pokemon_species: list[NamedAPIResource]


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
    pokemon: NamedAPIResource | None
    sprites: PokemonFormSprites
    version_group: NamedAPIResource | None
    names: list[Name]
    form_names: list[Name]


class PokemonHabitat(BaseModel):
    """
    Habitats are generally different terrain Pokémon can be found in but can also be areas
    designated for rare or legendary Pokémon.
    """

    id: int
    name: str
    names: list[Name]
    pokemon_species: list[NamedAPIResource]


class AwesomeName(BaseModel):
    awesome_name: str
    language: NamedAPIResource | None


class PokemonShape(BaseModel):
    """Shapes used for sorting Pokémon in a Pokédex."""

    id: int
    name: str
    awesome_names: list[AwesomeName]
    names: list[Name]
    pokemon_species: list[NamedAPIResource]


class PokemonSpeciesDexEntry(BaseModel):
    entry_number: int
    pokedex: NamedAPIResource | None


class PalParkEncounterArea(BaseModel):
    base_score: int
    rate: int
    area: NamedAPIResource | None


class Genus(BaseModel):
    genus: str
    language: NamedAPIResource | None


class PokemonSpeciesVariety(BaseModel):
    is_default: bool
    pokemon: NamedAPIResource | None


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
    growth_rate: NamedAPIResource | None
    pokedex_numbers: list[PokemonSpeciesDexEntry]
    egg_groups: list[NamedAPIResource]
    color: NamedAPIResource | None
    shape: NamedAPIResource | None
    evolves_from_species: NamedAPIResource | None
    evolution_chain: APIResource | None
    habitat: NamedAPIResource | None
    generation: NamedAPIResource | None
    names: list[Name]
    pal_park_encounters: list[PalParkEncounterArea]
    flavor_text_entries: list[FlavorText]
    form_descriptions: list[Description]
    genera: list[Genus]
    varieties: list[PokemonSpeciesVariety]


class MoveStatAffect(BaseModel):
    change: int | None
    move: NamedAPIResource | None


class MoveStatAffectSets(BaseModel):
    increase: MoveStatAffect
    decrease: MoveStatAffect


class NatureStatAffectSets(BaseModel):
    increase: list[NamedAPIResource]
    decrease: list[NamedAPIResource]


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
    characteristics: list[APIResource]
    move_damage_class: NamedAPIResource | None
    names: list[Name]


class TypeRelations(BaseModel):
    no_damage_to: list[NamedAPIResource]
    half_damage_to: list[NamedAPIResource]
    double_damage_to: list[NamedAPIResource]
    no_damage_from: list[NamedAPIResource]
    half_damage_from: list[NamedAPIResource]
    double_damage_from: list[NamedAPIResource]


class TypePokemon(BaseModel):
    slot: int
    pokemon: NamedAPIResource | None


class Type(BaseModel):
    """
    Types are properties for Pokémon and their moves. Each type has three properties: which types
    of Pokémon it is super effective against, which types of Pokémon it is not very effective
    against, and which types of Pokémon it is completely ineffective against.
    """

    id: int
    name: str
    damage_relations: TypeRelations
    game_indices: list[GenerationGameIndex]
    generation: NamedAPIResource | None
    move_damage_class: NamedAPIResource | None
    names: list[Name]
    pokemon: list[TypePokemon]
    moves: list[NamedAPIResource]
