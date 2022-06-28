from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class ImageBase(BaseModel):
    url: str
    alt_text: Optional[str] = None


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int
    entity_type: str
    entity_id: int
    created_at: datetime

    class Config:
        from_attributes = True
