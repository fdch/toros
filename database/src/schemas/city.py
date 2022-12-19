from pydantic import BaseModel
from typing import Optional

class City(BaseModel):
    id: str
    name : str
    acronym: Optional[str] = None


