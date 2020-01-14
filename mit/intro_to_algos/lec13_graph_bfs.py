# Explore graph level by level from the starting vertex
def bfs(start, graph):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print("Visited " + vertex)
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


# Graph:
#    a------s      d------f
#    |      |   _-'|   _-'|
#    |      |_-'   |_-'   |
#    z      x------c------v

vertices = ['a', 'z', 'x', 's', 'd', 'c', 'f', 'v']
edges = [['a', 'z'],
         ['a', 's'],
         ['s', 'x'],
         ['x', 'd'],
         ['c', 'x'],
         ['d', 'c'],
         ['d', 'f'],
         ['c', 'v'],
         ['c', 'f'],
         ['f', 'v']]
graph = {}
for vertex in vertices:
    graph[vertex] = set()

for edge in edges:
    graph[edge[0]].add(edge[1])
    graph[edge[1]].add(edge[0])

bfs('s', graph)
# Applications:
# 1) Shortest path
# 2) Fb friend recommendations
# 3) Peer-to-peer networks
# 4) Garbage collectors in modern progamming langs
