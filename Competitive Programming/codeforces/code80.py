ints = list(map(int, input().split()))
n, m = ints[0], ints[1]

count = 0

for i in range(1, n + 1):
    comb = n - i + 1
    for j in range(comb + 1, n + 1):
        comb *= j
    count += 1

print(count)

# 157557417
# 568992324
