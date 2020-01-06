try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ZeroDivisionError:
    print("Zero division error")
except ValueError as err:
    print(err)