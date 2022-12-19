from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

class Event(BaseModel):
    id: str
    name : str
    datetime: datetime
    url: Optional[str]
    personRefs: List[str] = []
    workRefs: List[str] = []
    description: Optional[str]
    venueRef: Optional[str] = None
    countryRef: Optional[str] = None


