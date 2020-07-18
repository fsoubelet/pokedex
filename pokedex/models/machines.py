from pydantic import BaseModel

from pokedex.models.commons import NamedAPIResource


class Machine(BaseModel):
    id: int
    item: NamedAPIResource
    move: NamedAPIResource
    version_group: NamedAPIResource
