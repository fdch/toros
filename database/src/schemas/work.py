from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

class Work(BaseModel):
    id: str
    name : str
    releasedate: datetime
    url: Optional[str]
    personRefs: List[str] = []
    description: Optional[str]
    eventRef: List[str] = None
    formatRef: List[str] = None


