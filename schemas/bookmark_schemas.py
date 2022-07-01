from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class BookmarkBase(BaseModel):
    entity_type: str
    entity_id: int


class BookmarkCreate(BookmarkBase):
    pass


class Bookmark(BookmarkBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
