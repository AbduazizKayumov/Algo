from math import inf
# The Huffman code - an optimal prefix code to compress data 
#					 very efficiently, savings of 20% ~ 90%
# 
# Let's consider the problem of designing a binary char code,
# in which each char is represented bu a unique binary string.
#
# If we use a fixed-length code, we need 3 bits to represent 
# 6 characters: a == 000, b = 001, ... , f = 101. This method
# requires to code the entire file.
#
# A variable-length code can do better than a fixed-length code,
# by giving frequent chars short codewords and infrequent chars
# long codewords. 
#
# 					  a     b     c     d     e     f 
# -----------------------------------------------------
# Frequency		  |  45	   13    12    16     9     5 |   
# fixed-length    | 000   001   010   011   100   101 |   300,000 bits
# Variable-length |  0    101   100   111  1101  1100 |   224,000 bits  => 25% better
# 
#
# An optimal code for a file is always represented by a full binary tree.
# The number of bits required to encode a gile is: cost = sum(depth(c) * c.freq) for node c
#
#
# Huffman invented a greedy algorithm that constructs an optimal prefix code called a 
# Huffman code.
#
#
#          100
#    	 /     \
#      a:45    55
#            /    \
#		    25     30
#         /   \    /  \
#       c:12 b:13 14  d:16
#				 /  \
#			   f:5  e:9
# 
# Codewords can be obtained by walking through from root to leaves: codeword += '1' if walks right, '0' otherwise

class Node:
	def __init__(self):
		self.character = None
		self.left = None
		self.right = None
		self.freq = 0

def extract_min(Q):
	mn, inx = Q[0].freq, 0
	for i in range(len(Q)):
		if Q[i].freq < mn:
			mn = Q[i].freq
			inx = i
	x = Q.pop(inx)
	return x


# C is a list of nodes
def huffman(C):
	n = len(C)
	Q = C.copy() # can be min-priority queue
	for i in range(n-1):
		z = Node()
		x, y = extract_min(Q), extract_min(Q)
		z.left = x
		z.right = y
		z.freq = x.freq + y.freq
		Q.append(z)
	return extract_min(Q)

def print_codewords(node, path = ""):
	if not node:
		return

	if node.character is not None:
		print(node.character, path)
		return

	print_codewords(node.left, path + "0")
	print_codewords(node.right, path + "1")



chars = ['a','b', 'c', 'd', 'e', 'f']
freqs = [ 45, 13,  12,  16,   9,   5]
C = []
for i in range(len(chars)):
	node = Node()
	node.character = chars[i]
	node.freq = freqs[i]
	C.append(node)


root = huffman(C)
print_codewords(root)
