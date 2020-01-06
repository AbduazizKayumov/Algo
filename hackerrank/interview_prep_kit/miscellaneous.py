import math


# https://www.hackerrank.com/challenges/flipping-bits/problem
def flippingBits(n):
    return 4294967295 - n


# https://www.hackerrank.com/challenges/ctci-big-o/problem
def primality(n):
    if n == 1:
        return "Not prime"
    if n == 2:
        return "Prime"
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return "Not prime"
    return "Prime"


# https://www.hackerrank.com/challenges/friend-circle-queries/problem
class Node:
    def __init__(self):
        self.parent = None
        self.count = 1

    def root(self):
        # go up as much as possible, if none return self
        if self.parent is None:
            return self
        return self.parent.root()

    def hand_shakes(self, other):
        # make sure self is not connected with other:
        # connect if other's root is not self.root
        # connect a shorter tree to taller tree, not vice versa
        # https://algorithms.tutorialhorizon.com/disjoint-set-union-find-algorithm-union-by-rank-and-path-compression/
        self_root = self.root()
        other_root = other.root()
        count = 0
        if self_root is not other_root:
            if self_root.count > other_root.count:
                other_root.parent = self_root
                self_root.count += other_root.count
                count = self_root.count
            else:
                self_root.parent = other_root
                other_root.count += self_root.count
                count = other_root.count
        return count


def maxCircle(queries):
    citizens = set()
    for q in queries:
        citizens.add(q[0])
        citizens.add(q[1])

    citizens = list(citizens)
    people = {}
    for citizen in citizens:
        people[citizen] = Node()

    res = []
    mx = 0
    for q in queries:
        person1 = people[q[0]]
        person2 = people[q[1]]

        count = person1.hand_shakes(person2)
        if mx < count:
            mx = count
        res.append(mx)

    return res
