# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem
def fibonacci(n):
    # recursion
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
def stepPerms(n):
    # backtracking
    steps = [1, 2, 4]
    if n < 4:
        return steps[n - 1]
    for i in range(3, n):
        sum = steps[i - 1] + steps[i - 2] + steps[i - 3]
        steps.append(sum)
    return steps[n - 1]


# https://www.hackerrank.com/challenges/recursive-digit-sum/problem
def superDigit(n, k=1):
    if n < 10 and k == 1:
        return n

    s = str(n)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])

    return superDigit(sum * k)
