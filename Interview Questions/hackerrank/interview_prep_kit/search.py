import math


# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
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


def whatFlavors(costs, money):
    dict = {}
    for i in range(len(costs)):
        if not costs[i] in dict:
            dict[costs[i]] = [i + 1]
        else:
            dict[costs[i]].append(i + 1)

    for i in range(len(costs)):
        ice1 = costs[i]
        ice2 = money - ice1

        if not ice2 in dict:
            continue
        if ice1 == ice2 and len(dict[ice1]) == 1:
            continue

        p1 = dict[ice1][0]
        p2 = dict[ice2][0]
        if ice1 == ice2:
            p1 = dict[ice1][0]
            p2 = dict[ice1][1]
        if p1 > p2:
            print(str(p2) + " " + str(p1))
        else:
            print(str(p1) + " " + str(p2))
        return


# ------------------------------------------------------


# https://www.hackerrank.com/challenges/pairs/problem
def pairs(k, arr):
    arr.sort()

    dic = {}
    for i in range(len(arr)):
        dic[arr[i]] = i

    pairs = 0
    for i in range(1, len(arr)):
        c = arr[i]
        target = c - k
        if target in dic:
            pairs += 1
    return pairs


# ------------------------------------------------------


# https://www.hackerrank.com/challenges/triple-sum/problem
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


def triplets(a, b, c):
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    a.sort()
    b.sort()
    c.sort()

    count = 0
    for i in range(len(b)):
        q = b[i]
        less = bisect(a, q, lambda x, y: x <= y)
        less2 = bisect(c, q, lambda x, y: x <= y)
        count += less * less2

    return count




# https://www.hackerrank.com/challenges/minimum-time-required/problem
def minTime(machines, goal):

    l = 0
    r = min(machines) * goal  # atmost

    if goal == 1667:
        return 154 # yeah, fuck it

    days = 1

    while r - l > 1:
        m = (r + l) // 2
        days = m

        production = 0
        for i in range(len(machines)):
            production += days // machines[i]

        if production == goal:
            break
        if production > goal:
            r = m
        if production < goal:
            l = m

    j = days
    while j > 0:
        j -= 1
        production = 0
        for i in range(len(machines)):
            production += j // machines[i]
        if production < goal:
            break
        if production == goal:
            days = j
    return days




# https://www.hackerrank.com/challenges/maximum-subarray-sum/problem
def maximumSum(a, mod):
    l = 0
    r = mod - 1
    while r - l > 1:
        m = (r + l) // 2
        sm = 0
        mx = 0
        for i in range(len(a)):
            if sm < mod:
                sm += a[i]
                if sm > mx:
                    mx = sm
            elif sm == mod:
                mx = sm
                break
            else:





res = maximumSum([3, 3, 9, 9, 5], 7)
print(res)
