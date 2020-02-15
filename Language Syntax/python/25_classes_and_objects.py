from inheritance import Student, PHDStudent

student1 = Student("John", "CSE", 4.41, False)
student2 = PHDStudent("Mike", "Art", 2.5, True)

print(student1.say_hello())
print(student2.say_hello())