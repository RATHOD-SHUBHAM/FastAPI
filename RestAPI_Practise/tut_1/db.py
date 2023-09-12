from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    gender: str
    ip_address: Optional[str] = None
