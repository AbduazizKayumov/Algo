from math import inf


# Dijkstra Algorithm to find shortest path
#
# 1) Assign zero to starting node and infinity (∞) to all other nodes
# 2) Add all nodes to non-visited priority queue - Q
# 3) While Q is not empty:
#       current_node = extract (remove) min from Q (which is the starting node at first)
#       set the min dist. to all the neighbors from the current node

def extract_min(Q, distance):
    pos = 0
    for i in range(len(Q)):
        if distance[Q[i]] < distance[Q[pos]]:
            pos = i
    return Q.pop(pos)


def dijkstra(vertices, edges, start):
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

    paths = []
    while queue:
        u = extract_min(queue, distance)
        paths.append((u, distance[u]))
        for v in adj[u]:
            w = edges[(u, v)]
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    paths.sort()
    return paths


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
         ('C', 'B'): 4,
         ('C', 'D'): 8,
         ('C', 'E'): 2,
         ('D', 'E'): 7,
         ('E', 'D'): 9}

# find shortest paths from 'A' to all other nodes
shortest_paths = dijkstra(vertices, edges, 'A')
print(shortest_paths)
