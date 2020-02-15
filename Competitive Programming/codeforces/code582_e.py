n = int(input())
s = input()
t = input()

a = []
b = []
c = []

answer = ""
for i in range(n):
    answer += "a"

for i in range(n):
    answer += "b"

for i in range(n):
    answer += "c"

for i in range(1, 3 * n):
    curr = ""
    curr += answer[-1]
    curr += a.pop()
