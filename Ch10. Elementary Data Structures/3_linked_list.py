# A linked list is a data structure that arranges its elements in a linear order
# It can be singular or doubly linked list.
# The first element is called "head" and the last one is "tail"
# If the last element is connected to the head element, then it is called "circular"


class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        # create new node
        node = ListNode(val)

        # connect it to tail
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def search(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return cur
        return None

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev

