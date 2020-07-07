def counting_sort(A, B, k):
    C = [0] * k

    # C[i] = the number of elements equal to i
    for a in A:
        C[a] += 1

    # C[i] = the number of elements less than or equal to i
    for i in range(1, k):
        C[i] += C[i - 1]

    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1


A = [4, 1, 2, 6, 5, 8, 0, 7, 3, 9]
B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 10
counting_sort(A, B, k)
print(B)
