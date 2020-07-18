from typing import Dict, List, Union

import requests
from loguru import logger

from pokedex.models.pokemon import Pokemon


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

    def get_pokemon(self, pokemon_id: Union[str, int]) -> Pokemon:
        """
        Query a pokemon's data and return it organised in a Pokemon object.

        Args:
            pokemon_id (Union[str, int]): the pokemon's identifier, either its ID number or its
                                          name.

        Returns:
            A Pokemon oject of the item_id's data.
        """
        pokemon_query_url: str = self.format_query_url(pokemon_id)

        logger.debug(f"Sending GET request for data for pokemon '{pokemon_id}'")
        response: requests.Response = requests.get(query_url)

        if response.status_code != 200:
            logger.error(f"Expected status code 200 but received {response.status_code}, aborting")
            quit()

        logger.debug(f"Formatting pokemon data into object")
        return Pokemon(**response.json())
