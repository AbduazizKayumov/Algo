# https://www.hackerrank.com/challenges/torque-and-development/problem
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return n * c_lib

    graph = {}
    for i in range(1, n + 1):
        graph[i] = set()

    for c in cities:
        graph[c[0]].add(c[1])
        graph[c[1]].add(c[0])

    total = 0
    visited = {}
    for i in range(1, n + 1):
        if i in visited:
            continue
        l = list(dfs(graph, i))
        if len(l) == 1:
            total += c_lib
        else:
            for c in l:
                visited[c] = 1
            total += c_road * (len(l) - 1)
            total += c_lib

    return total


# https://www.hackerrank.com/challenges/find-the-nearest-clone/problem
def bfs(graph, start, colors):
    visited = set()
    queue = [start]
    path = 0
    while queue:
        current_node = queue.pop(0)
        if colors[current_node] == colors[start] and current_node != start:
            return path
        if current_node not in visited:
            visited.add(current_node)
            queue.extend(graph[current_node] - visited)
            path += 1
    return -1


def findShortest(graph_nodes, graph_from, graph_to, ids, color):
    graph = {}
    colors = {}

    # construct graph and
    for node in range(graph_nodes):
        graph[node + 1] = set()
        colors[node + 1] = ids[node]

    for i in range(len(graph_from)):
        graph[graph_from[i]].add(graph_to[i])
        graph[graph_to[i]].add(graph_from[i])

    # collect nodes that have the specified color we're looking for
    guys = set()
    for node in range(graph_nodes):
        if colors[node + 1] == color:
            guys.add(node + 1)

    shortest = -1
    paths = []
    for node in guys:
        path = bfs(graph, node, colors)
        if path != -1:
            paths.append(path)

    if len(paths) > 0:
        shortest = min(paths)

    return shortest


# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = {}
        for i in range(n):
            self.graph[i + 1] = set()

    def connect(self, x, y):
        self.graph[x].add(y)
        self.graph[y].add(x)

    def find_all_distances(self, start):
        visited = set()
        queue = [start]
        distances = {start: 0}

        while queue:
            node = queue.pop(0)

            if node not in visited:
                visited.add(node)

                remaining = self.graph[node] - visited
                queue.extend(remaining)

                for r in remaining:
                    if r not in distances:
                        distances[r] = distances[node] + 6

        res = ""
        for node in range(1, self.n + 1):
            if node == start:
                continue
            if node in distances:
                res += str(distances[node])
            else:
                res += "-1"
            if node != self.n:
                res += " "

        print(res)



# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem
def point(x, y, m):
    return x * m + y


def maxRegion(grid):
    ans = 0

    n, m = len(grid), len(grid[0])

    # prepare the graph
    graph = {}
    for i in range(len(grid)):
        for j in range(m):
            graph[i * m + j] = set()

    ones = set()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                continue
            ans = 1
            ones.add(point(i, j, m))

            # for every node, add it adjasent nodes that make a region together

            # i - 1, j - 1
            if i > 0 and j > 0 and grid[i - 1][j - 1] == 1:
                graph[point(i - 1, j - 1, m)].add(point(i, j, m))
                graph[point(i, j, m)].add(point(i - 1, j - 1, m))

            # i - 1, j
            if i > 0 and grid[i - 1][j] == 1:
                graph[point(i - 1, j, m)].add(point(i, j, m))
                graph[point(i, j, m)].add(point(i - 1, j, m))

            # i - 1, j + 1
            if i > 0 and j < m - 1 and grid[i - 1][j + 1]:
                graph[point(i - 1, j + 1, m)].add(point(i, j, m))
                graph[point(i, j, m)].add(point(i - 1, j + 1, m))

            # i, j - 1
            if j > 0 and grid[i][j - 1] == 1:
                graph[point(i, j - 1, m)].add(point(i, j, m))
                graph[point(i, j, m)].add(point(i, j - 1, m))

            # i, j + 1
            if j < m - 1 and grid[i][j + 1] == 1:
                graph[point(i, j + 1, m)].add(point(i, j, m))
                graph[point(i, j, m)].add(point(i, j + 1, m))

            # i + 1, j - 1
            if i < n - 1 and j > 0 and grid[i + 1][j - 1]:
                graph[point(i + 1, j - 1, m)].add(point(i, j, m))
                graph[point(i, j, m)].add(point(i + 1, j - 1, m))

            # i + 1, j
            if i < n - 1 and grid[i + 1][j] == 1:
                graph[point(i + 1, j, m)].add(point(i, j, m))
                graph[point(i, j, m)].add(point(i + 1, j, m))

            # i + 1, j + 1
            if i < n - 1 and j < m - 1 and grid[i + 1][j + 1] == 1:
                graph[point(i + 1, j + 1, m)].add(point(i, j, m))
                graph[point(i, j, m)].add(point(i + 1, j + 1, m))

    for one in list(ones):
        maybe = dfs(graph, one)
        if len(maybe) > ans:
            ans = len(maybe)

    return ans
