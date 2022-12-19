from pydantic import BaseModel
from typing import Optional

class Venue(BaseModel):
    id: str
    name : str
    countryRef: Optional[str] = None
    cityRef: Optional[str] = None
    personRef: Optional[str] = None
    address: Optional[str] = None
    kind: Optional[str] = None
    contact: Optional[str] = None
    description: Optional[str] = None


