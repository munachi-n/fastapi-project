from typing import Any, Dict
import hashlib
import hmac
import secrets


def generate_api_key() -> str:
    return secrets.token_urlsafe(32)


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed


def generate_otp(length: int = 6) -> str:
    return "".join(secrets.choice("0123456789") for _ in range(length))


def verify_otp(otp: str, stored_otp: str) -> bool:
    return hmac.compare_digest(otp, stored_otp)


def generate_reset_token() -> str:
    return secrets.token_urlsafe(32)
