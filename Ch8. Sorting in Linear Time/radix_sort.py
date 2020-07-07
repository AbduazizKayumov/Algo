# Sorts by ith digit
def counting_sort(A, i):
    count = {}
    for j in range(10):
        count[j] = []

    for a in A:
        s = str(a)
        index = ord(s[i]) - ord('0')
        count[index].append(a)

    res = []
    for i in range(10):
        res.extend(count[i])

    return res


# Sort an array A by least significant digit to most significant digit
def radix_sort(A, d):
    for i in range(d - 1, -1, -1):
        A = counting_sort(A, i)
        print(A)
    return A


A = [423, 109, 223, 681, 562, 809, 998, 703, 365, 974]
A = radix_sort(A, 3)
