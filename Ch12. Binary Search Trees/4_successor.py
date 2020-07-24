class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


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


# If the right subtree is not empty -> return the leftmost node in the right subtree
# Otherwise, return the first rightmost ancestor
def successor(node):
    if node.right:
        return minimum(node.right)
    parent = node.parent
    while parent and node == parent.right:
        node = parent
        parent = node.parent
    return parent
