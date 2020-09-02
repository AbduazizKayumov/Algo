from math import inf


# Problem definition:
# Given a rod with length n, that can be cut and sold in pieces. Cut the rod in a way such that
# it maximizes the profit.

# Solution 1. Recursive
# Time complexity: O(2^N)
# 2^N because cutting or not cutting is decided on each unit
def cut_rod(p, n):
    if n <= 0:
        return 0
    res = -inf
    for i in range(1, n + 1):
        res = max(res, p[i - 1] + cut_rod(p, n - i))

    return res


# Solution 2. Memoized + Recursive (Top-down)
def cut_rod_memoized(p, n, memo):
    if n <= 0:
        return 0

    if n in memo:
        return memo[n]

    res = -inf
    for i in range(1, n + 1):
        res = max(res, p[i - 1] + cut_rod_memoized(p, n - i, memo))
    memo[n] = res

    return res


# Solution 3. Memoized (Bottom-up)
def cut_rod_bottom_up(p, n):
    dp = [0] * n
    for j in range(1, n + 1):
        cur = -inf
        for i in range(1, j + 1):
            cur = max(cur, p[i - 1] + dp[j - i - 1])
        dp[j - 1] = cur
    return dp[-1]


p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 4
ans = cut_rod(p, n)

print("Recursive = ", ans)

ans = cut_rod_memoized(p, n, {})
print("Recursive + Memo = ", ans)

ans = cut_rod_bottom_up(p, n)
print("Memo (bottom up)  = ", ans)
