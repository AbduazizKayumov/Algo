num1 = float(input())
operator = input()
num2 = float(input())

if operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
else:
    print("Unsupported operator")