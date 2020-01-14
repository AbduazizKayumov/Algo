# Follow path until you get stuck
# If stuck, go back and visit neighbor
def dfs(start, graph, visited=None):
    if visited is None:
        visited = set()
    if start not in visited:
        visited.add(start)
        print("Visited " + start)
        for vertex in graph[start] - visited:
            dfs(vertex, graph, visited)
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

dfs('s', graph)

# Applications:
# 1) Cycle detection iff DFS has a back edge
# 2) Job scheduling: topological sort
