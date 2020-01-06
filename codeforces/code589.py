ints = list(map(int, input().split()))
h, w = ints[0], ints[1]

grid = []

r = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in range(h):
    grid.append([0] * w)
    for rr in range(r[i]):
        if rr < w:
            grid[i][rr] = 1
    if r[i] < w:
        grid[i][r[i]] = -1

possible = True
for i in range(w):
    if not possible:
        break
    for cc in range(c[i] + 1):
        if cc < c[i]:
            if grid[cc][i] == -1:
                possible = False
                break
            grid[cc][i] = 1
    if c[i] < h and grid[c[i]][i] == 1:  # this should be empty, but 1 was displayed
        possible = False
        break
    elif c[i] < h:
        grid[c[i]][i] = -1

unreserved = 0
if possible:
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0:
                unreserved += 1

if unreserved == 0 and possible:
    print("1")
elif unreserved == 0 and not possible:
    print("0")
else:
    print((2 ** unreserved) % 1000000007)
