n = int(input())
s = list(input())
count = 0
for i in range(1, len(s)):
    if i % 2 == 0:
        continue
    if s[i] == 'a':
        # s[i-1] must be 'b'
        if s[i-1] == 'a':
            count += 1
            s[i-1] = 'b'
    else:
        # s[i-1] must be 'b'
        if s[i-1] == 'b':
            count += 1
            s[i-1] = 'a'

print(count)
print(''.join(s))

