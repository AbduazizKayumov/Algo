import random


def minimum(A):
    if not A:
        return 0
    _min = A[0]
    for a in A:
        _min = min(a, _min)

    return a


def maximum(A):
    if not A:
        return 0
    _max = A[0]
    for a in A:
        _max = max(a, _max)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


# Select ith element from unsorted array
def randomized_select(A, p, r, i):
    if i > len(A) or i <= 0:
        return -1

    if p == r:
        return A[p]

    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:  # the pivot value is the answer
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    return randomized_select(A, q + 1, r, i - k)


A = [10, 3, 15, 5, 6, 21, 1, 9]
min3 = randomized_select(A, 0, len(A) - 1, 0)
print(min3)