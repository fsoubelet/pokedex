from pydantic import BaseModel
from typing import List


class Name(BaseModel):
    name: str
    language: Language


class Language(BaseModel):
    id: int
    name: str
    official: bool
    iso639: str
    iso3166: str
    names: List[Name]
