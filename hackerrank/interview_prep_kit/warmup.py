import math


# https://www.hackerrank.com/challenges/sock-merchant/problem
def sockMerchant(n, ar):
    ar.sort()
    sum = 1
    pairs = 0
    for i in range(1, n):
        if ar[i] != ar[i - 1]:
            pairs += sum / 2
            sum = 1
        elif i == n - 1:
            if (ar[i] == ar[i - 1]):
                sum += 1
            pairs += sum / 2
        else:
            sum += 1
    return pairs


# https://www.hackerrank.com/challenges/counting-valleys/problem
def countingValleys(n, s):
    current = 0
    valleys = 0
    for i in range(n):
        prev = current
        if s[i] == "U":
            current = current + 1
        else:
            current = current - 1
        if prev >= 0 and current < 0:
            valleys = valleys + 1
    return valleys


# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
def jumpingOnClouds(c):
    jumps = -1
    i = 0
    while i < len(c):
        jumps += 1
        if i + 2 < len(c) and c[i + 2] != 1:
            i += 2
            continue
        i += 1
    return jumps


# https://www.hackerrank.com/challenges/repeated-string/problem
def repeatedString(s, n):
    count = s.count('a')
    endCount = s[0:(n % len(s))].count('a')
    return math.floor(n / len(s)) * count + endCount
