n = int(input())
p = list(map(int, input().split()))
l = []

even = n // 2
odd = n - even

for i in range(len(p)):
    if p[i] == 0:
        continue
    l.append(p[i])
    if p[i] % 2 == 0:
        even -= 1
    else:
        odd -= 1
