from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class NotificationType(str, Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
    IN_APP = "in_app"


class NotificationStatus(str, Enum):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"


class NotificationBase(BaseModel):
    user_id: int
    title: str
    message: str
    notification_type: NotificationType = NotificationType.IN_APP


class NotificationCreate(NotificationBase):
    pass


class Notification(NotificationBase):
    id: int
    status: NotificationStatus = NotificationStatus.PENDING
    created_at: datetime
    sent_at: Optional[datetime] = None

    class Config:
        from_attributes = True
