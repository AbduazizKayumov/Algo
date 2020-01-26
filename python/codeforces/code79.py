t = int(input())

answers = []
for ti in range(t):
    ints = list(map(int, input().split()))
    n, s = ints[0], ints[1]

    a = list(map(int, input().split()))
    if sum(a) <= s:
        answers.append("0")
        continue

    summ = 0
    mx = a[0]
    mx_index = 0

    for i in range(len(a)):
        summ += a[i]
        if summ > s:
            # can I skip any a[i] 0 <= i
            if a[i] < mx:
                ans = mx_index + 1
                break

        if a[i] >= mx:
            mx_index = i + 1
            mx = a[i]

    answers.append(mx_index)

for a in answers:
    print(a)
