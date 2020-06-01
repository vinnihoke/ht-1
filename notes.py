# Indicate a size for the hash table.
hash_table_size = 5

# This is where we store stuff.
hash_table = [None] * hash_table_size


class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'HashTableEntry({repr(self.key)}, {repr(self.value)})'


def new_hash(s):
    # This breaks our code down into numbers from a string.
    str_bytes = s.encode()

    # This value from each will be added up to be used in the modulo of hash_slot.
    total = 0

    for b in str_bytes:
        total += b

    return total


def hash_slot(s):
    # This will always return the same slot, as long as the hash_table_size doesn't change.
    h = new_hash(s)

    # The value is returned here.
    return h % len(hash_table)


def add(key, value):
    # Get the slot into the hash table list
    slot = hash_slot(key)
    hash_table[slot] = HashTableEntry(key, value)


def remove(key):
    slot = hash_slot(key)
    hash_table[slot] = None


def get(key):
    slot = hash_slot(key)
    hash_entry = hash_table[slot]

    if hash_entry is not None:
        return hash_entry.value

    return None


if __name__ == "__main__":
    add("Hello", "#ff0000")
    add("Something", 22)
    print(hash_table)
    print(get("Hello"))
    print(get("Something"))
