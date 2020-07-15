from math import inf


# Given a problem of size n, divide it into subproblems of size n/b, a>=1, b > 1.
# Solve each subproblem recursively. Combine solution of subproblems to get overall solution:
#       T(N) = aT(n/b) + [work to merge]
# Merge-sort is the classic example

# Convex Hull
# Given n points in plane:
#   - no two points have the same x coordinate,
#   - no two points have the same y coordinate
#   -> no three in a line for convenience
#
# Convex Hull - the smallest polygon containing all points in S
# and is represented by the sequence of points on the boundary in order clockwise as
# doubly-linked list
#
# Solution 1: Brute-force
# Test each line segment to see if it makes up the edge of the convex hull:
# - if the rest of the points are on one side of the segment, the segment is on the convex hull
# - else, the segment is not
# -> O(N^2) edges, O(N) testes -> O(N^3) complexity
#
# Solution 2: Divide & conquer Convex hull
# 1) Sort points by x coord
# 2) For input set S of points:
#       * Divide into left half A and right half B by x coords
#       * Compute left and right halves
#       * Combine two halves (merge step)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.prev = None

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


def height(a, b, x):
    if a == b:
        return -inf
    slope = (a.y - b.y) / (a.x - b.x)
    c = a.y - slope * a.x
    return x * slope + c


def trench(a, b, x):
    if a == b:
        return inf
    slope = (a.y - b.y) / (a.x - b.x)
    c = a.y - slope * a.x
    return x * slope + c


def convex(s):
    if len(s) <= 2:
        for i in range(1, len(s)):
            s[i - 1].next = s[i]
            s[i].prev = s[i - 1]
        s[-1].next = s[0]
        s[0].prev = s[-1]
        return s

    mid = len(s) // 2
    A = s[:mid]
    B = s[mid:]

    a = convex(A)[-1]
    b = convex(B)[0]
    x = (a.x + b.x) / 2

    while height(a.prev, b, x) > height(a, b, x) or height(a, b.next, x) > height(a, b, x):
        if height(a.prev, b, x) > height(a, b, x):
            a = a.prev
        else:
            b = b.next

    a.next = b
    b.prev = a

    while trench(a.prev, b, x) < trench(a, b, x) or trench(a, b.next, x) < trench(a, b, x):
        if trench(a.prev, b, x) < trench(a, b, x):
            a = a.prev
        else:
            b = b.next

    a.prev = b
    b.next = a

    ans = [a]
    current = a.next
    while current != a:
        ans.append(current)
        current = current.next

    return ans


a = Point(1, 1)
b = Point(2, 10)
c = Point(7, 12)
d = Point(9, 9)
e = Point(8, 4)
f = Point(5, 0.1)
g = Point(3, 3)
h = Point(7.5, 5)
i = Point(6, 6)
j = Point(4, 8)
points = [a, b, c, d, e, f, g, h, i, j]
points.sort(key=lambda k: k.x)
res = convex(points)
print(*res)
