from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class PaymentBase(BaseModel):
    order_id: int
    amount: float
    currency: str = "USD"


class PaymentCreate(PaymentBase):
    payment_method: str


class Payment(PaymentBase):
    id: int
    user_id: int
    payment_method: str
    status: str = "pending"
    transaction_id: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
