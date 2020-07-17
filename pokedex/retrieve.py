import requests


def get_pokemon_json(pokemon_name: str) -> dict:
    """
    Send a request for the given Pokemon's data to the PokeAPI and return the queried data as a
    dictionary. The data is queried to the GET 'pokemon' endpoint.

    Args:
        pokemon_name (str): the pokemon's name.

    Returns:
        A dictionary of the pokemon's info.
    """
    query_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(query_url)
