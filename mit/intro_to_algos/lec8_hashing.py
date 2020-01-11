import random

# Chaining:
# Linked list of colliding elements in each slot of table

m = 10  # we may have only 10 keys


# Division method
def hash(value):
    return value % m


# Multiplication method
def hash_mult(value):
    w = 32
    r = 8
    a = random.randint(-(2 ** (w - 1)), (2 ** w))
    return ((a * value) % (2 ** w)) >> (w - r)


arr = [100, 91, 45, 25, 33, 10, 27]
hash_table = [[] for _ in range(m)]

for a in arr:
    h = hash(a)
    hash_table[h].append(a)

for row in hash_table:
    print(row)
