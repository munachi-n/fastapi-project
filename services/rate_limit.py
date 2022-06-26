from typing import Optional
from datetime import datetime


class RateLimiter:
    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._requests = {}

    def is_allowed(self, key: str) -> bool:
        now = datetime.utcnow()
        if key not in self._requests:
            self._requests[key] = []

        self._requests[key] = [
            t
            for t in self._requests[key]
            if (now - t).total_seconds() < self.window_seconds
        ]

        if len(self._requests[key]) < self.max_requests:
            self._requests[key].append(now)
            return True
        return False

    def reset(self, key: str):
        if key in self._requests:
            del self._requests[key]


rate_limiter = RateLimiter()
