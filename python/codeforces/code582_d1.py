import math

ints = list(map(int, input().split()))
n, k = ints[0], ints[1]
a = list(map(int, input().split()))
a.sort()

answers = [0] * len(a)
for i in range(n):
    cur = 0
    for j in range(i + 1, n):
        if a[i] * 2 > a[j]:
            break
        div = math.floor(math.log2(a[i])) + 1
        cur +=
