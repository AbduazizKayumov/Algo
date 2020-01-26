from math import inf


def extract_min(Q, distance):
    pos = 0
    for i in range(len(Q)):
        if distance[Q[i]] < distance[Q[pos]]:
            pos = i
    return Q.pop(pos)

# Speed-up 2
# Bi-Directional search -> two-way Dijkstra: from source to target, from target to source
def b_dijkstra(vertices, edges, source, target):
    adj_s = {}
    adj_t = {}
    distance_s = {}
    distance_t = {}
    queue_s = []
    queue_t = []
    parent_s = {}
    parent_t = {}

    for vertex in vertices:
        adj_s[vertex] = set()
        adj_t[vertex] = set()

        queue_s.append(vertex)
        queue_t.append(vertex)

        if vertex == source:
            distance_s[vertex] = 0
        else:
            distance_s[vertex] = inf

        if vertex == target:
            distance_t[vertex] = 0
        else:
            distance_t[vertex] = inf

    weights = {}
    for e in edges:
        adj_s[e[0]].add(e[1])
        adj_t[e[1]].add(e[0])
        weights[(e[0], e[1])] = e[2]

    while queue_s:
        u_s = extract_min(queue_s, distance_s)

        for v in adj_s[u_s]:
            w = weights[(u_s, v)]
            if distance_s[u_s] + w < distance_s[v]:
                distance_s[v] = distance_s[u_s] + w
                parent_s[v] = u_s

        u_t = extract_min(queue_t, distance_t)
        for v in adj_t[u_t]:
            w = weights[(v, u_t)]
            if distance_t[u_t] + w < distance_t[v]:
                distance_t[v] = distance_t[u_t] + w
                parent_t[v] = u_t

        # terminate condition
        if u_s == u_t:  # u is discovered by both directions
            # however, the terminator may not be the solution
            print("Terminated at vertex: ", u_s)
            break

    # search for x that distance_s[x] + distance_t[x] is minimum
    x = source
    distance_x = -1
    for v in list(distance_s.keys()):
        if v not in distance_t:
            continue
        if distance_x == -1 or distance_s[v] + distance_t[v] < distance_x:
            distance_x = distance_s[v] + distance_t[v]
            x = v

    if x not in parent_t or x not in parent_s:
        # bidirectional search did not meet in any point
        # Dijkstra from source computed all shortest paths to target
        # Dijkstra from target computed all shortest paths to source
        print("Shortest distance: ", distance_s[target])
        print("Shortest path:")
        path = [target]
        p = parent_s[target]
        while p:
            path.append(p)
            if p in parent_s:
                p = parent_s[p]
            else:
                p = None
        path.reverse()
        print(path)
        return

    # build shortest path from source to x
    path = [x]
    p = parent_s[x]
    while p:
        path.append(p)
        if p in parent_s:
            p = parent_s[p]
        else:
            p = None
    path.reverse()

    # build shortest path from x to target
    path_t = []
    p = parent_t[x]
    while p:
        path_t.append(p)
        if p in parent_t:
            p = parent_t[p]
        else:
            p = None
    path.extend(path_t)

    print("Shortest distance: ", distance_s[x] + distance_t[x])
    print("Shortest path:")
    print(path)


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
b_dijkstra(vertices, edges, 'A', 'D')
