from typing import Dict, List

import requests
from loguru import logger
from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[Dict]
    forms: List[Dict]
    game_indices: List[Dict]
    held_items: List[Dict]
    location_area_encounters: str
    moves: List[Dict]
    sprites: Dict
    species: Dict
    stats: List[Dict]
    types: List[Dict]


def format_query_url(pokemon_name: str) -> str:
    """
    Returns the PokeAPI url to send a GET request to for a specific pokemon's information.

    Args:
        pokemon_name (str): the pokemon's name.

    Returns:
        The proper url.
    """
    logger.trace(f"Formatting query url for pokemon_name '{pokemon_name}'")
    return f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"


def pokemon_json(pokemon_name: str) -> Dict:
    """
    Send a request for the given Pokemon's data to the PokeAPI and return the queried data as a
    dictionary. The data is queried to the GET 'pokemon_name' endpoint.

    Args:
        pokemon_name (str): the pokemon_name's name.

    Returns:
        A dictionary of the pokemon_name's data.
    """
    query_url: str = format_query_url(pokemon_name)
    logger.debug(f"Sending GET request for data for pokemon '{pokemon_name}'")
    response: requests.Response = requests.get(query_url)

    if response.status_code != 200:
        logger.error(f"Expected status code 200 but received {response.status_code}, aborting")
        quit()

    return response.json()


def get_pokemon(pokemon_name: str) -> Pokemon:
    """
    Query a pokemon's data and return it organised in a Pokemon object.

    Args:
        pokemon_name (str): the pokemon_name's name.

    Returns:
        A Pokemon oject of the pokemon_name's data.
    """
    pokedict: dict = pokemon_json(pokemon_name)

    logger.debug(f"Formatting pokemon data into object")
    return Pokemon(**pokedict)
