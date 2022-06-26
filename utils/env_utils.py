from typing import Optional
import os
import json


def get_env(key: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(key, default)


def get_env_int(key: str, default: int = 0) -> int:
    value = os.getenv(key)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default


def get_env_bool(key: str, default: bool = False) -> bool:
    value = os.getenv(key, "").lower()
    if value in ("true", "1", "yes"):
        return True
    if value in ("false", "0", "no"):
        return False
    return default


def load_env_file(file_path: str = ".env"):
    if not os.path.exists(file_path):
        return
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()
