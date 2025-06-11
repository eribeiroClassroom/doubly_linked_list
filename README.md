# doubly_linked_list
Implementing some functions of a doubly linked list

## Java starter code

```css
DoublyLinkedListDemo/
├── Node.java
├── DoublyLinkedList.java
└── Main.java

```

## Python starter code

```css
doubly_linked_list/
├── node.py
├── doubly_linked_list.py
└── main.py
```


## Assignment description

1. Implement the functions discussed in class during the classroom practice session, i.e.: 

```
Node find(int data)
bool remove_node(int data)
void add_node_after(int data, int new data)
void remove_this_node(Node current)
```
The above function signatures are suggestions. Make all changes you find necessary to implement the correct solution. 

2. Implement the setter and getter functions in the Node class to control access to the member variables. The functions you are expected to implement are: 

```
Node get_previous()
Node get_next()
void set_next(Node the_node)
void set_previous(Node the_node)
```

3. Modify/extend all functions so that they use the getter and setter functions correctly. See the following example of using these functions:

```Java
Current.getPrevious().setNext(current.getNext())   // instead of (Current.prev).next = current.next
Current.getNext().setPrevious(current.getPrevious())   // instead of (Current.next).prev = current.prev
```
