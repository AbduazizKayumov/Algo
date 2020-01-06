# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
def minimumAbsoluteDifference(arr):
    arr.sort()
    m = arr[-1]
    for i in range(len(arr)):
        ab = abs(arr[i] - arr[i - 1])
        if ab < m:
            m = ab
    return m


# https://www.hackerrank.com/challenges/luck-balance/problem
def luckBalance(k, contests):
    # loose all not-important contests
    luck = sum(contest[0] for contest in contests if contest[1] == 0)
    important = []
    important.extend(list(contest[0] for contest in contests if contest[1] != 0))
    important.sort()
    important.reverse()

    print(important)

    for i in range(len(important)):
        if i < k:
            luck += important[i]
        else:
            luck -= important[i]

    return luck


# https://www.hackerrank.com/challenges/angry-children/problem
def maxMin(k, arr):
    arr.sort()
    m = arr[len(arr) - 1]
    for i in range(k, len(arr)):
        mn = arr[i - k]
        mx = arr[i]
        if mx - mn < m:
            m = mx - mn
    return m


# https://www.hackerrank.com/challenges/greedy-florist/problem
def getMinimumCost(k, c):
    c.sort()
    cost = 0

    cnt = 0
    sum = 0
    purchased = 0

    for i in range(len(c) - 1, -1, -1):
        cnt += 1
        sum += c[i]
        if cnt == k or i == 0:
            cost += (purchased + 1) * sum
            sum = 0
            purchased += 1
            cnt = 0
    return cost
