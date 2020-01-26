t = int(input())
answers = []

for ti in range(t):
    ints = list(map(int, input().split()))
    n, m = ints[0], ints[1]

    stack = list(map(int, input().split()))
    stack.reverse()

    b = list(map(int, input().split()))

    time = 0
    cache = {}
    for i in range(len(b)):
        if b[i] in cache:
            time += 1
            cache.pop(b[i])
            continue

        p = stack.pop()
        while p != b[i]:
            cache[p] = 1
            p = stack.pop()

        time += 2 * len(cache) + 1

    answers.append(time)

for a in answers:
    print(a)
