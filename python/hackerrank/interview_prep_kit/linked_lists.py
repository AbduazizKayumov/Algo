# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtPosition(head, data, position):
    current = head
    i = 1
    while current.next != None:
        current = current.next
        i += 1
        if i == position:
            break
    new_node = SinglyLinkedListNode(data)
    new_node.next = current.next
    current.next = new_node
    return head
# ------------------------------------------------------



# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def reverse(head):
    current = head
    while current != None:
        nextt = current.next
        if nextt == None:
            head = current
        current.next = current.prev
        current.prev = nextt
        current = current.prev
    return head
# ------------------------------------------------------





# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    if head.data >= data:
        new_node.next = head
        new_node.prev = head.prev
        head.prev = new_node
        return new_node
    current = head
    while current.next:
        if current.next.data > data:
            break
        current = current.next
    print(str(current.data))
    new_node.prev = current
    new_node.next = current.next
    current.next = new_node
    return head
# ------------------------------------------------------


