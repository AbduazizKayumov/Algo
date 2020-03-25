# Repeatedly adjust adjacent elements that are our of order
def bubble_sort(A):
    for i in range(len(A)):
        for j in range(1, len(A)):
            if A[j] < A[j - 1]:
                A[j], A[j-1] = A[j-1], A[j]
    return A


print(bubble_sort([10, 2, 17, 16, 12, 6]))