# AVL vs Red-Black tree:
# - AVL provides faster lookups (AVL is more strictly balanced)
# - Red-Black tree provides faster insertion & removal
# - AVL stores heights for each node whereas Red-Black tree only stores one bit(color) for each node
# - Red-Black tree is used to implement map, multimap, multiset, AVL is used in databases (for faster lookups)

BLACK = "B"
RED = "R"


class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.color = BLACK

# Properties of Red-black trees
# 1. Every node is either red or black
# 2. The root is black
# 3. Every leaf(NIL) is black
# 4. If a node is red, then its both children are black
# 5. For each node, all simple paths from the node to descendant leaves contains the same number of black nodes
class RBTree:
    def __init__(self):
        self.nil = Node(0)
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.root = self.nil

    # Rotation is a local operation in Red-black tree that preserves the BST property.
    # Any node x can be left or right rotated
    # LEFT-ROTATION(x) rotates x with its right node
    #     y                                       x
    #    / \                                     / \
    #   x   c    <-----left-rotation-----       a   y
    #  / \                                         / \
    # a  b                                        b  c
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    # RIGHT-ROTATION(y) rotates y with its left node
    #     y                                       x
    #    / \                                     / \
    #   x   c    -----right-rotation----->      a   y
    #  / \                                         / \
    # a  b                                        b  c
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def insert(self, key):
        z = Node(key)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z

        z.left = self.nil
        z.right = self.nil
        z.color = RED
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.left_rotate(z.parent.parent)
        self.root.color = BLACK


def print_tree(root):
    levels = []
    d = {root: 0}
    q = [root]
    while q:
        cur = q.pop()
        depth = d[cur]

        if depth >= len(levels):
            levels.append([])

        levels[depth].append(str(cur.val) + "(" + str(cur.color) + ")")

        if cur.right.val != 0:
            d[cur.right] = depth + 1
            q.append(cur.right)

        if cur.left.val != 0:
            d[cur.left] = depth + 1
            q.append(cur.left)

    for i in range(len(levels)):
        print("Level ", str(i), ": ", *levels[i])


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
tree = RBTree()
for a in arr:
    tree.insert(a)

print_tree(tree.root)
