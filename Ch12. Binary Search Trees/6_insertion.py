class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_tree_walk(node):
    if node:
        inorder_tree_walk(node.left)
        print(node.val)
        inorder_tree_walk(node.right)


def insert(root, x):
    if not root:
        return Node(x)

    if x < root.val:
        if root.left:
            return insert(root.left, x)
        else:
            root.left = Node(x)
            return root.left
    else:
        if root.right:
            return insert(root.right, x)
        else:
            root.right = Node(x)
            return root.right


arr = [5, 1, 10, -1, 2, 7, 11]
root = Node(6)

for a in arr:
    insert(root, a)

inorder_tree_walk(root)
