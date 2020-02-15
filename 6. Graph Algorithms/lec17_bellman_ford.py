from math import inf


# Bellman-Ford algorithm to find shortest paths
# 1) Assign zero to starting node and infinity (∞) to all other nodes: distance = {}
# 2) for i from 0 to len(vertices)
#       for edge(u, v) with weight w in edges:
#           // relaxing
#           if distance[u] + w < distance[v]:
#               distance[v] = distance[u] + w
# 3) Check for negative weight cycles
#       for edge(u, v) with weight w in edges:
#           if distance[u] + w < distance[v]:
#               report "Graph contains negative edges"
# Complexity: O(|V|*|E|)
# Bellman-Ford vs Dijkstra: Bellman-Ford can work with graphs with negative weights
# and can detect negative weight cycles
#
# After |V| - 1 passes, if we find a distance[v] that can be relaxed, then
# this means the graph has a negative weight cycle

def bellman_ford(vertices, edges, start):
    adj = {}
    distance = {}
    queue = []
    for vertex in vertices:
        adj[vertex] = set()
        queue.append(vertex)
        if vertex == start:
            distance[vertex] = 0
        else:
            distance[vertex] = inf

    for e in edges:
        adj[e[0]].add(e[1])

    for i in range(len(vertices) - 1):
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edges[edge]
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # check for negative weight cycles
    for edge in edges:
        u = edge[0]
        v = edge[1]
        w = edges[edge]
        if distance[u] + w < distance[v]:
            print("Graph contains negative weight cycles!")

    return distance


# Graph:
#        _B-------D
#      /` |       |
#    A<   |       |
#      \_ |       |
#        `C-------E

vertices = ['A', 'B', 'C', 'D', 'E']
edges = {('A', 'B'): 10,
         ('A', 'C'): 3,
         ('B', 'C'): 1,
         ('B', 'D'): 2,
         ('C', 'B'): 4,  # change to -4
         ('C', 'D'): 8,
         ('C', 'E'): 2,
         ('D', 'E'): 7,
         ('E', 'D'): 9}

# find shortest paths from 'A' to all other nodes
shortest_paths = bellman_ford(vertices, edges, 'A')
print(shortest_paths)
