from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class ReportBase(BaseModel):
    reason: str
    description: Optional[str] = None


class ReportCreate(ReportBase):
    entity_type: str
    entity_id: int


class Report(ReportBase):
    id: int
    reporter_id: int
    status: str = "pending"
    created_at: datetime

    class Config:
        from_attributes = True
