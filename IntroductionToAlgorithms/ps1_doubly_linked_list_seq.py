class DoublyLinkedList:
    class Node:
        def __init__(self, item=None, prev=None, next=None):
            self.item = item
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_first(self, x):
        new_node = self.Node(x)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, x):
        new_node = self.Node(x)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        x = self.head.item
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return x

    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        x = self.tail.item
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return x

    def remove(self, x1, x2):
        L2 = DoublyLinkedList()
        L2.head = x1
        L2.tail = x2
        if x1 == self.head:
            self.head = x2.next
        else:
            x1.prev.next = x2.next
        if x2 == self.tail:
            self.tail = x1.prev
        else:
            x2.next.prev = x1.prev
        x1.prev = None
        x2.next = None
        return L2

    def splice(self, x, L2):
        xn = x.next
        x1 = L2.head
        x2 = L2.tail
        x1.prev = x
        x.next = x1
        x2.next = xn
        if xn:
            xn.prev = x2
        else:
            self.tail = x2

dll = DoublyLinkedList()
dll.insert_first(1)
dll.insert_last(2)
dll.insert_last(3)
assert dll.delete_first() == 1
assert dll.delete_last() == 3
dll.insert_first(0)
dll.insert_last(4)
L2 = dll.remove(dll.head.next, dll.tail.prev)
assert dll.head.item == 0
assert dll.tail.item == 4
assert L2.head.item == 2
assert L2.tail.item == 2
dll.splice(dll.head.next, L2)
assert dll.head.item == 0
assert dll.head.next.item == 2
assert dll.head.next.next.item == 4
assert dll.tail.item == 4