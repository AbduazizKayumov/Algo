# https://www.hackerrank.com/challenges/ctci-ransom-note/problem
def checkMagazine(magazine, note):
    dict = {}
    for c in magazine:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1

    for c in note:
        if not c in dict:
            return "No"
        if dict[c] <= 0:
            return "No"
        dict[c] -= 1

    return "Yes"


# https://www.hackerrank.com/challenges/two-strings/problem
def twoStrings(s1, s2):
    dict = {}

    for c in s1:
        dict[c] = 1

    for c in s2:
        if c in dict:
            return "Yes"

    return "No"


# https://www.hackerrank.com/challenges/count-triplets-1/problem
def countTriplets(numbers, r):
    # clean the data
    arr = []
    for n in numbers:
        if n == 1 or n % r == 0:
            arr.append(n)

    right = {}
    for i in range(len(arr)):
        if arr[i] in right:
            right[arr[i]] += 1
        else:
            right[arr[i]] = 1

    left = {}
    count = 0
    for i in range(len(numbers)):
        mid = numbers[i]
        if mid in right:
            right[mid] -= 1

        left_count = 0
        if mid / r in left:
            left_count = left[mid / r]
        right_count = 0
        if mid * r in right:
            right_count = right[mid * r]

        if mid in left:
            left[mid] += 1
        else:
            left[mid] = 1
        count += left_count * right_count

    return count


# https://www.hackerrank.com/challenges/frequency-queries/problem
def freqQuery(queries):
    answer = []

    arr = {}
    freq = {}

    INSERT = 1
    DELETE = 2
    CHECK_FREQ = 3

    for q in queries:
        command = q[0]
        value = q[1]
        if command == INSERT:
            if value not in arr:
                arr[value] = 1
                if 1 not in freq:
                    freq[1] = set()
                freq[1].add(value)
            else:
                f = arr[value]
                arr[value] += 1

                if f in freq:
                    freq[f].remove(value)
                    if len(freq[f]) == 0:
                        freq.pop(f)

                if arr[value] not in freq:
                    freq[arr[value]] = set()
                freq[arr[value]].add(value)
        elif command == DELETE:
            if value in arr:
                f = arr[value]
                arr[value] -= 1

                if f in freq:
                    freq[f].remove(value)
                    if len(freq[f]) == 0:
                        freq.pop(f)

                if arr[value] <= 0:
                    arr.pop(value)
                else:
                    if arr[value] not in freq:
                        freq[arr[value]] = set()
                    freq[arr[value]].add(value)
        elif command == CHECK_FREQ:
            if value in freq:
                answer.append(1)
            else:
                answer.append(0)

    return answer


# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
def sherlockAndAnagrams(s):
    substrings = {}
    for i in range(len(s)):
        if ("" + s[i]) in substrings:
            substrings[""+s[i]] += 1
        else:
            substrings[s[i] + ""] = 0

        for j in range(i+1, len(s)):
            sub = s[i:j+1]
            sub = ''.join(sorted(sub))
            if sub in substrings:
                substrings[sub] += 1
            else:
                substrings[sub] = 0
    pairs = 0
    # print(substrings)
    for value in substrings.values():
        pairs += (value + 1) * value // 2

    return pairs
