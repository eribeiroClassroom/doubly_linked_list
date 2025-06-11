from doubly_linked_list import DoublyLinkedList

def main():
    dll = DoublyLinkedList()
    dll.add_node(10)
    dll.add_node(20)
    dll.add_node(30)

    print("List contents:", end=' ')
    dll.print_list()  # Output: 10 20 30

if __name__ == '__main__':
    main()


