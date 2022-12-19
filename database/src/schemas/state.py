from pydantic import BaseModel
from typing import Optional

class State(BaseModel):
    id: str
    name : str
    countryRef: Optional[str] = None


