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


# If the left subtree is not empty -> return the rightmost node in the left subtree
# Otherwise, return the first leftmost ancestor
def predecessor(node):
    if node.left:
        return maximum(node.left)
    parent = node.parent
    while parent and node == parent.left:
        node = parent
        parent = node.parent
    return parent
