n = int(input())
friends = list(map(int, input().split()))
original = friends.copy()

guys = {}
for i in range(len(friends)):
    if friends[i] != 0:
        guys[friends[i]] = 1

dumbs = []
for i in range(1, n + 1):
    if i not in guys:
        dumbs.append(i)

for i in range(len(friends)):
    if friends[i] == 0:
        maybe = dumbs.pop()
        if maybe != i + 1:
            friends[i] = maybe
            continue

        if dumbs:
            candidate = dumbs.pop()
            friends[i] = candidate
            dumbs.append(maybe)
        else:
            # only 1 left, change it with any dumb
            for j in range(len(original)):
                if j != i and original[j] == 0 and friends[j] != maybe:
                    friends[i] = friends[j]
                    friends[j] = maybe
                    break

print(*friends)