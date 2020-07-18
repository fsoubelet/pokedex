import functools
from typing import Union

import requests
from loguru import logger

from pokedex.models import Pokemon


class PokeClient:
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
        logger.trace(f"Formatting query url for item_id '{item_id}'")
        return f"{self.base_url}/{item_type}/{item_id}/"

    @functools.lru_cache()
    def get_pokemon(self, pokemon_id: Union[str, int]) -> Pokemon:
        """
        Query a pokemon's data and return it organised in a Pokemon object.

        Args:
            pokemon_id (Union[str, int]): the pokemon's identifier, either its ID number or its
                                          name.

        Returns:
            A Pokemon oject of the item_id's data.
        """
        if not self._is_valid_id(pokemon_id):
            logger.error(
                f"The provided pokemon ID is of type '{type(pokemon_id)}' but should be "
                f"either 'int' or 'string'"
            )

        pokemon_query_url: str = self.format_query_url(item_id=pokemon_id, item_type="pokemon")

        logger.debug(f"Sending GET request for data for pokemon with ID '{pokemon_id}'")
        response: requests.Response = requests.get(pokemon_query_url)

        if response.status_code != 200:
            logger.error(f"Expected status code 200 but received {response.status_code}, aborting")
            quit()

        logger.debug(f"Formatting pokemon data into object")
        return Pokemon(**response.json())

    @staticmethod
    def _is_valid_id(provided_id: Union[str, int]) -> bool:
        """
        Returns the validity of the provided ID for use in PokeAPI: should be integer or string.

        Args:
            provided_id (Union[str, int]): the identifier to use in a query.

        Returns:
            True if the types are acceptable, False otherwise.
        """
        return isinstance(provided_id, str) or isinstance(provided_id, int)
