from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from decimal import Decimal
from typing import Optional, List

class ProductResponse(BaseModel):
    id: UUID
    name: str
    category: str
    price: Decimal
    created_at: datetime

    class Config:
        from_attributes = True

class ProductListResponse(BaseModel):
    data: List[ProductResponse]
    next_cursor: Optional[str] = None