import functools
from typing import Union

import requests
from loguru import logger

from pokedex import models


class PokeClient:
    """
    High-level object to query data from the PokeAPI. The version 2 of the API is used, and each
    endpoint of the API is covered by a function from this client. Each of this functions makes
    use of an LRU cache to avoid querying results too many times. Beware, as that may be
    memory-intensive.
    """

    def __init__(self):
        self.base_url: str = "https://pokeapi.co/api/v2/"

    def format_query_url(self, item_id: Union[str, int], item_type: str) -> str:
        """
        Returns the PokeAPI url to send a GET request to for a specific pokemon's information.

        Args:
            item_id (Union[str, int]): the item's identifier, either its ID number or its name.
            item_type (str): the item's type, either a pokemon or a berry, etc.

        Returns:
            The proper url to send a GET request to.
        """
        logger.trace(f"Formatting query url for item_attribute_id '{item_id}'")
        return f"{self.base_url}/{item_type}/{item_id}/"

    @staticmethod
    def validate_id(provided_id: Union[str, int]) -> None:
        """
        Checks the validity of the provided ID for use in PokeAPI: should be integer or string.

        Args:
            provided_id (Union[str, int]): the identifier to use in a query.

        Returns:
            Nothing, but will raise a TypeError if validation is unsuccessful.
        """
        if not (isinstance(provided_id, str) or isinstance(provided_id, int)):
            logger.error(
                f"The provided pokemon ID is of type '{type(provided_id)}' but should be "
                f"either 'int' or 'string'"
            )
            raise TypeError("Invalid type for provided ID, should be either 'integer' or 'string'.")

    @staticmethod
    def validate_response_status(response: requests.Response) -> None:
        """
        Checks the validity of the provided response's status code, expecting 200.

        Args:
            response (requests.Response): the response of a GET request to the PokeAPI.

        Returns:
            Nothing, but will raise an exception if status code is not 200.
        """
        if response.status_code != 200:
            logger.error(f"Expected status code 200 but received {response.status_code}, aborting")
            raise Exception(
                f"GET request returned with status code {response.status_code}, when querying "
                f"address '{response.request.url}' check the validity of your parameter"
            )

    @functools.lru_cache()
    def get_berry(self, berry_id: Union[str, int]) -> models.Berry:
        """
        Query a berry's data and return it organised in a Berry object.

        Args:
            berry_id (Union[str, int]): the berry's identifier, either its ID number or its name.

        Returns:
            A pokedex.models.berries.Berry oject of the item's data.
        """
        self.validate_id(berry_id)
        berry_query_url: str = self.format_query_url(item_id=berry_id, item_type="berry")

        logger.debug(f"Sending GET request for data for berry with ID '{berry_id}'")
        response: requests.Response = requests.get(berry_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting berry data into Berry object")
        return models.Berry(**response.json())

    @functools.lru_cache()
    def get_berry_firmness(self, berry_firmness_id: Union[str, int]) -> models.BerryFirmness:
        """
        Query a berry firmness's data and return it organised in a BerryFirmness object.

        Args:
            berry_firmness_id (Union[str, int]): the berry firmness's identifier, either its ID
                                                 number or its name.

        Returns:
            A pokedex.models.berries.BerryFirmness oject of the item's data.
        """
        self.validate_id(berry_firmness_id)
        berry_firmness_query_url: str = self.format_query_url(
            item_id=berry_firmness_id, item_type="berry-firmness"
        )

        logger.debug(
            f"Sending GET request for data for berry firmness with ID '{berry_firmness_id}'"
        )
        response: requests.Response = requests.get(berry_firmness_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting berry firmness data into BerryFirmness object")
        return models.BerryFirmness(**response.json())

    @functools.lru_cache()
    def get_berry_flavor(self, berry_flavor_id: Union[str, int]) -> models.BerryFlavor:
        """
        Query a berry flavor's data and return it organised in a BerryFlavor object.

        Args:
            berry_flavor_id (Union[str, int]): the berry flavor's identifier, either its ID number
                                               or its name.

        Returns:
            A pokedex.models.berries.BerryFlavor oject of the item's data.
        """
        self.validate_id(berry_flavor_id)
        berry_flavor_query_url: str = self.format_query_url(
            item_id=berry_flavor_id, item_type="berry-flavor"
        )

        logger.debug(f"Sending GET request for data for berry flavor with ID '{berry_flavor_id}'")
        response: requests.Response = requests.get(berry_flavor_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting berry flavor data into BerryFlavor object")
        return models.BerryFlavor(**response.json())

    @functools.lru_cache()
    def get_contest_type(self, contest_type_id: Union[str, int]) -> models.ContestType:
        """
        Query a contest type's data and return it organised in a ContestType object.

        Args:
            contest_type_id (Union[str, int]): the contest type's identifier, either its ID number
                                               or its name.

        Returns:
            A pokedex.models.contests.ContestType oject of the item's data.
        """
        self.validate_id(contest_type_id)
        contest_type_query_url: str = self.format_query_url(
            item_id=contest_type_id, item_type="contest-type"
        )

        logger.debug(f"Sending GET request for data for contest type with ID '{contest_type_id}'")
        response: requests.Response = requests.get(contest_type_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting contest type data into ContestType object")
        return models.ContestType(**response.json())

    @functools.lru_cache()
    def get_contest_effect(self, contest_effect_id: Union[str, int]) -> models.ContestEffect:
        """
        Query a contest effect's data and return it organised in a ContestEffect object.

        Args:
            contest_effect_id (Union[str, int]): the contest effect's identifier, either its ID
                                                 number or its name.

        Returns:
            A pokedex.models.contests.ContestEffect oject of the item's data.
        """
        self.validate_id(contest_effect_id)
        contest_effect_query_url: str = self.format_query_url(
            item_id=contest_effect_id, item_type="contest-effect"
        )

        logger.debug(
            f"Sending GET request for data for contest effect with ID '{contest_effect_id}'"
        )
        response: requests.Response = requests.get(contest_effect_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting contest effect data into ContestEffect object")
        return models.ContestEffect(**response.json())

    @functools.lru_cache()
    def get_super_contest_effect(
        self, super_contest_effect_id: Union[str, int]
    ) -> models.SuperContestEffect:
        """
        Query a super contest effect's data and return it organised in a SuperContestEffect object.

        Args:
            super_contest_effect_id (Union[str, int]): the contest effect's identifier, either its
                                                       ID number or its name.

        Returns:
            A pokedex.models.contests.SuperContestEffect oject of the item's data.
        """
        self.validate_id(super_contest_effect_id)
        super_contest_effect_query_url: str = self.format_query_url(
            item_id=super_contest_effect_id, item_type="super-contest-effect"
        )

        logger.debug(
            f"Sending GET request for data for super contest effect with ID "
            f"'{super_contest_effect_id}'"
        )
        response: requests.Response = requests.get(super_contest_effect_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting super contest effect data into SuperContestEffect object")
        return models.SuperContestEffect(**response.json())

    @functools.lru_cache()
    def get_encounter_method(self, encounter_method_id: Union[str, int]) -> models.EncounterMethod:
        """
        Query an encounter method's data and return it organised in an EncounterMethod object.

        Args:
            encounter_method_id (Union[str, int]): the encounter method's identifier, either its ID
                                                   number or its name.

        Returns:
            A pokedex.models.encounters.EncounterMethod oject of the item's data.
        """
        self.validate_id(encounter_method_id)
        encounter_method_query_url: str = self.format_query_url(
            item_id=encounter_method_id, item_type="encounter-method"
        )

        logger.debug(
            f"Sending GET request for data for encounter method with ID '{encounter_method_id}'"
        )
        response: requests.Response = requests.get(encounter_method_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting encounter method data into EncounterMedhod object")
        return models.EncounterMethod(**response.json())

    @functools.lru_cache()
    def get_encounter_condition(
        self, encounter_condition_id: Union[str, int]
    ) -> models.EncounterCondition:
        """
        Query an encounter condition's data and return it organised in an EncounterCondition object.

        Args:
            encounter_condition_id (Union[str, int]): the encounter condition's identifier,
                                                      either its ID number or its name.

        Returns:
            A pokedex.models.encounters.EncounterCondition oject of the item's data.
        """
        self.validate_id(encounter_condition_id)
        encounter_condition_query_url: str = self.format_query_url(
            item_id=encounter_condition_id, item_type="encounter-condition"
        )

        logger.debug(
            f"Sending GET request for data for encounter condition with ID "
            f"'{encounter_condition_id}'"
        )
        response: requests.Response = requests.get(encounter_condition_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting encounter condition data into EncounterCondition object")
        return models.EncounterCondition(**response.json())

    @functools.lru_cache()
    def get_encounter_condition_value(
        self, encounter_condition_id: Union[str, int]
    ) -> models.EncounterConditionValue:
        """
        Query an encounter condition value's data and return it organised in an
        EncounterConditionValue object.

        Args:
            encounter_condition_id (Union[str, int]): the encounter condition value's identifier,
                                                      either its ID number or its name.

        Returns:
            A pokedex.models.encounters.EncounterConditionValue oject of the item's data.
        """
        self.validate_id(encounter_condition_id)
        encounter_condition_value_query_url: str = self.format_query_url(
            item_id=encounter_condition_id, item_type="encounter-condition-value"
        )

        logger.debug(
            f"Sending GET request for data for encounter condition value with ID "
            f"'{encounter_condition_id}'"
        )
        response: requests.Response = requests.get(encounter_condition_value_query_url)
        self.validate_response_status(response)

        logger.trace(
            f"Formatting encounter condition value data into EncounterConditionValue " f"object"
        )
        return models.EncounterConditionValue(**response.json())

    @functools.lru_cache()
    def get_evolution_chain(self, evolution_chain_id: Union[str, int]) -> models.EvolutionChain:
        """
        Query an evolution chain's data and return it organised in an EvolutionChain object.

        Args:
            evolution_chain_id (Union[str, int]): the evolution chain's identifier, either its ID
                                                  number or its name.

        Returns:
            A pokedex.models.evolution.EvolutionChain oject of the item's data.
        """
        self.validate_id(evolution_chain_id)
        evolution_chain_query_url: str = self.format_query_url(
            item_id=evolution_chain_id, item_type="evolution-chain"
        )

        logger.debug(
            f"Sending GET request for data for evolution chain with ID '{evolution_chain_id}'"
        )
        response: requests.Response = requests.get(evolution_chain_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting evolution chain data into EvolutionChain object")
        return models.EvolutionChain(**response.json())

    @functools.lru_cache()
    def get_evolution_trigger(
        self, evolution_trigger_id: Union[str, int]
    ) -> models.EvolutionTrigger:
        """
        Query an evolution trigger's data and return it organised in an EvolutionTrigger object.

        Args:
            evolution_trigger_id (Union[str, int]): the evolution trigger's identifier,
                                                    either its ID number or its name.

        Returns:
            A pokedex.models.evolution.EvolutionTrigger oject of the item's data.
        """
        self.validate_id(evolution_trigger_id)
        evolution_trigger_query_url: str = self.format_query_url(
            item_id=evolution_trigger_id, item_type="evolution-trigger"
        )

        logger.debug(
            f"Sending GET request for data for evolution trigger with ID '{evolution_trigger_id}'"
        )
        response: requests.Response = requests.get(evolution_trigger_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting evolution trigger data into EvolutionTrigger object")
        return models.EvolutionTrigger(**response.json())

    @functools.lru_cache()
    def get_generation(self, generation_id: Union[str, int]) -> models.Generation:
        """
        Query a generation's data and return it organised in a Generation object.

        Args:
            generation_id (Union[str, int]): the generation's identifier, either its ID number or
                                             its name.

        Returns:
            A pokedex.models.games.Generation oject of the item's data.
        """
        self.validate_id(generation_id)
        generation_query_url: str = self.format_query_url(
            item_id=generation_id, item_type="generation"
        )

        logger.debug(f"Sending GET request for data for generation with ID '{generation_id}'")
        response: requests.Response = requests.get(generation_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting generation data into Generation object")
        return models.Generation(**response.json())

    @functools.lru_cache()
    def get_pokedex(self, pokedex_id: Union[str, int]) -> models.Pokedex:
        """
        Query a pokedex's data and return it organised in a Pokedex object.

        Args:
            pokedex_id (Union[str, int]): the pokedex's identifier, either its ID number or
                                          its name.

        Returns:
            A pokedex.models.games.Pokedex oject of the item's data.
        """
        self.validate_id(pokedex_id)
        pokedex_query_url: str = self.format_query_url(item_id=pokedex_id, item_type="pokedex")

        logger.debug(f"Sending GET request for data for pokedex with ID '{pokedex_id}'")
        response: requests.Response = requests.get(pokedex_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting pokedex data into Pokedex object")
        return models.Pokedex(**response.json())

    @functools.lru_cache()
    def get_version(self, version_id: Union[str, int]) -> models.Version:
        """
        Query a version's data and return it organised in a Version object.

        Args:
            version_id (Union[str, int]): the version's identifier, either its ID number or
                                          its name.

        Returns:
            A pokedex.models.games.Version oject of the item's data.
        """
        self.validate_id(version_id)
        version_query_url: str = self.format_query_url(item_id=version_id, item_type="version")

        logger.debug(f"Sending GET request for data for version with ID '{version_id}'")
        response: requests.Response = requests.get(version_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting version data into Version object")
        return models.Version(**response.json())

    @functools.lru_cache()
    def get_version_group(self, version_group_id: Union[str, int]) -> models.VersionGroup:
        """
        Query a version group's data and return it organised in a VersionGroup object.

        Args:
            version_group_id (Union[str, int]): the version group's identifier, either its ID
                                                number or its name.

        Returns:
            A pokedex.models.games.VersionGroup oject of the item's data.
        """
        self.validate_id(version_group_id)
        version_group_query_url: str = self.format_query_url(
            item_id=version_group_id, item_type="version-group"
        )

        logger.debug(f"Sending GET request for data for version group with ID '{version_group_id}'")
        response: requests.Response = requests.get(version_group_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting version group data into VersionGroup object")
        return models.VersionGroup(**response.json())

    @functools.lru_cache()
    def get_item(self, item_id: Union[str, int]) -> models.Item:
        """
        Query an item's data and return it organised in an Item object.

        Args:
            item_id (Union[str, int]): the item's identifier, either its ID number or its name.

        Returns:
            A pokedex.models.items.Item oject of the item's data.
        """
        self.validate_id(item_id)
        item_query_url: str = self.format_query_url(item_id=item_id, item_type="item")

        logger.debug(f"Sending GET request for data for item with ID '{item_id}'")
        response: requests.Response = requests.get(item_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting item data into Item object")
        return models.Item(**response.json())

    @functools.lru_cache()
    def get_item_attribute(self, item_attribute_id: Union[str, int]) -> models.ItemAttribute:
        """
        Query an item attribute's data and return it organised in an ItemAttribute object.

        Args:
            item_attribute_id (Union[str, int]): the item attribute's identifier, either its ID
                                                 number or its name.

        Returns:
            A pokedex.models.items.ItemAttribute oject of the item's data.
        """
        self.validate_id(item_attribute_id)
        item_attribute_query_url: str = self.format_query_url(
            item_id=item_attribute_id, item_type="item-attribute"
        )

        logger.debug(
            f"Sending GET request for data for item attribute with ID '{item_attribute_id}'"
        )
        response: requests.Response = requests.get(item_attribute_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting item attribute data into ItemAttribute object")
        return models.ItemAttribute(**response.json())

    @functools.lru_cache()
    def get_item_category(self, item_category_id: Union[str, int]) -> models.ItemCategory:
        """
        Query an item category's data and return it organised in an ItemCategoru object.

        Args:
            item_category_id (Union[str, int]): the item category's identifier, either its ID
                                                number or its name.

        Returns:
            A pokedex.models.items.ItemCategory oject of the item's data.
        """
        self.validate_id(item_category_id)
        item_category_query_url: str = self.format_query_url(
            item_id=item_category_id, item_type="item-category"
        )

        logger.debug(f"Sending GET request for data for item category with ID '{item_category_id}'")
        response: requests.Response = requests.get(item_category_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting item category data into ItemCategory object")
        return models.ItemCategory(**response.json())

    @functools.lru_cache()
    def get_item_fling_effect(
        self, item_fling_effect_id: Union[str, int]
    ) -> models.ItemFlingEffect:
        """
        Query an item fling effect's data and return it organised in an ItemFlingEffect object.

        Args:
            item_fling_effect_id (Union[str, int]): the item fling effect's identifier,
                                                    either its ID number or its name.

        Returns:
            A pokedex.models.items.ItemFlingEffect oject of the item's data.
        """
        self.validate_id(item_fling_effect_id)
        item_fling_effect_query_url: str = self.format_query_url(
            item_id=item_fling_effect_id, item_type="item-fling-effect"
        )

        logger.debug(
            f"Sending GET request for data for item fling effect with ID '{item_fling_effect_id}'"
        )
        response: requests.Response = requests.get(item_fling_effect_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting item fling effect data into ItemFlingEffect object")
        return models.ItemFlingEffect(**response.json())

    @functools.lru_cache()
    def get_item_pocket(self, item_pocket_id: Union[str, int]) -> models.ItemPocket:
        """
        Query an item pocket's data and return it organised in an ItemPocket object.

        Args:
            item_pocket_id (Union[str, int]): the item pocket's identifier, either its ID number or
                                              its name.

        Returns:
            A pokedex.models.items.ItemPocket oject of the item's data.
        """
        self.validate_id(item_pocket_id)
        item_pocket_query_url: str = self.format_query_url(
            item_id=item_pocket_id, item_type="item-pocket"
        )

        logger.debug(f"Sending GET request for data for item pocket with ID '{item_pocket_id}'")
        response: requests.Response = requests.get(item_pocket_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting item pocket data into ItemPocket object")
        return models.ItemPocket(**response.json())

    @functools.lru_cache()
    def get_location(self, location_id: Union[str, int]) -> models.Location:
        """
        Query a location's data and return it organised in a Location object.

        Args:
            location_id (Union[str, int]): the location's identifier, either its ID number or its
                                           name.

        Returns:
            A pokedex.models.locations.Location oject of the item's data.
        """
        self.validate_id(location_id)
        location_query_url: str = self.format_query_url(item_id=location_id, item_type="location")

        logger.debug(f"Sending GET request for data for location with ID '{location_id}'")
        response: requests.Response = requests.get(location_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting location data into Location object")
        return models.Location(**response.json())

    @functools.lru_cache()
    def get_location_area(self, location_area_id: Union[str, int]) -> models.LocationArea:
        """
        Query a location area's data and return it organised in a LocationArea object.

        Args:
            location_area_id (Union[str, int]): the location area's identifier, either its ID
                                                number or its name.

        Returns:
            A pokedex.models.locations.LocationArea oject of the item's data.
        """
        self.validate_id(location_area_id)
        location_area_query_url: str = self.format_query_url(
            item_id=location_area_id, item_type="location-area"
        )

        logger.debug(f"Sending GET request for data for location area with ID '{location_area_id}'")
        response: requests.Response = requests.get(location_area_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting location area data into LocationArea object")
        return models.LocationArea(**response.json())

    @functools.lru_cache()
    def get_pal_park_area(self, pal_park_area_id: Union[str, int]) -> models.PalParkArea:
        """
        Query a pal park area's data and return it organised in a PalParkArea object.

        Args:
            pal_park_area_id (Union[str, int]): the pal park area's identifier, either its ID
                                                number or its name.

        Returns:
            A pokedex.models.locations.PalParkArea oject of the item's data.
        """
        self.validate_id(pal_park_area_id)
        pal_park_area_query_url: str = self.format_query_url(
            item_id=pal_park_area_id, item_type="pal-park-area"
        )

        logger.debug(f"Sending GET request for data for pal park area with ID '{pal_park_area_id}'")
        response: requests.Response = requests.get(pal_park_area_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting pal park area data into Location object")
        return models.PalParkArea(**response.json())

    @functools.lru_cache()
    def get_region(self, region_id: Union[str, int]) -> models.Region:
        """
        Query a region's data and return it organised in a Region object.

        Args:
            region_id (Union[str, int]): the region's identifier, either its ID number or its name.

        Returns:
            A pokedex.models.locations.Region oject of the item's data.
        """
        self.validate_id(region_id)
        region_query_url: str = self.format_query_url(item_id=region_id, item_type="region")

        logger.debug(f"Sending GET request for data for region with ID '{region_id}'")
        response: requests.Response = requests.get(region_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting region data into Region object")
        return models.Region(**response.json())

    @functools.lru_cache()
    def get_machine(self, machine_id: Union[str, int]) -> models.Machine:
        """
        Query a machine's data and return it organised in a Machine object.

        Args:
            machine_id (Union[str, int]): the machine's identifier, either its ID number or its
                                          name.

        Returns:
            A pokedex.models.machines.Machine oject of the item's data.
        """
        self.validate_id(machine_id)
        machine_query_url: str = self.format_query_url(item_id=machine_id, item_type="machine")

        logger.debug(f"Sending GET request for data for machine with ID '{machine_id}'")
        response: requests.Response = requests.get(machine_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting machine data into Machine object")
        return models.Machine(**response.json())

    @functools.lru_cache()
    def get_move(self, move_id: Union[str, int]) -> models.Move:
        """
        Query a move's data and return it organised in a Move object.

        Args:
            move_id (Union[str, int]): the move's identifier, either its ID number or its name.

        Returns:
            A pokedex.models.moves.Move oject of the item's data.
        """
        self.validate_id(move_id)
        move_query_url: str = self.format_query_url(item_id=move_id, item_type="move")

        logger.debug(f"Sending GET request for data for move with ID '{move_id}'")
        response: requests.Response = requests.get(move_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting move data into Move object")
        return models.Move(**response.json())

    @functools.lru_cache()
    def get_move_ailment(self, move_ailment_id: Union[str, int]) -> models.MoveAilment:
        """
        Query a move ailment's data and return it organised in a MoveAilment object.

        Args:
            move_ailment_id (Union[str, int]): the move ailment's identifier, either its ID number
                                               or its name.

        Returns:
            A pokedex.models.moves.MoveAilment oject of the item's data.
        """
        self.validate_id(move_ailment_id)
        move_ailment_query_url: str = self.format_query_url(
            item_id=move_ailment_id, item_type="move-ailment"
        )

        logger.debug(f"Sending GET request for data for move ailment with ID '{move_ailment_id}'")
        response: requests.Response = requests.get(move_ailment_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting move ailment data into MoveAilment object")
        return models.MoveAilment(**response.json())

    @functools.lru_cache()
    def get_move_battle_style(
        self, move_battle_style_id: Union[str, int]
    ) -> models.MoveBattleStyle:
        """
        Query a move battle style's data and return it organised in a MoveBattleStyle object.

        Args:
            move_battle_style_id (Union[str, int]): the move battle_style's identifier,
                                                    either its ID number or its name.

        Returns:
            A pokedex.models.moves.MoveBattleStyle oject of the item's data.
        """
        self.validate_id(move_battle_style_id)
        move_battle_style_query_url: str = self.format_query_url(
            item_id=move_battle_style_id, item_type="move-battle-style"
        )

        logger.debug(
            f"Sending GET request for data for move battle style with ID '{move_battle_style_id}'"
        )
        response: requests.Response = requests.get(move_battle_style_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting move battle style data into MoveBattleStyle object")
        return models.MoveBattleStyle(**response.json())

    @functools.lru_cache()
    def get_move_category(self, move_category_id: Union[str, int]) -> models.ModelName:
        """
        Query a move category's data and return it organised in a ModelName object.

        Args:
            move_category_id (Union[str, int]): the move category's identifier, either its ID
                                                number or its name.

        Returns:
            A pokedex.models.moves.ModelName oject of the item's data.
        """
        self.validate_id(move_category_id)
        move_category_query_url: str = self.format_query_url(
            item_id=move_category_id, item_type="move-category"
        )

        logger.debug(f"Sending GET request for data for move category with ID '{move_category_id}'")
        response: requests.Response = requests.get(move_category_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting move category data into ModelName object")
        return models.ModelName(**response.json())

    @functools.lru_cache()
    def get_move_damage_class(
        self, move_damage_class_id: Union[str, int]
    ) -> models.MoveDamageClass:
        """
        Query a move damage class's data and return it organised in a MoveDamageClass object.

        Args:
            move_damage_class_id (Union[str, int]): the move damage class's identifier,
                                                    either its ID number or its name.

        Returns:
            A pokedex.models.moves.MoveDamageClass oject of the item's data.
        """
        self.validate_id(move_damage_class_id)
        move_damage_class_query_url: str = self.format_query_url(
            item_id=move_damage_class_id, item_type="move-damage-class"
        )

        logger.debug(
            f"Sending GET request for data for move damage class with ID '{move_damage_class_id}'"
        )
        response: requests.Response = requests.get(move_damage_class_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting move damage class data into MoveDamageClass object")
        return models.MoveDamageClass(**response.json())

    @functools.lru_cache()
    def get_move_learn_method(
        self, move_learn_method_id: Union[str, int]
    ) -> models.MoveLearnMethod:
        """
        Query a move learn method's data and return it organised in a MoveLearnMethod object.

        Args:
            move_learn_method_id (Union[str, int]): the move learn method's identifier,
                                                    either its ID number or its name.

        Returns:
            A pokedex.models.moves.MoveLearnMethod oject of the item's data.
        """
        self.validate_id(move_learn_method_id)
        move_learn_method_query_url: str = self.format_query_url(
            item_id=move_learn_method_id, item_type="move-learn-method"
        )

        logger.debug(
            f"Sending GET request for data for move learn method with ID '{move_learn_method_id}'"
        )
        response: requests.Response = requests.get(move_learn_method_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting move learn method data into MoveLearnMethod object")
        return models.MoveLearnMethod(**response.json())

    @functools.lru_cache()
    def get_move_target(self, move_target_id: Union[str, int]) -> models.MoveTarget:
        """
        Query a move target's data and return it organised in a MoveTarget object.

        Args:
            move_target_id (Union[str, int]): the move target's identifier, either its ID number
                                              or its name.

        Returns:
            A pokedex.models.moves.MoveTarget oject of the item's data.
        """
        self.validate_id(move_target_id)
        move_target_query_url: str = self.format_query_url(
            item_id=move_target_id, item_type="move-target"
        )

        logger.debug(f"Sending GET request for data for move target with ID '{move_target_id}'")
        response: requests.Response = requests.get(move_target_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting move target data into Move object")
        return models.MoveTarget(**response.json())

    @functools.lru_cache()
    def get_ability(self, ability_id: Union[str, int]) -> models.Ability:
        """
        Query an ability's data and return it organised in an Ability object.

        Args:
            ability_id (Union[str, int]): the ability's identifier, either its ID number or its
                                          name.

        Returns:
            A pokedex.models.pokemon.Ability oject of the item's data.
        """
        self.validate_id(ability_id)
        ability_query_url: str = self.format_query_url(item_id=ability_id, item_type="ability")

        logger.debug(f"Sending GET request for data for ability with ID '{ability_id}'")
        response: requests.Response = requests.get(ability_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting ability data into Ability")
        return models.Ability(**response.json())

    @functools.lru_cache()
    def get_characteristic(self, characteristic_id: Union[str, int]) -> models.Characteristic:
        """
        Query a characteristic's data and return it organised in a Characteristic object.

        Args:
            characteristic_id (Union[str, int]): the characteristic's identifier, either its ID
                                                 number or its name.

        Returns:
            A pokedex.models.pokemon.Characteristic oject of the item's data.
        """
        self.validate_id(characteristic_id)
        characteristic_query_url: str = self.format_query_url(
            item_id=characteristic_id, item_type="characteristic"
        )

        logger.debug(
            f"Sending GET request for data for characteristic with ID '{characteristic_id}'"
        )
        response: requests.Response = requests.get(characteristic_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting characteristic data into Characteristic")
        return models.Characteristic(**response.json())

    @functools.lru_cache()
    def get_egg_group(self, egg_group_id: Union[str, int]) -> models.EggGroup:
        """
        Query an egg group's data and return it organised in an EggGroup object.

        Args:
            egg_group_id (Union[str, int]): the egg group's identifier, either its ID number or its
                                            name.

        Returns:
            A pokedex.models.pokemon.EggGroup oject of the item's data.
        """
        self.validate_id(egg_group_id)
        egg_group_query_url: str = self.format_query_url(
            item_id=egg_group_id, item_type="egg-group"
        )

        logger.debug(f"Sending GET request for data for egg group with ID '{egg_group_id}'")
        response: requests.Response = requests.get(egg_group_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting egg group data into EggGroup")
        return models.EggGroup(**response.json())

    @functools.lru_cache()
    def get_gender(self, gender_id: Union[str, int]) -> models.Gender:
        """
        Query a gender's data and return it organised in a Gender object.

        Args:
            gender_id (Union[str, int]): the gender's identifier, either its ID number or its name.

        Returns:
            A pokedex.models.pokemon.Gender oject of the item's data.
        """
        self.validate_id(gender_id)
        gender_query_url: str = self.format_query_url(item_id=gender_id, item_type="gender")

        logger.debug(f"Sending GET request for data for gender with ID '{gender_id}'")
        response: requests.Response = requests.get(gender_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting gender data into Gender object")
        return models.Gender(**response.json())

    @functools.lru_cache()
    def get_growth_rate(self, growth_rate_id: Union[str, int]) -> models.GrowthRate:
        """
        Query a growth rate's data and return it organised in a GrowthRate object.

        Args:
            growth_rate_id (Union[str, int]): the growth rate's identifier, either its ID number
                                              or its name.

        Returns:
            A pokedex.models.pokemon.GrowthRate oject of the item's data.
        """
        self.validate_id(growth_rate_id)
        growth_rate_query_url: str = self.format_query_url(
            item_id=growth_rate_id, item_type="growth-rate"
        )

        logger.debug(f"Sending GET request for data for growth rate with ID '{growth_rate_id}'")
        response: requests.Response = requests.get(growth_rate_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting growth rate data into GrowthRate object")
        return models.GrowthRate(**response.json())

    @functools.lru_cache()
    def get_nature(self, nature_id: Union[str, int]) -> models.Nature:
        """
        Query a nature's data and return it organised in a nature object.

        Args:
            nature_id (Union[str, int]): the nature's identifier, either its ID number or its name.

        Returns:
            A pokedex.models.pokemon.Nature oject of the item's data.
        """
        self.validate_id(nature_id)
        nature_query_url: str = self.format_query_url(item_id=nature_id, item_type="nature")

        logger.debug(f"Sending GET request for data for nature with ID '{nature_id}'")
        response: requests.Response = requests.get(nature_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting nature data into Nature object")
        return models.Nature(**response.json())

    @functools.lru_cache()
    def get_pokeathlon_stat(self, pokeathlon_stat_id: Union[str, int]) -> models.PokeathlonStat:
        """
        Query a pokeathlon stat's data and return it organised in a PokeathlonStat object.

        Args:
            pokeathlon_stat_id (Union[str, int]): the pokeathlon stat's identifier, either its ID
                                                  number or its name.

        Returns:
            A pokedex.models.pokemon.PokeathlonStat oject of the item's data.
        """
        self.validate_id(pokeathlon_stat_id)
        pokeathlon_stat_query_url: str = self.format_query_url(
            item_id=pokeathlon_stat_id, item_type="pokeathlon-stat"
        )

        logger.debug(
            f"Sending GET request for data for pokeathlon stat with ID '{pokeathlon_stat_id}'"
        )
        response: requests.Response = requests.get(pokeathlon_stat_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting pokeathlon stat data into PokeathlonStat object")
        return models.PokeathlonStat(**response.json())

    @functools.lru_cache()
    def get_pokemon(self, pokemon_id: Union[str, int]) -> models.Pokemon:
        """
        Query a pokemon's data and return it organised in a Pokemon object.

        Args:
            pokemon_id (Union[str, int]): the pokemon's identifier, either its ID number or its
                                          name.

        Returns:
            A pokedex.models.pokemon.Pokemon oject of the item's data.
        """
        self.validate_id(pokemon_id)
        pokemon_query_url: str = self.format_query_url(item_id=pokemon_id, item_type="pokemon")

        logger.debug(f"Sending GET request for data for pokemon with ID '{pokemon_id}'")
        response: requests.Response = requests.get(pokemon_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting pokemon data into Pokemon object")
        return models.Pokemon(**response.json())

    @functools.lru_cache()
    def get_pokemon_color(self, pokemon_color_id: Union[str, int]) -> models.PokemonColor:
        """
        Query a pokemon color's data and return it organised in a PokemonColor object.

        Args:
            pokemon_color_id (Union[str, int]): the pokemon color's identifier, either its ID number
                                                or its name.

        Returns:
            A pokedex.models.pokemon.PokemonColor oject of the item's data.
        """
        self.validate_id(pokemon_color_id)
        pokemon_color_query_url: str = self.format_query_url(
            item_id=pokemon_color_id, item_type="pokemon-color"
        )

        logger.debug(f"Sending GET request for data for pokemon color with ID '{pokemon_color_id}'")
        response: requests.Response = requests.get(pokemon_color_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting pokemon color data into PokemonColor object")
        return models.PokemonColor(**response.json())

    @functools.lru_cache()
    def get_pokemon_form(self, pokemon_id: Union[str, int]) -> models.PokemonForm:
        """
        Query a pokemon form's data and return it organised in a PokemonForm object.

        Args:
            pokemon_id (Union[str, int]): the pokemon form's identifier, either its ID number or its
                                          name.

        Returns:
            A pokedex.models.pokemon.PokemonForm oject of the item's data.
        """
        self.validate_id(pokemon_id)
        pokemon_form_query_url: str = self.format_query_url(
            item_id=pokemon_id, item_type="pokemon-form"
        )

        logger.debug(f"Sending GET request for data for pokemon form with ID '{pokemon_id}'")
        response: requests.Response = requests.get(pokemon_form_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting pokemon form data into PokemonForm object")
        return models.PokemonForm(**response.json())

    @functools.lru_cache()
    def get_pokemon_habitat(self, pokemon_habitat_id: Union[str, int]) -> models.PokemonHabitat:
        """
        Query a pokemon habitat's data and return it organised in a PokemonHabitat object.

        Args:
            pokemon_habitat_id (Union[str, int]): the pokemon habitat's identifier, either its ID
                                                  number or its name.

        Returns:
            A pokedex.models.pokemon.PokemonHabitat oject of the item's data.
        """
        self.validate_id(pokemon_habitat_id)
        pokemon_habitat_query_url: str = self.format_query_url(
            item_id=pokemon_habitat_id, item_type="pokemon-habitat"
        )

        logger.debug(
            f"Sending GET request for data for pokemon habitat with ID '{pokemon_habitat_id}'"
        )
        response: requests.Response = requests.get(pokemon_habitat_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting pokemon habitat data into PokemonHabitat object")
        return models.PokemonHabitat(**response.json())

    @functools.lru_cache()
    def get_pokemon_shape(self, pokemon_shape_id: Union[str, int]) -> models.PokemonShape:
        """
        Query a pokemon shape's data and return it organised in a PokemonShape object.

        Args:
            pokemon_shape_id (Union[str, int]): the pokemon shape's identifier, either its ID
                                                number or its name.

        Returns:
            A pokedex.models.pokemon.PokemonShape oject of the item's data.
        """
        self.validate_id(pokemon_shape_id)
        pokemon_shape_query_url: str = self.format_query_url(
            item_id=pokemon_shape_id, item_type="pokemon-shape"
        )

        logger.debug(f"Sending GET request for data for pokemon shape with ID '{pokemon_shape_id}'")
        response: requests.Response = requests.get(pokemon_shape_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting pokemon shape data into PokemonShape object")
        return models.PokemonShape(**response.json())

    @functools.lru_cache()
    def get_pokemon_species(self, pokemon_species_id: Union[str, int]) -> models.PokemonSpecies:
        """
        Query a pokemon species's data and return it organised in a PokemonSpecies object.

        Args:
            pokemon_species_id (Union[str, int]): the pokemon species's identifier, either its ID
                                                  number or its name.

        Returns:
            A pokedex.models.pokemon.PokemonSpecies oject of the item's data.
        """
        self.validate_id(pokemon_species_id)
        pokemon_species_query_url: str = self.format_query_url(
            item_id=pokemon_species_id, item_type="pokemon-species"
        )

        logger.debug(
            f"Sending GET request for data for pokemon species with ID '{pokemon_species_id}'"
        )
        response: requests.Response = requests.get(pokemon_species_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting pokemon species data into PokemonSpecies object")
        return models.PokemonSpecies(**response.json())

    @functools.lru_cache()
    def get_stat(self, stat_id: Union[str, int]) -> models.Stat:
        """
        Query a stat's data and return it organised in a Stat object.

        Args:
            stat_id (Union[str, int]): the stat's identifier, either its ID number or its name.

        Returns:
            A pokedex.models.pokemon.Stat oject of the item's data.
        """
        self.validate_id(stat_id)
        stat_query_url: str = self.format_query_url(item_id=stat_id, item_type="stat")

        logger.debug(f"Sending GET request for data for stat with ID '{stat_id}'")
        response: requests.Response = requests.get(stat_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting stat data into Stat object")
        return models.Stat(**response.json())

    @functools.lru_cache()
    def get_type(self, type_id: Union[str, int]) -> models.Type:
        """
        Query a type's data and return it organised in a Type object.

        Args:
            type_id (Union[str, int]): the type's identifier, either its ID number or its name.

        Returns:
            A pokedex.models.pokemon.Type oject of the item's data.
        """
        self.validate_id(type_id)
        type_query_url: str = self.format_query_url(item_id=type_id, item_type="type")

        logger.debug(f"Sending GET request for data for type with ID '{type_id}'")
        response: requests.Response = requests.get(type_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting type data into Type object")
        return models.Type(**response.json())

    @functools.lru_cache()
    def get_language(self, language_id: Union[str, int]) -> models.Language:
        """
        Query a language's data and return it organised in a Language object.

        Args:
            language_id (Union[str, int]): the language's identifier, either its ID number or its
                                           name.

        Returns:
            A pokedex.models.commons.Language oject of the item's data.
        """
        self.validate_id(language_id)
        language_query_url: str = self.format_query_url(item_id=language_id, item_type="language")

        logger.debug(f"Sending GET request for data for language with ID '{language_id}'")
        response: requests.Response = requests.get(language_query_url)
        self.validate_response_status(response)

        logger.trace(f"Formatting language data into Language object")
        return models.Language(**response.json())
