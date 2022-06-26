from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class ShippingBase(BaseModel):
    order_id: int
    carrier: str
    tracking_number: Optional[str] = None


class ShippingCreate(ShippingBase):
    pass


class Shipping(ShippingBase):
    id: int
    status: str = "pending"
    estimated_delivery: Optional[datetime] = None
    shipped_at: Optional[datetime] = None
    delivered_at: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
