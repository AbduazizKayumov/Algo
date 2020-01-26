q = int(input())
answers = []

for i in range(q):
    s = input()
    ints = list(map(int, s.split()))
    a, b, n, S = ints[0], ints[1], ints[2], ints[3]

    x = S // n
    S -= min(x, a) * n
    if S <= b:
        answers.append("YES")
    else:
        answers.append("NO")



for a in answers:
    print(a)
