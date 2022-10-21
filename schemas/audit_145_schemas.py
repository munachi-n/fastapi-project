from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class AuditBase(BaseModel):
    action: str
    entity_type: str

class AuditCreate(AuditBase):
    entity_id: int

class Audit(AuditBase):
    id: int
    user_id: Optional[int] = None
    entity_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
