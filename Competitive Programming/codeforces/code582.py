q = int(input())
answers = []

for ti in range(q):
    ints = list(map(int, input().split()))
    n, m = ints[0], ints[1]

    digits = {}
    mult = 1
    while True:
        s = str(mult * m)
        mult += 1
        digit = int(s[-1])
        if digit in digits:
            break
        digits[digit] = 1

    digits = list(digits.keys())
    total = 0
    mult = n // m // len(digits)
    
    for i in range(len(digits)):
        total += mult * digits[i]

    rem = n // m % len(digits)
    for i in range(rem):
        total += digits[i]

    rem = n % m

    answers.append(total)

for a in answers:
    print(a)
