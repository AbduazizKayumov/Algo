# A stack is a data structure that follows LIFO (Last In, First Out) policy.
class Stack:
    def __init__(self, size):
        self.size = size
        self.top = 0
        self.arr = [0] * size

    def is_empty(self):
        return self.top == 0

    def push(self, x):
        self.arr[self.top] = x
        self.top += 1

    def pop(self):
        if self.is_empty():
            return -1
        self.top -= 1
        return self.arr[self.top + 1]
