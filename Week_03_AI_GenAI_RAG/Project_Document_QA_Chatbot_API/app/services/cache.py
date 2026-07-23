import hashlib

cache = {}

def make_key(session_id, query):
    return hashlib.sha256(f"{session_id}:{query}".encode("utf-8")).hexdigest()

def get(session_id, query):
    key = make_key(session_id, query)
    return cache.get(key)

def set(session_id, query, value):
    key = make_key(session_id, query)
    cache[key] = value