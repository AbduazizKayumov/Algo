# https://www.hackerrank.com/challenges/alternating-characters/problem
def alternatingCharacters(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    return count


# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
def makeAnagram(a, b):
    chars_a = [0] * 26
    for char in a:
        chars_a[ord(char) - 97] += 1

    chars_b = [0] * 26
    for char in b:
        chars_b[ord(char) - 97] += 1

    deletions = 0
    for i in range(len(chars_a)):
        deletions += abs(chars_a[i] - chars_b[i])

    return deletions


# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
def isValid(s):
    freq = {}
    for char in s:
        if not char in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    numbers = []
    for i in list(freq.values()):
        numbers.append(i)

    numbers.sort()

    for i in range(1, len(numbers) - 1):
        p = numbers[i - 1]
        c = numbers[i]
        n = numbers[i + 1]
        if p == c and p == n:
            continue

        if p != c and p != n and c != n:
            return "NO"

        if p != c and p != n:
            numbers[i - 1] -= 1
            if numbers[i - 1] == 0:
                numbers.pop(i - 1)
            break

        if c != p and c != n:
            numbers[i] -= 1
            if numbers[i] == 0:
                numbers.pop(i)
            break

        if n != p and n != c:
            numbers[i + 1] -= 1
            if numbers[i + 1] == 0:
                numbers.pop(i + 1)
            break

    for i in range(1, len(numbers)):
        p = numbers[i - 1]
        c = numbers[i]
        if p != c:
            return "NO"

    return "YES"


# https://www.hackerrank.com/challenges/special-palindrome-again/problem
def substrCount(n, s):
    count = 0

    freq = [[s[0], 1]]

    for i in range(1, len(s)):
        if s[i] == freq[-1][0]:
            freq[-1][1] += 1
        else:
            freq.append([s[i], 1])

    # check for the elements in freq ('aaa' can form (3+1)*3/2 palindromes)
    for i in range(len(freq)):
        count += (freq[i][1] + 1) * freq[i][1] // 2

    i = 1
    while len(freq) > i + 1:
        current = freq[i]

        if freq[i - 1][0] == freq[i + 1][0] and current[1] == 1:
            count += min(freq[i - 1][1], freq[i + 1][1])
        i += 1

    return count


# https://www.hackerrank.com/challenges/common-child/problem
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
def commonChild(R, C):
    n = len(R)
    m = len(C)

    prev = [0] * (m + 1)

    for i in range(1, n + 1):
        current = [0] * (m + 1)
        for j in range(1, m + 1):
            if R[i - 1] == C[j - 1]:
                current[j] = prev[j - 1] + 1
            else:
                current[j] = max(current[j - 1], prev[j])
        prev = current.copy()
        current.clear()

    return prev[-1]
