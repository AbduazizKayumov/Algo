def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        for j in range(i, 0, -1):
            if list[j - 1] > key:
                list[j] = list[j - 1]
                list[j - 1] = key
            else:
                break
    return list


def merge(left, right):
    list = []
    l = 0
    r = 0
    while l < len(left) or r < len(right):
        if l < len(left) and r < len(right):
            if left[l] <= right[r]:
                list.append(left[l])
                l = l + 1
            else:
                list.append(right[r])
                r = r + 1
            continue
        if l < len(left):
            list.append(left[l])
            l = l + 1
        if r < len(right):
            list.append(right[r])
            r = r + 1
    return list


def merge_sort(list):
    if len(list) == 1:
        return list

    mid = int(len(list) / 2)
    left = list[0:mid]
    right = list[mid:len(list)]

    return merge(merge_sort(left), merge_sort(right))


# bisect(arr, key, lambda x, y: x > y)
def bisect(arr, val, cmp):
    l = -1
    r = len(arr)
    while r - l > 1:
        e = (l + r) >> 1  # divide by 2
        if cmp(arr[e], val):
            l = e
        else:
            r = e
    return r


# returns -1 of not found
def binary_search(arr, val):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) >> 1
        if arr[m] == val:
            return m
        if arr[m] > val:
            r = m
        if arr[m] < val:
            l = m
    return -1


def string_to_int_list(s):
    return list(map(int, s.split()))


def all_capitals(s):
    return ''.join([c for c in s if c.isupper()])


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited


# longest common subsequence
def lcs(a, b):
    m = len(a)
    n = len(b)

    A = a.upper()
    column = [0] * (m + 1)

    for i in range(1, n + 1):
        current = [0] * (m + 1)
        for j in range(1, m + 1):
            if b[i - 1] == A[j - 1]:
                current[j] = column[j - 1] + 1
            else:
                current[j] = max(current[j - 1], column[j])
        column = current.copy()
        current.clear()

    return column[-1]


def is_permutation(a, b):
    a = list(a)
    a.sort()

    b = list(b)
    b.sort()

    if a == b:
        return True
    return False
