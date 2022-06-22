from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ProductList(BaseModel):
    items: List[Product]
    total: int
    page: int
    per_page: int
