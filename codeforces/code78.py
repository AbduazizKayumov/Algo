def is_permutation(a, b):
    a = list(a)
    a.sort()

    b = list(b)
    b.sort()

    if a == b:
        return True
    return False


s = input()
ints = list(map(int, s.split()))
n, m = ints[0], ints[1]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dict = {}
for bi in b:
    dict[bi] = 1

x = 0
while True:
    found = True
    tmp = []
    for i in range(len(a)):
        if (a[i] + x) % m not in dict:
            found = False
            break

    if found:

        is_permutation()
