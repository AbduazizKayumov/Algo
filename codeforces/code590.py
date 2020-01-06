from collections import deque


ints = list(map(int, input().split()))
n, k = ints[0], ints[1]
conversations = list(map(int, input().split()))

screen = deque()
cache = {}
for i in range(len(conversations)):
    if conversations[i] in cache:
        continue

    if len(screen) >= k:
        remove = screen.popleft()
        cache.pop(remove)

        screen.append(conversations[i])
        cache[conversations[i]] = 1
    else:
        screen.append(conversations[i])
        cache[conversations[i]] = 1

print(len(screen))
screen.reverse()
print(*screen)
