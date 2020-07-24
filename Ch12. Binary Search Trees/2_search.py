class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right


# Return if the search key equals to current node's value
# Search from left subtree if the search key is less
# Search from right subtree otherwise
def search(node, k):
    if not node or k == node.val:
        return node

    if k < node.val:
        return search(node.left, k)
    else:
        return search(node.right, k)


# Keep looking down until hit or null
def search_iterative(node, k):
    while node and node.val != k:
        if k < node.val:
            node = node.left
        else:
            node = node.right
    return node
