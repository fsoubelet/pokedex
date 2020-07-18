from typing import Dict, List

from pydantic import BaseModel


class Language(BaseModel):
    id: int
    name: str
    official: bool
    iso639: str
    iso3166: str
    names: List[Dict]


class Name(BaseModel):
    name: str
    language: Language
