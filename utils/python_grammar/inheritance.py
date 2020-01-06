class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def say_hello(self):
        print("Hello")


class PHDStudent(Student):

    #override
    def say_hello(self):
        print("Good day")

    def research(self):
        print("Researching something")
