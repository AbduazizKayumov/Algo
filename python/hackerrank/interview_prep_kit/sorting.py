import math


# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
def countSwaps(a):
    swaps = 0
    for i in range(len(a)):
        for j in range(1, len(a)):
            if a[j] < a[j - 1]:
                key = a[j]
                a[j] = a[j - 1]
                a[j - 1] = key
                swaps += 1
    print("Array is sorted in " + str(swaps) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[len(a) - 1]))


# https://www.hackerrank.com/challenges/mark-and-toys/problem
def maximumToys(prices, k):
    count = 0
    prices.sort()
    for i in range(len(prices)):
        if k - prices[i] >= 0:
            count += 1
            k -= prices[i]
        else:
            break
    return count


# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
def allowed(days):
    d = len(days)
    midIndex = math.floor(d / 2)
    threshold = days[midIndex]
    if d % 2 == 0:
        threshold += days[midIndex - 1]
    else:
        threshold += threshold
    return threshold


def bisect(arr, val, cmp):
    l = -1
    r = len(arr)
    while r - l > 1:
        e = (l + r) >> 1
        if cmp(arr[e], val):
            l = e
        else:
            r = e
    return r


def activityNotifications(expenditure, d):
    if d >= len(expenditure):
        return 0
    notifies = 0

    days = expenditure[0:d]
    days.sort()
    spending = expenditure[d]
    m = allowed(days)
    if spending >= m:
        notifies += 1

    for i in range(d, len(expenditure) - 1):
        rempos = bisect(days, expenditure[i - d], lambda x, y: x < y)
        days.pop(rempos)

        pos = bisect(days, expenditure[i], lambda x, y: x < y)
        days.insert(pos, expenditure[i])

        spending = expenditure[i + 1]
        limit = allowed(days)
        if spending >= limit:
            notifies += 1

    return notifies


# ------------------------------------------------------


# https://www.hackerrank.com/challenges/ctci-merge-sort/problem
class Sort():
    def __init__(self, swaps=0):
        self.swaps = swaps

    def merge(self, left, right):
        list = []
        l = 0
        r = 0

        while l < len(left) or r < len(right):
            if l < len(left) and r < len(right):
                if left[l] > right[r]:
                    list.append(right[r])
                    # there at length - l bigger elements in left
                    # which means the bigger ones and right[r] are inversions
                    self.swaps += len(left) - l
                    r = r + 1
                else:
                    list.append(left[l])
                    l = l + 1
            elif l < len(left):
                list.extend(left[l:len(left)])
                break
            elif r < len(right):
                list.extend(right[r:len(right)])
                break

        return list

    def merge_sort(self, list):
        if len(list) == 1:
            return list

        mid = int(len(list) / 2)
        left = list[0:mid]
        right = list[mid:len(list)]

        return self.merge(self.merge_sort(left), self.merge_sort(right))


def countInversions(arr):
    sort = Sort()
    sort.merge_sort(arr)
    return sort.swaps


# https://www.hiredintech.com/classrooms/algorithm-design/lesson/19/task/16
def sort_the_files(n, result):

    def dfs(filename):
        if int(filename) > n or len(result) > n:
            return
        result.append("IMG" + str(filename) + ".jpg")
        for c in "0123456789":
            dfs(filename + c)

    n = min(n, 1000)
    for c in "123456789":
        dfs(c)
    return result


res = sort_the_files(1000, [])
print(res)
