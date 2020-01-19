from math import inf


# 5 easy steps to dynamic programming
# 1) Define subproblems
# 2) Guess (part of a problem)
# 3) Relate subproblem solutions
# 4) Recurse + memoize
#    or build DP table bottom-up check subproblems acyclic/topological order
# 5) Solve original problem := a subproblem
#    or by combining subproblem solutions

# Text justification
# Split text into good lines
# - obvious solution: put as many words that fit on first line, repeat
#   but this can make very bad lines:
#   BAD (100 badness)                           GOOD(50)
# blah blah blah                           blah_blah       <--5 empty - 5^2
# blah            <---10 empty - 10^2      blah_blah       <--5 empty - 5^2
# reallylongword                           reallylongword

def badness(text, line_width):
    total_width = 0
    for word in text:
        total_width += len(word)

    # add spaces
    total_width += len(text) - 1

    if total_width > line_width:
        return inf

    return (total_width - line_width) ** 2


def justify(text, start=0, line_width=None, dp=None):
    n = len(text)

    if start >= n:
        return 0

    if dp is None:
        dp = {}

    if start in dp:
        return dp[start]

    if line_width is None:
        line_width = len(text[0])
        for i in range(1, len(text)):
            if line_width < len(text[i]):
                line_width = len(text[i])

    minn = inf
    for end in range(start + 1, n + 1):
        current = badness(text[start:end], line_width) + justify(text, end, line_width, dp)
        if current < minn:
            minn = current

    dp[start] = minn
    return minn


text = [
    "blah", "blah", "blah", "blah", "reallylongword"
]
res = justify(text)
print(res)  # 50, with greedy approach it gives 100 badness
