from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class AnalyticsBase(BaseModel):
    metric: str
    value: float

class AnalyticsCreate(AnalyticsBase):
    pass

class Analytics(AnalyticsBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    
    class Config:
        from_attributes = True
