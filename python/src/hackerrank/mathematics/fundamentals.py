import math
from math import gcd


# https://www.hackerrank.com/challenges/find-point/problem
def findPoint(px, py, qx, qy):
    dx = 2 * abs(px - qx)
    dy = 2 * abs(py - qy)
    if qx < px:
        dx = -dx
    if qy < py:
        dy = - dy
    return [px + dx, py + dy]


# https://www.hackerrank.com/challenges/maximum-draws/problem
def maximumDraws(n):
    return n + 1


# https://www.hackerrank.com/challenges/handshake/problem
def handshake(n):
    return (n + 1) * n // 2 - n


# https://www.hackerrank.com/challenges/lowest-triangle/problem
def lowestTriangle(base, area):
    # Complete this function
    return math.ceil(2 * area / base)


# https://www.hackerrank.com/challenges/game-with-cells/problem
def gameWithCells(n, m):
    drops_n = math.ceil(n / 2)
    drops_m = math.ceil(m / 2)
    return drops_n * drops_m


# https://www.hackerrank.com/challenges/leonardo-and-prime/problem
def primeCount(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    count = 0
    mult = 1
    for p in primes:
        mult *= p
        if mult > n:
            break
        count += 1
    return count


# https://www.hackerrank.com/challenges/connecting-towns/problem
def connectingTowns(n, routes):
    res = 1
    for r in routes:
        res *= r
    return res % 1234567


# https://www.hackerrank.com/challenges/p1-paper-cutting/problem
def paper_cut(n, m):
    return n * m - 1


# https://www.hackerrank.com/challenges/summing-the-n-series/problem
def summingSeries(n):
    s = n * n
    if s < 1000000007:
        return s
    return s % 1000000007


# https://www.hackerrank.com/challenges/sherlock-and-moving-tiles/problem
def movingTiles(l, v1, v2, queries):
    if v1 == v2:
        return [0] * len(queries)
    answers = []
    d = math.sqrt(2) * l
    for q in queries:
        overlap = math.sqrt(q) * math.sqrt(2)
        t = (d - overlap) / abs(v1 - v2)
        answers.append(t)
    return answers


# https://www.hackerrank.com/challenges/best-divisor/problem
def bestDivisor(n):
    best = 1
    sm = 1
    for i in range(1, n + 1):
        if n % i != 0:
            continue
        s = str(i)
        tmp = 0
        for c in s:
            tmp += int(c)
        if tmp > sm:
            best = i
            sm = tmp
    return best


# https://www.hackerrank.com/challenges/restaurant/problem
def restaurant(l, b):
    best = l * b
    for i in range(1, min(l, b) + 1):
        if l % i == 0 and b % i == 0:
            best = l // i * b // i

    return best


# https://www.hackerrank.com/challenges/reverse-game/problem
def reverse_game(n, k):
    answer = []
    index = {}
    for i in range(n // 2 + 1):
        answer.append(n - i - 1)
        index[n - i - 1] = len(answer) - 1
        if n - i - 1 == i:
            continue
        answer.append(i)
        index[i] = len(answer) - 1
    return index[k]


# https://www.hackerrank.com/challenges/strange-grid/problem
def strangeGrid(r, c):
    answer = (c - 1) * 2
    if r % 2 == 0:
        answer += r // 2
        answer += (r // 2 - 1) * 9
    else:
        answer += r // 2
        answer += r // 2 * 9
    return answer


# https://www.hackerrank.com/challenges/diwali-lights/problem
def lights(n):
    return (2 ** n - 1) % 10000


# https://www.hackerrank.com/challenges/sherlock-and-divisors/problem
def divisors(n):
    if n % 2 != 0:
        return 0

    count = 0
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                count += 1
            if (n // i) % 2 == 0 and n // i != i:
                count += 1

    return count


# https://www.hackerrank.com/challenges/halloween-party/problem
def halloweenParty(k):
    return k // 2 * (k - k // 2)


# https://www.hackerrank.com/challenges/filling-jars/problem
def solve_operations(n, operations):
    sm = 0
    for op in operations:
        sm += (abs(op[0] - op[1]) + 1) * op[2]

    return sm // n


# https://www.hackerrank.com/challenges/is-fibo/problem
def is_fibo(n):
    if n < 0:
        return "IsNotFibo"
    if n == 0 or n == 1:
        return "IsFibo"
    fibo = [0, 1]
    while fibo[-1] < n:
        fi = fibo[-1] + fibo[-2]
        if fi == n:
            return "IsFibo"
        fibo.append(fi)
    return "IsNotFibo"


# https://www.hackerrank.com/challenges/sherlock-and-permutations/problem
def sherlock_and_permutations(n, m):
    fact = {}
    fact[0] = 1
    fact[1] = 1
    for i in range(2, n + m):
        fact[i] = i * fact[i - 1]

    return (fact[n + m - 1] // (fact[n] * fact[m - 1])) % 1000000007


# https://www.hackerrank.com/challenges/harry-potter-and-the-floating-rocks/problem
def potter_rocks(x1, y1, x2, y2):
    return gcd(y1 - y2, x1 - x2) - 1



# https://www.hackerrank.com/challenges/even-odd-query/problem
def even_odd_query(arr, queries):
    results = []
    for query in queries:
        if query[0] < len(arr) and arr[query[0]] == 0 and query[0] != query[1]:
            results.append("Odd")
        elif arr[query[0]-1] % 2 == 0:
            results.append("Even")
        else:
            results.append("Odd")
    return results


# https://www.hackerrank.com/challenges/even-odd-query/problem
def nine_zeros(n):
    ans = 9
    b = 1
    while ans % n != 0:
        binary = str(bin(b))[2:]
        ans = int(binary) * 9
        b += 1
    return ans
