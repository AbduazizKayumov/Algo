# Insert key A[i] into the already sorted A[0:i]
def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


print(insertion_sort([10, 7, 12, 1]))


