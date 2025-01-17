/*
 * Course: COMP 2113 FA01, 2023
 * Assignment 4, Question 1
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-10-16
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.
*/
public class Main {
    public static void main(String[] args) {
        BinarySearchTree bst1 = new BinarySearchTree();

        bst1.insertValue(10);
        bst1.insertValue(5);
        bst1.insertValue(15);
        bst1.insertValue(4);
        bst1.insertValue(16);
        bst1.insertValue(6);
        bst1.insertValue(14);
        bst1.insertValue(30);
        bst1.insertValue(5);
        bst1.insertValue(0);

        bst1.depthTraverse();

        bst1.breadthTraverse();

        // Finding size from root
        bst1.size(bst1.root);
        bst1.size(bst1.getNode(0));

        // Finding depth from the last position of the tree
        bst1.depth(bst1.getNode(9));

    }
}