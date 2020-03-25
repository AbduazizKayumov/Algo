from math import inf

# Shortest path
# 1) Recursion: terrible solution -> O(V^E)
def shortest_path(adj, w, start, target):
    if start == target:
        return 0
    shortest = inf
    for v in adj[target]:
        d = w[(target, v)] + shortest_path(adj, w, start, v)
        if d < shortest:
            shortest = d
    return shortest


# 2) Shortest path with Memoized Dp: effectively DFS + Bellman-Ford
# - Takes infinite time if cycles
# + Works for DAGs (Directed acyclic graphs)
# + O(V + E) time

def shortest_path_dp(adj, w, start, target, memo=None):
    if start == target:
        return 0
    if memo is None:
        memo = {}
    if (start, target) in memo:
        return memo[(start, target)]

    shortest = inf
    for v in adj[target]:
        d = w[(target, v)] + shortest_path_dp(adj, w, start, v, memo)
        if d < shortest:
            shortest = d
    memo[(start, target)] = shortest
    return shortest


# Graph
#    A---(3)--->B---(3)--->C
#    |                     |
#   (5)                   (3)
#    |                     |
#    v                     v
#    E---------(5)-------->D

vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ['A', 'B', 3],
    ['A', 'E', 5],
    ['B', 'C', 3],
    ['C', 'D', 3],
    ['E', 'D', 5]
]
adj = {}
weights = {}
for e in edges:
    if e[1] not in adj:
        adj[e[1]] = set()
    adj[e[1]].add(e[0])
    weights[(e[1], e[0])] = e[2]

print(shortest_path_dp(adj, weights, 'A', 'D'))
