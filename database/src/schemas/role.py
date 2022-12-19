from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Role(BaseModel):
    id: str
    name: str
    datestart: Optional[datetime]
    dateend: Optional[datetime]


