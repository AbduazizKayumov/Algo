# A queue is a data structure that follows FIFO (First In, First out) policy


class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, x):
        self.arr.append(x)

    def dequeue(self):
        return self.arr.pop()
