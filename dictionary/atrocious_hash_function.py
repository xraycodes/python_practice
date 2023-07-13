#educational video, not an actual hash function. Understanding how dictionary works and uses hash tables

data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]

def simple_hash(s: str) -> int:
    basic_hash = ord(s[0])
    return basic_hash % 10


def get(k: str) -> str:
    """Return the value for a kwey, or None if key doesn't exist"""
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


keys = [""] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    # h = hash(key)
    print(key, h)
    keys[h] = key
    values[h] = value

print(keys)
print(values)
print()
value = get("pizza")
print(value)