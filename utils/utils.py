import hashlib
import secrets


def generate_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


def generate_token(length: int = 32) -> str:
    return secrets.token_hex(length)


def validate_email(email: str) -> bool:
    import re

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_password(password: str) -> bool:
    return len(password) >= 8


def truncate_string(text: str, length: int = 50) -> str:
    if len(text) <= length:
        return text
    return text[: length - 3] + "..."
