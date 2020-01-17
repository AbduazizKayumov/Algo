from math import inf


def extract_min(Q, distance):
    pos = 0
    for i in range(len(Q)):
        if distance[Q[i]] < distance[Q[pos]]:
            pos = i
    return Q.pop(pos)


# Speed-up 1
# Single-source single target graphs
#       - stop when the target is visited
def dijkstra(vertices, edges, source, target):
    adj = {}
    distance = {}
    queue = []
    parent = {}

    for vertex in vertices:
        adj[vertex] = set()
        queue.append(vertex)
        if vertex == source:
            distance[vertex] = 0
        else:
            distance[vertex] = inf

    weights = {}
    for e in edges:
        adj[e[0]].add(e[1])
        weights[(e[0], e[1])] = e[2]

    while queue:
        u = extract_min(queue, distance)

        # Speed-up 1
        if u == target:
            break

        for v in adj[u]:
            w = weights[(u, v)]
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u

    print("Shortest distance: ", distance[target])
    print("Shortest path:")
    path = [target]
    p = parent[target]
    while p:
        path.append(p)
        if p in parent:
            p = parent[p]
        else:
            p = None
    path.reverse()
    print(path)


# Graph:
#        _B-------D
#      /` |       |
#    A<   |       |
#      \_ |       |
#        `C-------E

vertices = ['A', 'B', 'C', 'D', 'E']
edges = [['A', 'B', 10],
         ['A', 'C', 3],
         ['B', 'C', 1],
         ['B', 'D', 2],
         ['C', 'B', 4],
         ['C', 'D', 8],
         ['C', 'E', 2],
         ['D', 'E', 7],
         ['E', 'D', 9]]

# find shortest paths from 'A' to all other nodes
dijkstra(vertices, edges, 'A', 'D')
