from math import floor

# Chaining:
# Linked list of colliding elements in each slot of table

m = 10  # we may have only 10 keys

# Division method
def hash(value):
    return value % m


# Multiplication method
def hash_mult(value):
    A = 0.6180339887
    return floor(m * ((A * value) % 1))


arr = [100, 91, 45, 25, 33, 10, 27]
hash_table = [[] for _ in range(m)]

for a in arr:
    h = hash_mult(a)
    hash_table[h].append(a)

for row in hash_table:
    print(row)
