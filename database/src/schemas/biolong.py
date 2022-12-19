from pydantic import BaseModel
from typing import List

class BioLong(BaseModel):
    id: str
    text: List[str] = []

