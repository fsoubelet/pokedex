"""
Model classes for the 'Machines' endpoint objects. Available endpoints are:
- Machines (https://pokeapi.co/api/v2/machine/{id}/)
"""

from pydantic import BaseModel

from pokedex.models.commons import NamedAPIResource


class Machine(BaseModel):
    """
    Machines are the representation of items that teach moves to Pokémon. They vary from version
    to version, so it is not certain that one specific TM or HM corresponds to a single Machine.
    """
    id: int
    item: NamedAPIResource
    move: NamedAPIResource
    version_group: NamedAPIResource
