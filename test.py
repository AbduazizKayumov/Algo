import random
from collections import Counter


def rand7():
    return random.randint(1, 7)


def rand10():
    ans = rand7() + (rand7() - 1)
    return ans % 11


n = 2000
a = []
for i in range(n):
    a.append(rand10())

c = Counter(a)
for i in range(0, 11):
    print(i, ": ", c[i] / n * 100, " %")