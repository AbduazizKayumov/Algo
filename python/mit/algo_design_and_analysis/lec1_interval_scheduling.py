# Interval Scheduling
#
# Given requests 1..n (say from professors)
# Each request has s[i] and f[i] (start time and finish time)
# Schedule optimal timetable

# Approach 1: Greedy interval scheduling
# Use a simple rule to select a request i, reject all request that are incompatible with i
# repeat until all request are processed
#
# Possible rules:
# a) Select request that starts earlier, min(s[i])
#       |------------|
#          |-----||------|    <--BAD
# b) Select request that is smallest, min(f[i], s[i])
#       |-------||-------|
#             |----|          <--BAD
# c) Select request that has minimum incompatibles:
#       |-----||-----||-----||-----|
#           |-----||-----||-----|      <--BAD
#           |-----|       |-----|
# d) Select request with earliest finish time min(f[i]) <--GOOD


def schedule(intervals):
    answer = []
    while intervals:
        # find i with earliest f[i]
        f = 0
        for i in range(len(intervals)):
            if intervals[i][1] < intervals[f][1]:
                f = i
        current = intervals.pop(f)
        answer.append(current)

        # remove all incompatible request wit i
        finish = current[1]
        compatibles = []
        for i in range(len(intervals)):
            if intervals[i][0] >= finish:
                compatibles.append(intervals[i])

        intervals = compatibles.copy()

    return answer


intervals = [
    [9, 11],
    [11, 13],
    [13, 15],
    [15, 17],
    [10, 12],
    [12, 14],
    [14, 16],
    [10, 12],
    [14, 16],
    [10, 12],
    [14, 16]
]
res = schedule(intervals)
print(res)


# Weighted Interval Scheduling
# Assume, every request has a weight,
# schedule a timetable with max weight

def intervals_key(intervals):
    min_start = intervals[0][0]
    max_finish = intervals[0][1]

    for i in intervals:
        if i[0] < min_start:
            min_start = i[0]
        if i[1] > max_finish:
            max_finish = i[1]

    return (min_start, max_finish)


def compatible(x, intervals):
    answer = []
    for i in intervals:
        if i[0] >= x[1]:
            answer.append(i)
    return answer


# O(N^2)
def schedule(intervals, dp=None):
    if not intervals:
        return 0

    if dp is None:
        dp = {}

    key = intervals_key(intervals)
    if key in dp:
        return dp[key]

    _max = 0
    for i in range(len(intervals)):
        x = intervals[i]
        current = x[2] + schedule(compatible(x, intervals), dp)
        if current >= _max:
            _max = current

    dp[key] = _max
    return _max


# sort before
# O(NlogN)
def schedule_divide(intervals):
    if not intervals:
        return 0
    return max(schedule_divide(intervals[1:]), intervals[0][2] + schedule_divide(compatible(intervals[0], intervals)))


intervals = [
    [9, 10, 1],
    [10, 11, 1],
    [11, 12, 1],
    [12, 13, 1],
    [13, 14, 1],
    [9, 10, 2],
    [10, 11, 1],
    [11, 12, 1],
    [11, 12, 2]
]
intervals.sort()
res = schedule_divide(intervals)
print(res)
