q = int(input())

powers = []
p = 0
while p < 40:
    powers.append(3 ** p)
    p += 1

powers.reverse()
sm = sum(powers)

for qi in range(q):
    n = int(input())

    x = sm
    for i in range(len(powers)):
        if x - powers[i] >= n:
            x -= powers[i]

    print(x)
