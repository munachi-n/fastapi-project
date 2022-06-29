from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class MessageBase(BaseModel):
    content: str
    receiver_id: int


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int
    sender_id: int
    read: bool = False
    created_at: datetime

    class Config:
        from_attributes = True
