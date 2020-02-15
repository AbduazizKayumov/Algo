def sayhi():
    print("Hello")


def say_hi(name):
    print("Hello " + name)


def say_age(name, age):
    print("Hello " + name + ", you are " + str(age))


def cube(num):
    return num * num * num


sayhi()
say_hi("Mike")
say_age("Aziz", "23")
print(cube(3))
