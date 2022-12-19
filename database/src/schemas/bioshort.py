from pydantic import BaseModel
from typing import Optional

class BioShort(BaseModel):
    id: str
    text: Optional[str]

