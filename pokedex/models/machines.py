from pydantic import BaseModel

from pokedex.models.games import VersionGroup
from pokedex.models.items import Item
from pokedex.models.moves import Move


class Machine(BaseModel):
    id: int
    item: Item
    move: Move
    version_group: VersionGroup
