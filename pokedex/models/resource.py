from typing import List

from pydantic import BaseModel

from pokedex.models.commons import APIResource, NamedAPIResource


class APIResourceList(BaseModel):
    count: int
    next: str
    previous: bool
    results: List[APIResource]


class NamedAPIResourceList(BaseModel):
    count: int
    next: str
    previous: bool
    results: List[NamedAPIResource]
