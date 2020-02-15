# Insert key A[i] into the already sorted A[0:i]
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i
        while j > 0:
            if arr[j - 1] > key:
                arr[j] = arr[j - 1]
                arr[j - 1] = key
                j -= 1
            else:
                break
    return arr


# Merge sort
# 1) If n = 1, done, nothing to sort
# 2) Otherwise recursively sort A[0:n/2] and A[n/2:] -> TOP TO BOTTOM
# 3) Merge the already sorted array -> BOTTOM TO TOP
def merge(left, right):
    list = []
    l = 0
    r = 0
    while l < len(left) or r < len(right):
        if l < len(left) and r < len(right):
            if left[l] <= right[r]:
                list.append(left[l])
                l += 1
            else:
                list.append(right[r])
                r += 1
            continue
        if l < len(left):
            list.append(left[l])
            l += 1
            continue
        if r < len(right):
            list.append(right[r])
            r += 1
    return list


def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr

    mid = n >> 1
    left = arr[0:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))
