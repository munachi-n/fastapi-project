from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class FollowBase(BaseModel):
    following_id: int


class FollowCreate(FollowBase):
    pass


class Follow(FollowBase):
    id: int
    follower_id: int
    created_at: datetime

    class Config:
        from_attributes = True
