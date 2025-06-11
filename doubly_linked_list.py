from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0)  # head sentinel
        self.tail = Node(0)  # tail sentinel
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, value):
        new_node = Node(value)
        last = self.tail.prev

        last.next = new_node
        new_node.prev = last
        new_node.next = self.tail
        self.tail.prev = new_node

    def print_list(self):
        current = self.head.next
        while current != self.tail:
            print(current.data, end=' ')
            current = current.next
        print()
