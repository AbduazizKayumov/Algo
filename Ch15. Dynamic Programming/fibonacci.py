# Dynamic programming
# ~ controlled brute force
# ~ recursion + re-use
# ~ try all guesses -> solve sub-subproblems -> memoize

# Example 1: Fibonacci
# Naive approach: O(2^N) -> exponential is bad
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Memoized DP approach
def fibonacci_dp(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    f = fibonacci_dp(n - 1, memo) + fibonacci_dp(n - 2, memo)
    memo[n] = f
    return f


# Bottom-up DP approach
# 1) Practically faster (no recursions)
# 2) Saves space (only remember last two numbers)
# There is O(lgn) time algorithm for Fibonacci, via diff. techniques ;-)
def fibonacci_bottom_up_dp(n):
    if n <= 2:
        return 1
    f1 = 1
    f2 = 1
    f = 0
    for i in range(2, n):
        f = f1 + f2
        f1, f2 = f2, f
    return f