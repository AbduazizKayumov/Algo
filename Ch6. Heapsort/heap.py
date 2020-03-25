def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def parent(i):
    return i // 2


# Max heapify i'th node from heap tree:
# 1) Take two child nodes: left and right
# 2) Compare left and right with their parent node
# 3) If the parent node is less than from left or right nodes,
#    replace the parent node with the largest one
#    3.1) Do max heapify for the replaced child node (left or right)
def max_heapify(A, i):
    l = left(i)
    r = right(i)
    largest = i
    if l <= len(A) and A[l - 1] > A[largest - 1]:
        largest = l
    if r <= len(A) and A[r - 1] > A[largest - 1]:
        largest = r

    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        max_heapify(A, largest)


# Build max heap:
# Do max_heapify for all nodes starting from n / 2 to 1,
# Nodes at n / 2 .. n are leaves, no need to max heapify
def build_max_heap(A):
    n = len(A)
    for i in range(n // 2, 0, -1):
        max_heapify(A, i)
    return A


# Heap sort:
# 1) Build heap tree from the input array
# 2) Find the max element (always the root node!)
# 3) Replace the root node(max) with the last node
# 4) Now the max element is at the end of the array, discard the last node from heap tree
# 5) The root node may violate max heap property, do max_heapify for node 1
# 6) Keep doing 2nd, 3rd, 4th and 5th until the heap tree is empty
def heap_sort(A):
    answer = []
    A = build_max_heap(A)
    while A:
        A[0], A[-1] = A[-1], A[0]
        answer.append(A.pop())
        max_heapify(A, 1)
    return answer


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(arr)
res = heap_sort(arr)
print(res)

arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print(arr)
res = heap_sort(arr)
print(res)
