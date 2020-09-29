# Let X and Y be sequences:
# dp[i][j] is the length of an LCS of X, Y
# dp[i][j] = 0 if i == 0 or j == 0
#          = dp[i-1][j-1] + 1 if x[i] == y[j]   # if current chars are same, then adding 1 will produce greater LCS
#          = max(dp[i-1][j], dp[i][j-1])        # if current chars are not same, then LCS is one of two options:
#                                                 Make LCS by removing cur char from X or Y (try both, take the max)

def longest_common_subsequence(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    dp = []
    for i in range(n + 1):
        dp.append([0] * (m + 1))

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[-1][-1]


s1 = "ABCBDAB"
s2 = "BDCABA"
res = longest_common_subsequence(s1, s2)
print(res)
