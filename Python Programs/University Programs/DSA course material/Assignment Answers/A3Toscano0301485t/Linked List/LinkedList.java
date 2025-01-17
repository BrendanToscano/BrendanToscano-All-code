/*
 * Course: COMP 2113 FA01, 2023
 * Assignment 3, Question 1b
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-08-08
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.
*/

/*
What does the program do?
The Linkedlist class does 3 things add, remove and traverse from any position.
The add will take in a position and a number and add it to the linked list.
The remove will take in a position and remove it from the linked list.
The traverse will print all numbers from position till the end of the list.
Error checks have been implemented. All error checks are mentioned below.
*/

/*
Error checks:-
In most of the code error checking has been implemented.
In add:-
- It will check if user entered posiion 0 and will set it to the head.
- Using the last postion we can check if a negative number or a number greater than the last position was entered.
In remove:-
- We check if the linked list is empty by checking if the head is empty.
- Like in add we check for out of range postions.
- In remove we also check if the head is being removed. We reassign the head to the next node.
In traversal:-
- We check if the linked list is empty like in remove.
- We check if the lastposition is greater than or equal to position and if a negative position is entered.
 */
public class LinkedList {
    // Creating the head
    Node head;
    // Add will take in the position and number and add it to the linked list.
    public void add(int position, int number){
        // Creating a new node.
        Node node = new Node();
        node.data = number;
        node.next = null;

        // Checking if user entered position 0 and setting a new head
        if(position == 0){
            node.next = head;
            head = node;
        }
        else{
            // Setting the start of the traverse node
            Node traverseNode = head;
            // Setting last position to 0 will be incremented till last value
            int lastPosition = 0;
            // Checking for tail
            while(traverseNode != null){
                // incrementing till tail.
                traverseNode = traverseNode.next;
                lastPosition++;
            }
            // Using last position value to check if entered position is in range
            if(position > lastPosition || position < 0){
                System.out.println("The given position is out of range");
            }
            else{
                // Resetting the traverseNode to head and incrementing till the node before the position node.
                traverseNode = head;
                for (int i = 0; i < position - 1; i++) {
                    traverseNode = traverseNode.next;
                }
                // Adding the node
                node.next = traverseNode.next;
                traverseNode.next = node;
            }
        }

    }
    // Removes node from position
    public void remove(int position){
        // Checking if list is empty
        if(head == null){
            System.out.println("Linked list is empty");
        }
        else {
            // Setting the start of the traverse node
            Node traverseNode = head;
            // Setting last position to 0 will be incremented till last value
            int lastPosition = 0;
            // Checking for tail
            while (traverseNode != null) {
                // incrementing till tail.
                traverseNode = traverseNode.next;
                lastPosition++;
            }
            // Checking if the position is in range.
            if(position > lastPosition || position < 0){
                System.out.println("The given position is out of range");
            }
            // Checking if head is being removed.
            else if(position == 0){
               head = head.next;
            }
            else{
                // Reseeting traverseNode to head and getting the node before the position node.
                traverseNode = head;
                for (int i = 0; i < position - 1; i++) {
                    traverseNode = traverseNode.next;
                }
                // Removing the node.
                Node traverseNode1 = traverseNode.next;
                traverseNode.next = traverseNode1.next;
            }
        }
    }
    // Traverse will display the list from user requested position.
    public void traverse(int position) {
        // Checking if list is empty.
        if (head == null) {
            System.out.println("Linked list is empty");
        }
        else {
            // Setting the start of the traverse node
            Node traverseNode = head;
            // Setting last position to 0 will be incremented till last value
            int lastPosition = 0;
            // Checking for tail
            while(traverseNode != null){
                // incrementing till tail.
                traverseNode = traverseNode.next;
                lastPosition++;
            }
            // If in range.
            if(lastPosition >= position && position >= 0){
                // Checking for tail
                 traverseNode = head;
                 // Incrementing traverseNode to position.
                for (int i = 0; i < position ; i++) {
                    traverseNode = traverseNode.next;
                }
                // Displaying everything after position.
                while(traverseNode != null) {
                    System.out.println(traverseNode.data);
                    traverseNode = traverseNode.next;
                }
            }
            // If not in range.
            else{
                System.out.println("The position entered is not valid");
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
            while (traverseNode != null) {
                // Printing node
                System.out.println(traverseNode.data);
                // Going to the next node
                traverseNode = traverseNode.next;
            }
        }
    }
}




