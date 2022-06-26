from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class CategoryList(BaseModel):
    items: List[Category]
    total: int
