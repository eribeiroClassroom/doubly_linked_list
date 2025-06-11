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

In this assignment you will implement the functions discussed in our previous classroom practice. You can implement the assignment in either Python or Java. You must write the code by yourself. You are free to use any help on syntax but you must try to figure our the logic solution on your own. It is fine with exchange ideas with colleagues but not copying code or generating code from anywhere. 

1. (25 pts) Implement the functions discussed in class during the classroom practice session, i.e.: 

```
Node find(int data)
bool remove_node(int data)
void add_node_after(int data, int new data)
void remove_this_node(Node current)
```
The above function signatures are suggestions. Make all changes you find necessary to implement the correct solution. 

2. (25 pts) Implement the setter and getter functions in the Node class to control access to the member variables. The functions you are expected to implement are: 

```
Node get_previous()
Node get_next()
void set_next(Node the_node)
void set_previous(Node the_node)
```

3. (25 pts) Modify/extend all functions so that they use the getter and setter functions correctly. See the following example of using these functions:

```Java
Current.getPrevious().setNext(current.getNext())   // instead of (Current.prev).next = current.next
Current.getNext().setPrevious(current.getPrevious())   // instead of (Current.next).prev = current.prev
```

4. (25 pts) Finally, test your program using the sequence `10, 20, 30, 40, 50, 60, 70, 80, 90, 100`, which you can hardcode. In your main program, you should provide calls to demonstrate (test) each function in Item 1 on this list of tasks. You  must also add a screenshot of your program's execution to this README.md file.

## Screenshots of program execution

Screenshots go here ... 
