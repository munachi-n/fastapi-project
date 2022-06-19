from typing import Any, Callable
import time
from functools import wraps


class MemoizationCache:
    def __init__(self):
        self._cache = {}

    def get(self, key: str) -> Any:
        return self._cache.get(key)

    def set(self, key: str, value: Any):
        self._cache[key] = value

    def clear(self):
        self._cache = {}


def memoize(cache: MemoizationCache = None):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            if cache and cache.get(key) is not None:
                return cache.get(key)
            result = func(*args, **kwargs)
            if cache:
                cache.set(key, result)
            return result

        return wrapper

    return decorator


memo_cache = MemoizationCache()


def clear_cache(cache: MemoizationCache):
    cache.clear()
