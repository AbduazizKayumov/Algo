# https://www.hackerrank.com/challenges/max-array-sum/problem
def maxSubsetSum(arr):
    sums = [0] * len(arr)
    sums[0] = arr[0]
    for i in range(1, len(arr)):
        if i - 2 >= 0:
            sums[i] = max(arr[i] + sums[i - 2], sums[i - 1], arr[i])
        else:
            sums[i] = max(arr[i], sums[i - 1])
    return sums[-1]


# https://www.hackerrank.com/challenges/candies/problem
def candies(arr):
    n = len(arr)
    count = [1] * n

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            count[i] = count[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1] and count[i] <= count[i + 1]:
            count[i] = count[i + 1] + 1

    return sum(count)


# https://www.hackerrank.com/challenges/abbr/problem
import os


def lcs(a, b):
    m = len(a)
    n = len(b)

    A = a.upper()
    column = [0] * (m + 1)

    for i in range(1, n + 1):
        current = [0] * (m + 1)
        for j in range(1, m + 1):
            if b[i - 1] == A[j - 1]:
                current[j] = column[j - 1] + 1
            else:
                current[j] = max(current[j - 1], column[j])
        column = current.copy()
        current.clear()

    return column[-1]


def abbreviation(a, b):
    # aBbdD
    # BBD
    if len(a) < len(b):
        return False

    n = len(a)
    prev = [True]
    for i in range(n):
        prev.append(prev[-1] and a[i].islower())

    # print(prev)
    for i in range(len(b)):
        current = [False]
        for j in range(n):
            if b[i] == a[j]:
                current.append(prev[j])
            elif b[i] == a[j].upper():
                current.append(prev[j] or current[-1])
            elif a[j].islower():
                current.append(current[-1])
            else:
                current.append(False)

        # print(current)
        prev = current

    return "YES" if prev[-1] else "NO"
