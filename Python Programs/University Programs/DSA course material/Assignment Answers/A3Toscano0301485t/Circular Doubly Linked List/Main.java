/*
 * Course: COMP 2113 FA01, 2023
 * Assignment 3, Question 2c
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-08-08
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.
*/

/*
This is where the program will run. Different test cases are included in the code.
*/
public class Main {

    public static void main(String[] args) {

        CircularDoublyLinkedList list = new CircularDoublyLinkedList();

        // Checking what happens when the list is empty.
        System.out.println("Should tell user linked list is Empty ");
        list.remove(0);
        list.traverse(0);
        list.traverseBackward(0);

        System.out.println("");

        // When out of range position is entered while list is empty.
        System.out.println("Should tell user linked list is empty or out of range for add");
        list.traverse(1);
        list.traverseBackward(1);
        list.add(1, 1);
        list.remove(1);

        System.out.println("");

        // Adding elements
        list.add(0, 5);
        System.out.println("Should be 5");
        list.traverse(0);
        System.out.println("Should be 5");
        list.traverseBackward(0);

        System.out.println("");

        list.add(0, 1);
        System.out.println("Should be 1,5");
        list.traverse(0);
        System.out.println("Should be 1,5");
        list.traverseBackward(0);

        System.out.println("");

        list.add(1, 3);
        System.out.println("Should be 1,3,5");
        list.traverse(0);
        System.out.println("Should be 1,5,3");
        list.traverseBackward(0);

        System.out.println("");

        list.add(1, 2);
        System.out.println("Should be 1,2,3,5");
        list.traverse(0);
        System.out.println("Should be 1,5,3,2");
        list.traverseBackward(0);

        System.out.println("");

        list.add(3,4);
        System.out.println("Should be 1,2,3,4,5");
        list.traverse(0);
        System.out.println("Should be 1,5,4,3,2");
        list.traverseBackward(0);

        System.out.println("");

        // Testing traverse
        System.out.println("Should traverse from position 2 (3,4,5,1,2)");
        list.traverse(2);
        System.out.println("Should traverse from position 2 (3,2,1,5,4)");
        list.traverseBackward(2);

        System.out.println("");

        System.out.println("Should traverse from position 2 (5,1,2,3,4)");
        list.traverse(4);
        System.out.println("Should traverse from position 2 (5,4,3,2,1)");
        list.traverseBackward(4);

        System.out.println("");

        // Checking what happens when out of range position is entered while list has elements
        System.out.println("Should tell user out of range error");
        list.add(14, 1);
        list.traverse(-1);
        list.traverse(14);
        list.traverseBackward(-1);
        list.traverseBackward(14);
        list.remove(14);

        System.out.println("");

        // Testing removing
        System.out.println("Should give 1,2,4,5");
        list.remove(2);
        list.traverse(0);
        System.out.println("Should give 2,4,5");
        list.remove(0);
        list.traverse(0);
        System.out.println("Should give 2,5");
        list.remove(1);
        list.traverse(0);
        System.out.println("Should give 2");
        list.remove(1);
        list.traverse(0);

    }
}