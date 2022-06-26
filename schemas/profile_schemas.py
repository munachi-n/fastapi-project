from typing import Any, Dict, List, Optional
from pydantic import BaseModel, validator


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    country: str = "USA"


class Profile(BaseModel):
    user_id: int
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[Address] = None
    social_links: Optional[Dict[str, str]] = None

    @validator("bio")
    def bio_max_length(cls, v):
        if v and len(v) > 500:
            raise ValueError("Bio must be less than 500 characters")
        return v
