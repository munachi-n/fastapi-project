from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class LikeBase(BaseModel):
    entity_type: str
    entity_id: int


class LikeCreate(LikeBase):
    pass


class Like(LikeBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
