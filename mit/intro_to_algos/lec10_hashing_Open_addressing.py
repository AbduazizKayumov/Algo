# Open addressing
# - no chaining, instead all items are stored in table
# - one item per-slot: m >= n
#
# Insertion, deletion and search
# - try probing different hash functions until an empty slot is found
# - flag with "DeleteMe" when deleting value
# - keep searching if key is not found or "DeleteMe" is encountered
#
# Open-addressing vs Chaining: better cache performance
# Chaining is less sensitive to hash functions


def hash(key, m):
    # just return m, very lazy hash function
    return m


def insert(key, table):
    # try probing diff hash functions until empty slot is found
    m = 0
    h = hash(key, m)
    while table[h]:
        if table[h] == "DeleteMe":
            break
        m += 1
        h = hash(key, m)
    table[h] = key


def delete(key, table):
    m = 0
    h = hash(key, m)
    while table[h] != key:
        m += 1
        h = hash(key, m)
    table[h] = "DeleteMe"


def search(key, table):
    m = 0
    h = hash(key, m)
    if table[h] == key:
        return h
    else:
        while table[h] != key and m < len(table) - 1:
            m += 1
            h = hash(key, m)
            if table[h] == key:
                return h
    return -1  # not found


arr = [456, 2, 1007, 65, 256, 883, 14, 147, 678, 89]
table = [None] * len(arr)

for a in arr:
    insert(a, table)
print(table)

delete(65, table)
print(table)

delete(14, table)
print(table)

h = search(14, table)
print(h)
