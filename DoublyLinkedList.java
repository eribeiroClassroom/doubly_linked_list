public class DoublyLinkedList {

    private Node head; // head sentinel
    private Node tail; // tail sentinel

    public DoublyLinkedList() {
        head = new Node(0); // dummy value
        tail = new Node(0); // dummy value
        head.next = tail;
        tail.prev = head;
    }

    // Adds a node with given value to the end of the list
    public void addNode(int value) {
        Node newNode = new Node(value);
        Node last = tail.prev;

        last.next = newNode;
        newNode.prev = last;
        newNode.next = tail;
        tail.prev = newNode;
    }

    // Print list 
    public void printList() {
        Node current = head.next;
        while (current != tail) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

}


