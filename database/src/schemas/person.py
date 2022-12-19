from pydantic import BaseModel
from typing import Optional, List

class Person(BaseModel):
    id: str
    name : str
    lastname : Optional[str]
    url: Optional[str]
    bioRef: Optional[str] = None
    roleRefs: List[str] = []


