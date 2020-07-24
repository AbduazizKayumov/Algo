class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right


# The leftmost node is the minimum
def minimum(node):
    while node.left:
        node = node.left
    return node


# The rightmost node is the max
def maximum(node):
    while node.right:
        node = node.right
    return node
