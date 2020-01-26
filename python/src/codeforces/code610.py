t = int(input())
answers = []

for ti in range(t):
    s = input()
    ints = list(map(int, s.split()))
    n, p, k = ints[0], ints[1], ints[2]
    prices = list(map(int, input().split()))
    n = len(prices)
    prices.sort()

    mx = 0
    # 1 1 2 2 2 3 4 5 6

    sum = 0
    for i in range(k):
        if sum > p:
            break
        current = sum
        count = i
        for j in range(i + k - 1, n, k):
            if current + prices[j] <= p:
                count += k
                current += prices[j]
            else:
                break
        sum += prices[i]
        if count > mx:
            mx = count

    answers.append(mx)

for a in answers:
    print(a)
