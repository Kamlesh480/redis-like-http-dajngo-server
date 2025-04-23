# store/kv_engine.py
from django.core.cache import cache

class KVEngine:
    def set(self, key, value):
        cache.set(key, value)
        return True

    def get(self, key):
        return cache.get(key)

    def delete(self, key):
        return cache.delete(key)