def unique(ll):
    dict = {}
    for s in ll:
        if s in dict:
            return False
        dict[s] = 1
    return True


s = input().split()
l = int(s[0])
r = int(s[1])

found = False
for i in range(l, r + 1):
    ans = list(str(i))
    if unique(ans):
        print(''.join(ans))
        found = True
        break

if not found:
    print("-1")
