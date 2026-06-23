from pydantic import BaseModel
from typing import Optional

class PartCreate(BaseModel):
    name: str
    description: Optional[str] = None
    unit: str
    quantity: float
    reorder_threshold: float

class PartUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    unit: Optional[str] = None
    quantity: Optional[float] = None
    reorder_threshold: Optional[float] = None

class PartResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    unit: str
    quantity: float
    reorder_threshold: float
    is_active: bool

    class Config:
        from_attributes = True