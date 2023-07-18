from typing import List, Dict

from pydantic import BaseModel


class Rate(BaseModel):
    cargo_type: str
    rate: str


class RateList(BaseModel):
    data: Dict[str, List[Rate]]
