import math


# Brute force solution to find the maximum subarray problem - O(n^2)
def max_subarray_brute_force(A):
    _max = 0
    for i in range(len(A)):
        _sum = 0
        for j in range(i, len(A)):
            _sum += A[j]
            if _sum > _max:
                _max = _sum
    return _max


# Finds the max subarray that contains the mid element: A[i,j] where i < m < j
def max_crossing_subarray(A, low, mid, high):
    _sum = 0
    left_sum = -math.inf
    max_left = mid
    for i in range(mid, low - 1, -1):
        _sum += A[i]
        if _sum > left_sum:
            left_sum = _sum
            max_left = i
    _sum = 0
    right_sum = -math.inf
    max_right = mid
    for i in range(mid + 1, high + 1):
        _sum += A[i]
        if _sum > right_sum:
            right_sum = _sum
            max_right = i
    return max_left, max_right, left_sum + right_sum


# Divide & Conquer algorithm to find the max subarray:
# 1. if A has a single element, return it (base case)
# 2. Have the mid element, there are 3 cases:
#       a) The max subarray is strictly on the left subarray A[0:mid]
#       b) The max subarray is the crossing array: A[i:j] where i<mid<j
#       c) The max subarray is strictly on the right subarray A[mid+1:]
#    Compute all of the 3 cases
# 3. return the max
def max_subarray(A, low, high):
    if low == high:
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = max_subarray(A, low, mid)
        right_low, right_high, right_sum = max_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        if right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        return cross_low, cross_high, cross_sum


# Linear time solution to find max subarray (Kadane's algorithm)
def max_subarray_linear(A):
    _max = 0
    current = 0
    for i in range(len(A)):
        current = max(0, current + A[i])  # max subarray ending at j
        _max = max(_max, current)
    return _max


print(max_subarray_linear([-10, 10, -9, 6, 7, -18]))
