from typing import List

from pydantic import BaseModel

from pokedex.models import commons


class APIResourceList(BaseModel):
    count: int
    next: str
    previous: bool
    results: List[commons.APIResource]


class NamedAPIResourceList(BaseModel):
    count: int
    next: str
    previous: bool
    results: List[commons.NamedAPIResource]
