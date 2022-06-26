from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class ReviewBase(BaseModel):
    product_id: int
    rating: int
    comment: Optional[str] = None


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ReviewList(BaseModel):
    items: List[Review]
    total: int
    average_rating: float
