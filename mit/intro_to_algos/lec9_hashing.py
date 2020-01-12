# Karp-Rabin Algorithm for String matching
# s - search key, t is a document
# 1) Compare h(s) == h(t[i:i+len(s)])
# 2) If values match:
#       - check if s == t[i:i+len(s)] to be true
#       - if yes, return
#       - else, continue searching
# 3) We need a suitable hash function
# 4) We need a data structure that:
#       - can drop its first char in O(1)
#       - can add a new char in O(1)
#
# Karp-Rubin String matching algorithm takes:
#           O(len(s) + len(t)*amortized(O(1)))

def match(s, t):
    if len(s) > len(t):
        return False
    s_hash = hash(s)

    for i in range(len(t) - len(s)):
        current = t[i:i + len(s)]
        t_hash = hash(current)
        if t_hash == s_hash and s == current:
            return True
    return False


res = match("abc", "aaaaaaaaaabacabccccc")
print(res)
