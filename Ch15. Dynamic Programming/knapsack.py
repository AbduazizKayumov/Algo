# Knapsack problem
# Given a knapsack (or backpack) with size S
# and items with their weights
# choose such items so that their weight is maximum

def knapsack(items, S, dp=None):
    if not items:
        return 0

    if dp is None:
        dp = {}

    if S in dp:
        return dp[S]

    # include this item
    item = 0
    if items[0] <= S:
        item = items[0]
    included = item + knapsack(items[1:], S - item, dp)

    # do not include this item
    not_included = knapsack(items[1:], S, dp)

    answer = max(included, not_included)
    dp[S] = answer
    return answer


def knapsack_dp_table(items, S):
    dp = []
    for i in items:
        dp.append([0] * (S + 1))
    dp.append([0] * (S + 1))
    # Requires O(N*S) memory
    # can be decreased to O(S)

    for i in range(1, len(items) + 1):
        for s in range(1, S + 1):
            include = 0
            if items[i - 1] <= s:
                include = items[i - 1]

            dp[i][s] = max(dp[i - 1][s], include + dp[i - 1][s - include])
    for d in dp:
        print(d)
    return dp[-1][-1]


items = [3, 4, 7, 15]
res = knapsack_dp_table(items, 12)
print(res)
