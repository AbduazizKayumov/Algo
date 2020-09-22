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
            for k in range(i + 1, j):
                cost = A[i] * A[k] * A[j]
                count = cost + dp[i][k] + dp[k][j]
                if count < dp[i][j]:
                    dp[i][j] = count
    return dp[0][len(A) - 1]


def matrix_chain_order(p):
    n = len(p)
    m = [[0] * n for _ in range(n)]

    for l in range(2, n):           # l is the chain length
        for i in range(n - l):      # for each i 0<=i<n-l
            j = i + l               # compute optimal solution for a chain with length l
            m[i][j] = inf           # j = i + l
            for k in range(i, j):   # by traversing all k between i and j
                cost = m[i][k] + m[k][j] + p[i] * p[k] * p[j]
                m[i][j] = min(m[i][j], cost)
    for d in m:
        print(d)

    return m[0][n-1]


A = [1, 2, 3, 4, 3]
min_cost = parenthesize(A, 0, len(A) - 1)
print(min_cost)

min_cost = parenthesize_dp(A)
print(min_cost)

min_cost = matrix_chain_order(A)
print(min_cost)
