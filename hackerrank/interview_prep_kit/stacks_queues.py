import  math

# https://www.hackerrank.com/challenges/balanced-brackets/problem
def isBalanced(s):
    stack = []

    math.ceil()

    brackets = {'(': ')', '{': '}', '[': ']'}

    for c in s:
        if c is '{' or c is '[' or c is '(':
            stack.insert(0, c)
        else:
            if len(stack) == 0:
                return "NO"
            else:
                top = stack[0]
                if brackets[top] == c:
                    stack.pop(0)
                else:
                    return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem
class MyQueue(object):
    def __init__(self):
        self.queue = []

    def peek(self):
        return self.queue[0]

    def pop(self):
        self.queue.pop(0)

    def put(self, value):
        self.queue.append(value)


# https://www.hackerrank.com/challenges/largest-rectangle/problem
def largestRectangle(histogram):
    largest = 0
    pos = []
    heights = []

    for i in range(len(histogram)):
        if len(pos) == 0 or histogram[i] >= heights[-1]:
            pos.append(i)
            heights.append(histogram[i])
        else:
            # keep popping that stack shit if heights[i] > histogram[i]
            last = 0
            while len(pos) > 0 and histogram[i] < heights[-1]:
                current = heights[-1] * (i - pos[-1])
                if current > largest:
                    largest = current
                last = pos[-1]
                pos.pop(-1)
                heights.pop(-1)
            pos.append(last)
            heights.append(histogram[i])

    # work on the remaining stack
    while len(pos) > 0:
        current = heights[-1] * (len(histogram) - pos[-1])
        if current > largest:
            largest = current
        pos.pop(-1)
        heights.pop(-1)

    return largest


# https://www.hackerrank.com/challenges/min-max-riddle/problem
def riddle(arr):
    n = len(arr)
    arr.append(-1)
    stack = []
    map = {}

    for i in range(len(arr)):
        # print(arr[i])
        while stack and arr[i] <= stack[-1][1]:
            building = stack.pop()
            height = i - building[0]
            map[i] = max(building[0], map.get(height, 0))
        stack.append([i, arr[i]])
    answers = []

    print(map)

    return answers


#res = riddle([5, 4, 3, 2, 1])
#print(res)

res = riddle([2, 6, 1, 12])
print(res)

res = riddle([1, 2, 3, 5, 1, 13, 3])
print(res)