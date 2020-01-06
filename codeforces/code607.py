def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


s = input()
l = list(map(int, s.split()))
n = l[0]
m = l[1]

graph = {}
for i in range(1, n + 1):
    graph[i] = set()

amounts = {}
for i in range(m):
    l = list(map(int, input().split()))
    debtor, bank, amount = l[0], l[1], l[2]
    graph[debtor].add(bank)
    graph[bank].add(debtor)

    if (debtor, bank) in amounts:
        amounts[(debtor, bank)] += amount
    else:
        amounts[(debtor, bank)] = amount

    if (bank, debtor) in amounts:
        amounts[(bank, debtor)] += -amount
    else:
        amounts[(bank, debtor)] = -amount

print(graph)

visited = set()
for i in range(1, n + 1):
    queue = [i]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            connections = graph[node] - visited
            if not connections:
                continue
            queue.extend(connections)

            print(connections)
            con = list(connections)
            for i in range(1, len(con)):
                z = min(amounts[(node, con[i])], amounts[(node, con[i - 1])])
                if amounts[(node, con[i-1])] == z:
                    amounts
