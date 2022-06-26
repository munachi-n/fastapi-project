import re
from typing import Optional


def validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_username(username: str) -> bool:
    return len(username) >= 3 and len(username) <= 30 and username.isalnum()


def validate_password(password: str) -> Optional[str]:
    if len(password) < 8:
        return "Password must be at least 8 characters"
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one digit"
    return None


def validate_phone(phone: str) -> bool:
    pattern = r"^\+?1?\d{9,15}$"
    return bool(re.match(pattern, phone))


def validate_url(url: str) -> bool:
    pattern = r"^https?://[^\s]+$"
    return bool(re.match(pattern, url))
