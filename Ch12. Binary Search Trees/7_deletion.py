class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


# The leftmost node is the minimum
def minimum(node):
    while node.left:
        node = node.left
    return node


def search(node, k):
    if not node or k == node.val:
        return node

    if k < node.val:
        return search(node.left, k)
    else:
        return search(node.right, k)


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
            root.left.parent = root
            return root.left
    else:
        if root.right:
            return insert(root.right, x)
        else:
            root.right = Node(x)
            root.right.parent = root
            return root.right


# Replace u with v
def transplant(u, v):
    if u.parent:
        if u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
    if v:
        v.parent = u.parent


# 3 cases of deleting a node z
# 1. Node z has no children -> simply remove parent's pointer to z
# 2. Node z has just one child -> exchange z with its child
# 3. Node z has two children:
#       Find z's successor y from z's right subtree
#       a) y is the right child of z -> simply replace z by y
#       b) y lies in within z's right subtree -> replace y by its own right child + replace z by y
def delete(z):
    if z.left is None:
        transplant(z, z.right)
        return z.right
    elif z.right is None:
        transplant(z, z.left)
        return z.left
    else:
        y = minimum(z.right)
        if y.parent != z:
            transplant(y, y.right)
            y.right = z.right
            y.right.parent = y
        transplant(z, y)
        y.left = z.left
        y.left.parent = y
    return y


arr = [5, 1, 10, -1, 2, 7, 11]
root = Node(6)

for a in arr:
    insert(root, a)
inorder_tree_walk(root)
print()

for a in arr:
    delete_me = search(root, a)
    delete(delete_me)
    inorder_tree_walk(root)
    print()
