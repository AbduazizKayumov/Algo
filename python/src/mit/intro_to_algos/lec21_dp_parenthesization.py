from math import inf


# Subproblems for strings / subsequences:
# 1) Suffixes A[i:]
# 2) Prefixes A[:i]
# 3) Subsequences A[i:j]

# Parenthesization
# Optimal evaluation of associative expression A1*A2*A3... e.g. multiplying rectangular matrices
#  A(n,1) * B(1,n) * C(n, 1)
# BAD:  (A*B)*C => AB(n,n)*C(n, 1) -> O(n^2)
# GOOD: A*(B*C) => A(n,1)*BC(1,1)  -> O(n)
#
# 1) What is the subproblem?
# a subsequence -> A[i:j]
# 2) Guessing:
# outermost multiplication at k
# # of choices = O(n)
# # of subproblems =  O(n^2)


def parenthesize(A, i, j, memo=None):
    if i == j - 1:
        return 0

    if memo is None:
        memo = {}

    if (i, j) in memo:
        return memo[(i, j)]

    minn = inf
    for k in range(i + 1, j):
        cost = A[i] * A[k] * A[j]
        count = cost + parenthesize(A, i, k, memo) + parenthesize(A, k, j, memo)
        if count < minn:
            minn = count

    memo[(i, j)] = minn
    return minn


def parenthesize_dp(A):
    dp = []
    n = len(A)
    for i in range(len(A)):
        dp.append([inf] * len(A))
    for i in range(len(A)):
        dp[i][i] = 0
        if i + 1 < len(A):
            dp[i][i + 1] = 0

    for i in range(n - 1, -1, -1):
        for j in range(n):
            if i == j - 1:
                continue
            minn = inf
            for k in range(i + 1, j):
                cost = A[i] * A[k] * A[j]
                count = cost + dp[i][k] + dp[k][j]
                if count < minn:
                    minn = count
            dp[i][j] = minn

    return dp[0][len(A)-1]


A = [1, 2, 3, 4, 3]
min_cost = parenthesize(A, 0, len(A) - 1)
print(min_cost)

min_cost = parenthesize_dp(A)
print(min_cost)
