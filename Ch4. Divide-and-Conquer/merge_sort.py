# Merge two sorted arrays
def merge(left, right):
    res = []
    l = 0
    r = 0
    while r < len(right) or l < len(left):
        if l >= len(left):
            res.append(right[r])
            r += 1
        elif r >= len(right):
            res.append(left[l])
            l += 1
        else:
            if right[r] < left[l]:
                res.append(right[r])
                r += 1
            else:
                res.append(left[l])
                l += 1
    return res

# Divide the input array into 2 arrays
# Conquer two subproblems
# Merge the already sorted two arrays
def merge_sort(A):
    if len(A) == 1:
        return A

    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]

    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([10, 2, 17, 16, 12, 6]))
