class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right


# Print left subtree
# Print the root
# Print right subtree
def inorder_tree_walk(node):
    if node:
        inorder_tree_walk(node.left)
        print(node.val)
        inorder_tree_walk(node.right)
