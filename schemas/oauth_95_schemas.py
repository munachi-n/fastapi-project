from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class OAuthBase(BaseModel):
    provider: str
    provider_id: str

class OAuthCreate(OAuthBase):
    access_token: str
    refresh_token: Optional[str] = None

class OAuth(OAuthBase):
    id: int
    user_id: int
    access_token: str
    refresh_token: Optional[str] = None
    expires_at: Optional[datetime] = None
    created_at: datetime
    
    class Config:
        from_attributes = True
