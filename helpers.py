from datetime import datetime, timedelta
from typing import Optional


def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    return dt.strftime(fmt)


def parse_datetime(dt_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    return datetime.strptime(dt_str, fmt)


def add_days(dt: datetime, days: int) -> datetime:
    return dt + timedelta(days=days)


def add_hours(dt: datetime, hours: int) -> datetime:
    return dt + timedelta(hours=hours)


def get_timestamp() -> float:
    return datetime.utcnow().timestamp()


def from_timestamp(ts: float) -> datetime:
    return datetime.fromtimestamp(ts)
