"""A very small in-memory cache with per-entry expiry."""

import time


class Cache:
    def __init__(self, ttl_seconds=60):
        self._ttl = ttl_seconds
        self._entries = {}

    def set(self, key, value):
        self._entries[key] = (value, time.monotonic() + self._ttl)

    def get(self, key):
        entry = self._entries.get(key)
        if entry is None:
            return None
        value, expires_at = entry
        if time.monotonic() > expires_at:
            del self._entries[key]
            return None
        return value

    def clear(self):
        self._entries.clear()
