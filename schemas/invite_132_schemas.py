from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class InviteBase(BaseModel):
    email: str
    role: str = "user"

class InviteCreate(InviteBase):
    pass

class Invite(InviteBase):
    id: int
    inviter_id: int
    token: str
    expires_at: datetime
    used: bool = False
    created_at: datetime
    
    class Config:
        from_attributes = True
