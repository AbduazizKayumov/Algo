def binary_search(x, A):
    l = -1
    r = len(A)
    while r - l > 1:
        mid = (r + l) >> 1
        if A[mid] == x:
            return mid
        if A[mid] > x:
            r = mid
        else:
            l = mid
    return -1


class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if key >= current.key:
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


arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]
res = binary_search(6, arr)
print(res)

arr = [5, 1, 10, -1, 2, 7, 11]
bst = BinarySearchTree()
for a in arr:
    bst.insert(a)

visited = set()
queue = [bst.root]
while queue:
    node = queue.pop(0)
    if node not in visited:
        visited.add(node)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

for v in visited:
    print(v.key)
