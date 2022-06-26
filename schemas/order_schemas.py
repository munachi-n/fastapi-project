from typing import Optional
from datetime import datetime, timedelta
from pydantic import BaseModel


class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: float


class OrderCreate(BaseModel):
    items: list[OrderItem]
    shipping_address: str


class Order(BaseModel):
    id: int
    user_id: int
    items: list[OrderItem]
    total: float
    status: str = "pending"
    shipping_address: str
    created_at: datetime
    updated_at: Optional[datetime] = None


class OrderUpdate(BaseModel):
    status: Optional[str] = None
    shipping_address: Optional[str] = None
