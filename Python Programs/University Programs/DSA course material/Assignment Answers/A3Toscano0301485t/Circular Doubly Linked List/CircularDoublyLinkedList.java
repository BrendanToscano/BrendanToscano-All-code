/*
 * Course: COMP 2113 FA01, 2023
 * Assignment 3, Question 2b
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-08-08
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.
*/

/*
What does the program do?
The Circular doubly Linkedlist class does 4 things add, remove , traverse and traverseBackward from any position.
The add will take in a position and a number and add it to the linked list.
The remove will take in a position and remove it from the linked list.
The traverse will print all numbers from position till the starting position.
The traverseBackward will print all numbers from position backwards till position.

Linked list:-
The difference between this and a linked list is that in a linked list we have the head pointing to the
head node which points to the second node and so on, it continues till the end of the linked list and the last
point on the tail will be Null.

Doubly linked list:-
The doubly linkedlist have 2 pointers in both directions on each node.
In a doubly linkedlist the head/first node points to the second node and the second
node point back to the first node, the second node points to the third node and the third node
points to the second node and so on.

Circular doubly linked list:-
In a circular doubly linkedlist the head points to the tail and the tail points to
the head the rest is the same as a doubly linkedlist.
Error checks have been implemented. All error checks are mentioned below. Most are same as the linkedlist ones.
*/

/*
Most error checks are same as linkedlist.
Had to add one final error check before the do loop in add to check if head is null.
Changed some error checks traverse and traverseBackward to work similar to the others in remove and add.
*/

public class CircularDoublyLinkedList {
    // Creating the head
    Node head;

    // Add will take in the position and number and add it to the linked list.
    public void add(int position, int number) {
        // Creating a new node.
        Node node = new Node();
        node.data = number;
        node.next = null;
        node.prev = null;

        // Checking if user entered position 0 and setting a new head
        if (position == 0) {
            // Creating the first head.
            if (head == null) {
                node.next = node;
                node.prev = node;
                head = node;
            }
            // All other heads.
            else {
                node.prev = head.prev;
                node.next = head;
                head.prev.next = node;
                head.prev = node;
                head = node;
            }
        } else {
            // Setting the start of the traverse node
            Node traverseNode = head;
            // Setting last position to 0 will be incremented till last value
            int lastPosition = 0;
            // Checking for tail
            if(head != null) {
                do {
                    // incrementing till tail.
                    traverseNode = traverseNode.next;
                    lastPosition++;
                } while (traverseNode != head && lastPosition < position);
            }
            // Using last position value to check if entered position is in range
            if (position > lastPosition || position < 0) {
                System.out.println("The given position is out of range");
            }
            else {
                // Resetting the traverseNode to head and incrementing till the node before the position node.
                traverseNode = head;
                for (int i = 0; i < position - 1; i++) {
                    traverseNode = traverseNode.next;
                }

                // Adding the node
                node.prev = traverseNode;
                node.next = traverseNode.next;
                traverseNode.next.prev = node;
                traverseNode.next = node;

            }
        }
    }

    // Removes node from position
    public void remove(int position) {
        // Checking if list is empty
        if (head == null) {
            System.out.println("Linked list is empty");
        } else {
            // Setting the start of the traverse node
            Node traverseNode = head;
            // Setting last position to 0 will be incremented till last value
            int lastPosition = 0;
            // Checking for tail
            while (traverseNode != head.prev) {
                // incrementing till tail.
                traverseNode = traverseNode.next;
                lastPosition++;
            }
            // Checking if the position is in range.
            if (position > lastPosition || position < 0) {
                System.out.println("The given position is out of range");
            }
            // Checking if head is being removed.
            else if (position == 0) {
                head = head.next;
                head.prev = traverseNode;
                traverseNode.next = head;
            } else {
                // Resetting traverseNode to head and getting the node before the position node.
                traverseNode = head;
                for (int i = 0; i < position - 1; i++) {
                    traverseNode = traverseNode.next;
                }
                // Removing the node.
                Node traverseNode1 = traverseNode.next;
                traverseNode.next = traverseNode1.next;
                traverseNode1.next.prev = traverseNode;
            }
        }
    }

    // Traverse will display the list from user requested position.
    public void traverse(int position) {
        // Checking if list is empty.
        if (head == null) {
            System.out.println("Linked list is empty");
        } else {
            // Setting the start of the traverse node
            Node traverseNode = head;
            // Setting last position to 0 will be incremented till last value
            int lastPosition = 0;
            // Checking for tail
            while (traverseNode != head.prev) {
                // incrementing till tail.
                traverseNode = traverseNode.next;
                lastPosition++;
            }
            // If in range.
            if (lastPosition >= position && position >= 0) {
                // Checking for tail
                traverseNode = head;
                // Incrementing traverseNode to position.
                for (int i = 0; i < position; i++) {
                    traverseNode = traverseNode.next;
                }
                Node traverseNode_check = traverseNode;
                // Displaying everything after position.
                do {
                    System.out.println(traverseNode.data);
                    traverseNode = traverseNode.next;
                } while (traverseNode != traverseNode_check);
            }
            // If not in range.
            else {
                System.out.println("The position entered is not valid");
            }
        }
    }

    public void traverseBackward(int position) {
        // Checking if list is empty.
        if (head == null) {
            System.out.println("Linked list is empty");
        } else {
            // Setting the start of the traverse node
            Node traverseNode = head;
            // Setting last position to 0 will be incremented till last value
            int lastPosition = 0;
            // Checking for tail
            while (traverseNode != head.prev) {
                // incrementing till tail.
                traverseNode = traverseNode.next;
                lastPosition++;
            }
            // If in range.
            if (lastPosition < position || position < 0) {
                System.out.println("The position is out of range");
            }
            // If not in range.
            else {
                // Checking for tail
                traverseNode = head;
                // Incrementing traverseNode to position.
                for (int i = 0; i < position; i++) {
                    traverseNode = traverseNode.next;
                }
                Node traverseNode_check = traverseNode;
                // Displaying everything after position.
                do {
                    System.out.println(traverseNode.data);
                    traverseNode = traverseNode.prev;
                } while (traverseNode != traverseNode_check);
            }
        }
    }
    // End of required code.

    // This code is for debugging purposes and was not required by the question
    // Keeping in-case required, won't affect the rest of the program in any way.
    // Basically does the same thing as Traversing through the list but from position 0.

    public void show(){
        Node traverseNode = head;
        if(traverseNode == null) {
            System.out.println("Linked list is empty");
        }
        else {
            // Checking for tail
            while (traverseNode != head.prev) {
                // Printing node
                System.out.println(traverseNode.data);
                // Going to the next node
                traverseNode = traverseNode.next;
            }
            System.out.println(traverseNode.data);

        }
    }
}


