from math import inf

# Optimal BST
# Given a dictionary of keys with their usage probabilities
# Find an optimal binary search tree which minimizes the 
# search cost.
# The expected search cost is the sum of all nodes' depths * probability: 
# E(T) = sum( depth(node[i]) + 1) * p[i] + sum(depth(leaf[i]) + 1) * q[i]
# where p and q are the probability distribution for nodes and leaves
# 
# An optimal binary search tree is not necessarily a tree whose 
# overall height is smallest

def pretty_print(e):
	res = []
	for ee in e:
		my = [ '%.2f' % elem for elem in ee ]
		res.append(my)
	for ee in res:
		print(ee)
	print()

def optimal_bst(p, q):
	n = len(p)
	e = [[0] * (n+1) for _ in range(n+1)]
	w = [[0] * (n+1) for _ in range(n+1)]
	root = [[0] * n for i in range(n)]

	for i in range(n+1):
		e[i][i] = q[i]
		w[i][i] = q[i]

	for l in range(1, n + 1):
		for i in range(n - l + 1):
			j = i + l
			e[i][j] = inf
			w[i][j] = w[i][j-1] + p[j-1] + q[j]
			for r in range(i, j):
				t = e[i][r] + e[r+1][j] + w[i][j]
				if t < e[i][j]:
					e[i][j] = t
					root[i][j-1] = r + 1

	print("The expected search table: ")
	pretty_print(e)
	print("The sum of probabilities: ")
	pretty_print(w)
	print("The root table: ")
	pretty_print(root)
	print(construct_bst(root, 0, n - 1), "is the root")


def construct_bst(root, i, j):
	n = len(root)
	parent = "k" + str(root[i][j])

	l, r = i, root[i][j] - 2
	if r >= 0 and root[l][r] != 0:
		left = construct_bst(root, l, r)
		print(left, "is the left child of", parent)

	l, r = root[i][j], j
	if l < n and root[l][r] != 0:
		right = construct_bst(root, l, r)
		print(right, "is the right child of", parent)

	return parent


p = [0.15, 0.10, 0.05, 0.10, 0.20]
q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
optimal_bst(p, q)
