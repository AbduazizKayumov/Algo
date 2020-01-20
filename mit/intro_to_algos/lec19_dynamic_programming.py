from math import inf


# Dynamic programming
# ~ controlled brute force
# ~ recursion + re-use
# ~ try all guesses -> solve sub-subproblems -> memoize

# Example 1: Fibonacci
# Naive approach: O(2^N) -> exponential is bad
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Memoized DP approach
def fibonacci_dp(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    f = fibonacci_dp(n - 1, memo) + fibonacci_dp(n - 2, memo)
    memo[n] = f
    return f


# Bottom-up DP approach
# 1) Practically faster (no recursions)
# 2) Saves space (only remember last two numbers)
# There is O(lgn) time algorithm for Fibonacci, via diff. techniques ;-)
def fibonacci_bottom_up_dp(n):
    if n <= 2:
        return 1
    f1 = 1
    f2 = 1
    f = 0
    for i in range(2, n):
        f = f1 + f2
        f1, f2 = f2, f
    return f


# Example 2: Shortest path
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
