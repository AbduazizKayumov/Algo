# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))


# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem
def lca(root, v1, v2):
    # find v1 or v2 using binary search
    if v1 <= root.info and v2 >= root.info:
        return root
    if v2 <= root.info and v1 >= root.info:
        return root
    if v1 <= root.info and v2 <= root.info:
        return lca(root.left, v1, v2)
    return lca(root.right, v1, v2)


# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
def checkBST(root, min=-1, max=10001):
    if root is None:
        return True
    if root.left is not None and root.left.data >= root.data:
        return False
    if root.right is not None and root.right.data <= root.data:
        return False
    if root.data <= min or root.data >= max:
        return False
    return checkBST(root.left, min, root.data) and checkBST(root.right, root.data, max)


# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    current = root
    answer = ""
    for i in range(len(s)):
        if s[i] == '1':
            current = current.right
        else:
            current = current.left
        if current.left is None and current.right is None:
            answer += current.data
            current = root

    print(answer)
