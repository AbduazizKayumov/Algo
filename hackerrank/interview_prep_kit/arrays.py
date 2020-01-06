# https://www.hackerrank.com/challenges/2d-array/problem
def hourglassSum(A):
    max = -70
    for i in range(4):
        for j in range(4):
            sum = A[i][j] + A[i][j+1] + A[i][j+2] + A[i + 1][j + 1] + A[i+2][j] + A[i+2][j+1] + A[i+2][j+2]
            if sum > max:
                max = sum
    return max

# https://www.hackerrank.com/challenges/ctci-array-left-rotation/
def rotLeft(list, l):
    result = []
    result.extend(list[l:len(list)])
    result.extend(list[0:l])
    return result

# https://www.hackerrank.com/challenges/new-year-chaos/problem
def minimumBribes(list):
    sum = 0
    labels = {}
    for i in range(len(list)):
        labels[list[i]] = i + 1

    for i in range(1, len(list)):
        key = list[i]
        for j in range(i, 0, -1):
            if list[j - 1] > key:
                list[j] = list[j - 1]
                list[j - 1] = key
                sum += 1
            else:
                break

    chaos = False
    for i in range(len(list)):
        if list[i] - labels[i + 1] > 2:
            chaos = True
            break

    if chaos:
        print("Too chaotic")
    else:
        print(str(sum))

# https://www.hackerrank.com/challenges/minimum-swaps-2/problem
def minimumSwaps(list):
    swaps = 0
    labels = {}
    for i in range(len(list)):
        labels[list[i]] = i + 1

    for i in range(len(list)):
        if list[i] == i + 1:
            continue
        key = list[i]
        to = labels[i + 1] - 1

        list[i] = i + 1
        list[to] = key

        labels[key] = to + 1
        labels[i + 1] = i + 1

        swaps += 1
    return swaps

# https://www.hackerrank.com/challenges/crush/problem
def arrayManipulation(n, queries):
    f = [0] * (n+1)
    t = [0] * (n+1)

    for i in range(len(queries)):
        q = queries[i]
        f[q[0] - 1] +=  q[2]
        t[q[1] - 1] += -q[2]

    max = 0
    current = 0
    for i in range(n):
        current += f[i]
        if current > max:
            max = current
        current += t[i]
        if current > max:
            max = current
    return max