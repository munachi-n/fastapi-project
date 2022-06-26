from typing import Optional, List
from datetime import datetime, timedelta


class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = {}
        self.last_refill = {}

    def consume(self, key: str, tokens: int = 1) -> bool:
        now = datetime.utcnow()
        if key not in self.tokens:
            self.tokens[key] = self.capacity
            self.last_refill[key] = now
            return True

        elapsed = (now - self.last_refill[key]).total_seconds()
        self.tokens[key] = min(
            self.capacity, self.tokens[key] + elapsed * self.refill_rate
        )
        self.last_refill[key] = now

        if self.tokens[key] >= tokens:
            self.tokens[key] -= tokens
            return True
        return False


class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}

    def is_allowed(self, key: str) -> bool:
        now = datetime.utcnow()
        if key not in self.requests:
            self.requests[key] = []

        self.requests[key] = [
            t
            for t in self.requests[key]
            if (now - t).total_seconds() < self.window_seconds
        ]

        if len(self.requests[key]) < self.max_requests:
            self.requests[key].append(now)
            return True
        return False
