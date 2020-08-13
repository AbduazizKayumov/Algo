# The height h of a binary search tree is between logn and n
# The importance of being balanced BST
# is to keep the height of a tree as logn
# so that all operations (search, insert, delete, min, max, next-larger, next-smaller)
# take O(logn) time

# AVL Trees = Adelson-Velskii & Landis
# AVL property:
#       - each node stores its height
#       - for every node, require heights of left & right children to differ by at most 1
#
# AVL vs Red-Black tree:
# - AVL provides faster lookups (AVL is more strictly balanced)
# - Red-Black tree provides faster insertion & removal
# - AVL stores heights for each node whereas Red-Black tree only stores one bit(color) for each node
# - Red-Black tree is used to implement map, multimap, multiset, AVL is used in databases (for faster lookups)


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0


def height(node):
    if node is None:
        return -1
    return node.height


def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1


class AVLTree:
    def __init__(self):
        self.root = None

    def right_rotate(self, node):
        child = node.left
        child.parent = node.parent
        node.parent = child

        if child.parent is None:
            self.root = child
        else:
            if child.parent.left is node:
                child.parent.left = child
            elif child.parent.right is node:
                child.parent.right = child

        node.left = child.right
        if node.left is not None:
            node.left.parent = node
        child.right = node
        node.parent = child

        update_height(node)
        update_height(child)

    def left_rotate(self, node):
        child = node.right
        child.parent = node.parent
        node.parent = child

        if child.parent is None:
            self.root = child
        else:
            if child.parent.left is node:
                child.parent.left = child
            elif child.parent.right is node:
                child.parent.right = child

        node.right = child.left
        if node.right is not None:
            node.right.parent = node
        child.left = node
        node.parent = child

        update_height(node)
        update_height(child)

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = Node(key)
        else:
            current = self.root
            while True:
                if key == current.key:
                    print("Node already exists")
                    break
                if key > current.key:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
            new_node.parent = current

            current = new_node.parent
            while current:
                update_height(current)
                if height(current.left) >= height(current.right) + 2:
                    # left
                    if height(current.left.left) >= height(current.left.right):
                        # left
                        # left + left -> right rotate
                        self.right_rotate(current)
                    else:
                        # right
                        # left + right -> left rotate -> right rotate
                        self.left_rotate(current.left)
                        self.right_rotate(current)
                        pass
                elif height(current.left) + 2 <= height(current.right):
                    # right
                    if height(current.right.right) >= height(current.right.left):
                        # right
                        # right + right -> left rotate
                        self.left_rotate(current)
                    else:
                        # left
                        # right + left -> right rotate -> left rotate
                        self.right_rotate(current.right)
                        self.left_rotate(current)
                current = current.parent


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
tree = AVLTree()
for a in arr:
    tree.insert(a)

    visited = set()
    queue = [tree.root]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node.key)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    print()
