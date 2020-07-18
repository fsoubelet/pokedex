from pydantic import BaseModel

from pokedex.models import games, items, moves


class Machine(BaseModel):
    id: int
    item: items.Item
    move: moves.Move
    version_group: games.VersionGroup
