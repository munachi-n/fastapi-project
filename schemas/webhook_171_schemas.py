from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

class WebhookBase(BaseModel):
    url: str
    events: List[str]

class WebhookCreate(WebhookBase):
    pass

class Webhook(WebhookBase):
    id: int
    user_id: int
    active: bool = True
    created_at: datetime
    
    class Config:
        from_attributes = True
