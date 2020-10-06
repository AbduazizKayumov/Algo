from math import inf


# Given two strings x and y, what is the cheapest way to convert x into y?
# There are 3 operations:
# 1) Insert y[i] into x
# 2) Delete x[i]
# 3) Replace x[i] with y[j]

def editDistance(w1: str, w2: str) -> int:
    n, m = len(w1), len(w2)
    dp = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(n+1):
        dp[i][0] = i

    for j in range(m+1):
        dp[0][j] = j

    # find lcs
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if w1[i - 1] == w2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] # if cur chars are equal, cur state is equal to prev. state
            else:
                # else: we need to edit, so +1 operation and min of prev.states (insert, delete or replace)
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    for d in dp:
        print(d)

    return dp[-1][-1]


editDistance("horse", "ros")
editDistance("intention", "execution")
editDistance("HIEROGLYPHOLOGY", "MICHAELANGELO")  # HELLO
editDistance([10, 7], [10, 2, 7, 10])
