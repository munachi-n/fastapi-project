from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class SettingBase(BaseModel):
    key: str
    value: str


class SettingCreate(SettingBase):
    pass


class Setting(SettingBase):
    id: int
    user_id: Optional[int] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
