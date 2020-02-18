# Find smallest element from i to n
# Swap the smallest one with A[i]
def selection_sort(A):
    for i in range(len(A)):
        pos = i
        for j in range(i, len(A)):
            if A[pos] > A[j]:
                pos = j
        A[i], A[pos] = A[pos], A[i]
    return A


print(selection_sort([10, 2, 17, 16, 12, 6]))
