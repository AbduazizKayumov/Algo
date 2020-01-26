from math import sqrt
from math import ceil


def find(fro, n):
    if n % fro == 0:
        return fro
    return find(fro + 1, n)


t = int(input())
answers = []
for ti in range(t):
    n = int(input())

    first = -1
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            first = i
            break

    if first == -1:
        answers.append("NO")
        continue

    second = -1
    nn = n // first
    for i in range(first + 1, ceil(sqrt(nn))):
        if nn % i == 0:
            second = i
            break

    if second == -1:
        answers.append("NO")
        continue

    third = nn // second
    answers.append("YES")
    answers.append(str(first) + " " + str(second) + " " + str(third))


for a in answers:
    print(a)
