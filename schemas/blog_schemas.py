from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class BlogPostBase(BaseModel):
    title: str
    content: str
    published: bool = False


class BlogPostCreate(BlogPostBase):
    pass


class BlogPost(BlogPostBase):
    id: int
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
