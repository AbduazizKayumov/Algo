q = int(input())
total = []
for qi in range(q):
    n = int(input())
    kids = list(map(int, input().split()))

    answers = [0] * n

    for i in range(n):
        if answers[kids[i]-1] != 0:
            continue
        tmp = kids[i]
        days = 1
        pairs = [tmp]

        while tmp != i + 1:
            tmp = kids[tmp - 1]
            pairs.append(tmp)
            days += 1

        for p in pairs:
            answers[p-1] = days

    total.append(answers)

for t in total:
    print(" ".join([str(i) for i in t]))
