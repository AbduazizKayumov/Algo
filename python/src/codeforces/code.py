n = int(input())
tree = {}
for i in range(n - 1):
    ints = list(map(int, input().split()))
    ints.sort()

    if ints[0] not in tree:
        tree[ints[0]] = set()
    tree[ints[0]].add(ints[1])

print(tree)

visited = set()
queue = [1]

h = {1: 0}
ll = []
while queue:
    node = queue.pop(0)
    if node not in visited:
        visited.add(node)
        if node in tree:
            leaves = tree[node] - visited
            for l in leaves:
                h[l] = h[node] + 1
            queue.extend(leaves)
        else:
            ll.append(node)


print(h)
print(ll)

for l in ll:
    print("Leaf ", l, h[l])


