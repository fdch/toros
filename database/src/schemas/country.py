from pydantic import BaseModel
from typing import Optional

class Country(BaseModel):
    id: str
    name : str
    acronym: Optional[str] = None


