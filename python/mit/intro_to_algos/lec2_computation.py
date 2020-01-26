L1 = [1, 2, 3]
L2 = [4, 5, 6]

L = L1 + L2  # O(1 + |L1| + |L2|) time

L[0] = L[1] + 20  # O(1) time

L.append(12)  # O(1) time

L1.extend(L2)  # O(1 + |L2|) time

i, j = 0, 3
L2 = L1[i:j]  # O(1 + j - i) time

exists = 2 in L2  # O(|L2|) time

length = len(L)  # O(1) time

L.sort()  # O(nlogn) time (comparison sort)

# hashing
D = {}
D[1] = "One"  # O(1) time
exists = 1 in D  # O(1) time

S = {1, 1, 2, 3} # a set is dictionary without values

# heappush and heappop: # O(logn) time