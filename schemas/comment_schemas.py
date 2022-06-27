from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CommentBase(BaseModel):
    content: str
    post_id: int


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
