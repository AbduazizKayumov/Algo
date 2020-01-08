def binary_search(x, A):
    l = -1
    r = len(A)
    while r - l > 1:
        mid = (r + l) >> 1
        if A[mid] == x:
            return mid
        if A[mid] > x:
            r = mid
        else:
            l = mid
    return -1


arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]
res = binary_search(6, arr)
print(res)
