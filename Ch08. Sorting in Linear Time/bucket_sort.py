from math import floor


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


# Divide the input into buckets, sort each bucket and merge
# Bucket sort assumes that the input is randomly distributed
# which results to n equal sized sub-intervals (or buckets).
# The average case running is O(n), like counting sort, bucket is fast
# since it assumes smth about the input
def bucket_sort(A):
    n = len(A)

    # create n buckets
    B = []
    for i in range(n):
        B.append([])

    # divide input elements into buckets
    for i in range(n):
        bucket_index = floor(n * A[i])
        B[bucket_index].append(A[i])

    # sort the buckets
    for i in range(n):
        insertion_sort(B[i])

    # concatenate the output
    output = []
    for i in range(n):
        output.extend(B[i])

    return output


A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
A = bucket_sort(A)
print(A)
