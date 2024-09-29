from typing import Optional
from pydantic import BaseModel

class Student(BaseModel):
    id: Optional[str] = None
    name: str
    nota: int