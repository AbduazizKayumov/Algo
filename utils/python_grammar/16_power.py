def power(num1, p):
    res = 1
    for i in range(p):
        res *= num1
    return res

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(2**3)
print(power(2,3))

for n in range(6):
    print(fibonacci(n))