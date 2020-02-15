from math import inf


# Given two strings x and y, what is the cheapest way to convert x into y?
# There are 3 operations:
# 1) Insert y[i] into x
# 2) Delete x[i]
# 3) Replace x[i] with y[j]


def lcs(x, y):
    dp = [0] * (len(x) + 1)

    for i in range(1, len(y) + 1):

        column = [0] * (len(x) + 1)

        for j in range(1, len(x) + 1):
            if x[j - 1] == y[i - 1]:
                column[j] = dp[j - 1] + 1
            else:
                column[j] = max(column[j - 1], dp[j])

        dp = column.copy()
    print(dp)


lcs("HIEROGLYPHOLOGY", "MICHAELANGELO")  # HELLO
lcs([10, 7], [10, 2, 7, 10])
