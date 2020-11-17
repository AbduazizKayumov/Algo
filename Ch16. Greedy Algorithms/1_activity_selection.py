# An activity selection problem
#
# Given activities with start and finish times, 
# select a maximum-size set of mutually compatible activities
# Activities a and b are compatible if they do not overlap each other

# Approach 1:
# We shall solve the problem using dynamic programming
# We decide to choose or not to choose for each activity.
# DP would be an overkill for this problem, since Greedy approach
# can solve it in O(n)

# Approach 2:
# Sort the activities by their finish time
# start picking activities with earliest finish time
# Greedy approach = local optimal solution leads to an optimal solution
# Greedy = "Choose the best now, fuck about the future"

def greedy_activity_selector(s, f):
	n = len(s)

	A = set()
	A.add(0)
	k = 0

	for m in range(1, n):
		if s[m] >= f[k]:
			A.add(m)
			k = m
	return A



s = [1, 3, 0, 5, 3, 5,  6,  8,  8,  2, 12]  # start times
f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]	# finish times
A = greedy_activity_selector(s, f)
print(A)