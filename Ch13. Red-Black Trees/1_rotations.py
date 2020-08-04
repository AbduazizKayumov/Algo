class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def print_tree(root):
    if not root:
        return
    levels = []
    d = {root: 0}
    q = [root]
    while q:
        cur = q.pop()
        depth = d[cur]
        if depth >= len(levels):
            levels.append([])
        levels[depth].append(cur.val)

        if cur.right:
            d[cur.right] = depth + 1
            q.append(cur.right)

        if cur.left:
            d[cur.left] = depth + 1
            q.append(cur.left)

    for i in range(len(levels)):
        print("Level ", str(i), ": ", *levels[i])


# Rotation is a local operation in Red-black tree that preserves the BST property.
# Any node x can be left or right rotated
# LEFT-ROTATION(x) rotates x with its right node
#     y                                       x
#    / \                                     / \
#   x   c    <-----left-rotation-----       a   y
#  / \                                         / \
# a  b                                        b  c
def left_rotate(x):
    root = x
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent is None:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y

    return root


# RIGHT-ROTATION(y) rotates y with its left node
#     y                                       x
#    / \                                     / \
#   x   c    -----right-rotation----->      a   y
#  / \                                         / \
# a  b                                        b  c
def right_rotate(y):
    root = y
    x = y.left
    y.left = x.right
    if x.right is not None:
        x.right.parent = y
    x.parent = y.parent
    if y.parent is None:
        root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    x.right = y
    y.parent = x

    return root


a = Node(5)
x = Node(12)
a.parent = x
x.left = a

y = Node(20)
y.parent = x
x.right = y

b = Node(18)
c = Node(25)

b.parent = y
y.left = b
c.parent = y
y.right = c

print("Before left-rotate(x):")
print_tree(x)
root = left_rotate(x)
print("After left-rotate(x):")
print_tree(root)

print()
print("Before right-rotate(y):")
print_tree(root)
root = right_rotate(root)
print("After right-rotate(x):")
print_tree(root)
