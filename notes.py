# Indicate a size for the hash table.
hash_table_size = 5

# This is where we store stuff.
hash_table = [None] * hash_table_size


def new_hash(s):
    # This breaks our code down into numbers from a string.
    str_bytes = s.encode()

    # This value from each will be added up to be used in the modulo of hash_index.
    total = 0

    for b in str_bytes:
        total += b

    return total


def hash_index(s):
    # This will always return the same index, as long as the hash_table_size doesn't change.
    h = new_hash(s)

    # The value is returned here.
    return h % hash_table_size


def add(key, value):
    # Get the index into the hash table list
    index = hash_index(key)
    hash_table[index] = value


def remove(key):
    index = hash_index(key)
    hash_table[index] = None



if __name__ == "__main__":
    add("Hello", "#ff0000")
    add("Something", 22)
    print(hash_table[hash_index("Hello")])
