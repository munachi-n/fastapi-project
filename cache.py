from typing import Optional


class Cache:
    def __init__(self):
        self._storage = {}

    def get(self, key: str) -> Optional[any]:
        return self._storage.get(key)

    def set(self, key: str, value: any, ttl: Optional[int] = None):
        self._storage[key] = value

    def delete(self, key: str):
        if key in self._storage:
            del self._storage[key]

    def clear(self):
        self._storage = {}

    def has(self, key: str) -> bool:
        return key in self._storage


cache = Cache()
