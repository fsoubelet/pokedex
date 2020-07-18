from pydantic import BaseModel

from pokedex.models import games
from pokedex.models import items
from pokedex.models import moves


class Machine(BaseModel):
    id: int
    item: items.Item
    move: moves.Move
    version_group: games.VersionGroup
