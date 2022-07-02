from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class LogBase(BaseModel):
    level: str
    message: str


class LogCreate(LogBase):
    source: Optional[str] = None


class Log(LogBase):
    id: int
    source: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
