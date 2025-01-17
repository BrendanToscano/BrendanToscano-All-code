/*
 * Course: COMP 2103 FA01, 2023
 * Assignment 8, Question 1
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-12-04
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.
*/
/*
 What does the program do?
 The program is an implemntation of a Circular Doubly linked list.
 It has has a menu with 7 options.
 Add node to the end of the list which calls the addNode function and adds the value to the the end of the list.
 Add node to postion whch calls the addNodePosition function and adds to the value to that position in the list.
 Delete node deletes the first node in the list
 Delete node position deletes the node at the user specified position of the list
 print list will print the linked list in order.
 print list reversed will print the linked list in reverse order.
 */
#include <stdio.h>
#include <stdlib.h>

// 22:08 - 22:08
// Creating the node typedef struct. Contains value, next pointer and prev pointer.
typedef struct node {
    int x;
    struct node *next;
    struct node *prev;
} NodeT, *NodeTP;

// 22:08 - 22:08
// Creating the node typedef struct. Contains the first node pointer and the total.
typedef struct {
    NodeTP first;
    int total;
} ListT, *ListTP;

// 22:18 - 22:54
// Adds node with value to the start of the CIrcular doubly linked list.
int addNodeToStart(ListTP this, int value){
    NodeTP node;
    
    if((node = malloc(sizeof(NodeT))) == NULL){
        printf("Error.\n");
        exit(EXIT_FAILURE);
    }
        
    // Checking if the list is empty.
    if (this->first == NULL){
        this->total = 0;
        // Setting the first pointer to the node
        this->first = node;
        // Setting value of node.
        node->x = value;
        // Setting the next and prev pointer to the node because it is a CDLL
        node->next = node;
        node->prev = node;
        this->total++;
    }
    else {
        // Setting prev pointer to the last node of the list.
        node->prev = this->first->prev;
        // Setting next pointer to the first node which in this case is the old first node of the list
        node->next = this->first;
        // Setting the value of the node.
        node->x = value;
        // Setting first node prev pointer to new node.
        this->first->prev = node;
        // Setting the next pointer of the last node to the new node.
        this->first->prev->next = node;
        // Setting the first pointer to the new node.
        this->first = node;
        this->total++;
    }
    return 1;
}

// 23:38 - 12:23
// Adds node with value to the end of the Circular doubly linked list.
int addNode(ListTP this, int value){
    NodeTP node, lastNode;
    
    if((node = malloc(sizeof(NodeT))) == NULL){
        printf("Error.\n");
        exit(EXIT_FAILURE);
    }
    
    // If the list is empty we call the addtostart fucntion
    if (this->first == NULL){
        addNodeToStart(this, value);
        return 1;
    }
    else{
        // Getting last node
        lastNode = this->first->prev;
        // Setting node value
        node->x = value;
        // Setting the next pointer of the node to point to the first node since it is a CDLL
        node->next = this->first;
        // Setting the prev pointer to point to the old lastnode.
        node->prev = lastNode;
        // Setting the old lastnode pointer to the new lastnode.
        lastNode->next = node;
        // Setting the first node prev pointer to the lastnode.
        this->first->prev = node;
        this->total++;
        return 1;
    }
}

// 1:32 - 2:18
// Adds node with value to the specified postion of the Circular doubly linked list.
int addNodePosition(ListTP this, int value, int position){
    NodeTP aux, node;
    int count = 0;
    
    if((aux = malloc(sizeof(NodeT))) == NULL){
        printf("Error.\n");
        exit(EXIT_FAILURE);
    }
    if((node = malloc(sizeof(NodeT))) == NULL){
        printf("Error.\n");
        exit(EXIT_FAILURE);
    }
    
    // If the postion is greater than the total number addded then the index is out of range. Also if negative.
    if (position > this->total || position < 0){
        printf("Position is out of range.\n");
        return 0;
    }
    // If the list is empty or position is 0 then calling addNodeToStart fucntion.
    else if (this->first == NULL || position == 0){
        addNodeToStart(this, value);
        return 1;
    }
    // If position is at the end then calling addNode.
    else if ((position + 1) == this->total){
        addNode(this, value);
        return 1;
    }
    else{
        // Till position is greater than count will keep incrementing
        for(aux->next = this->first; position > count; aux = aux->next){
            count++;
        }
        // Setting the value of the node.
        node->x = value;
        // Setting current node next ppinter to next node.
        node->next = aux->next;
        // Setting current node prev pointer to node.
        node->prev = aux;
        // setting the prev pointer of the next node to current node.
        aux->next->prev = node;
        // Settign the next pointer of the node to the current node.
        aux->next = node;
        this->total++;
        return 1;
    }
}

// Next day 14:38 - 15:12
// Deletes first occurance of value in the list.
int deleteNode(ListTP this, int value){
    NodeTP current;
    int count = 0;
    
    // Checking if list is empty.
    if (this->first == NULL){
        printf("The list is empty.\n");
        return 0;
    }
    // Loop till it finds the first occurance of the value.
    for (current = this->first; current->x != value; current = current->next){
        // Will run till the end of the list.
        if (count >= this->total){
            printf("Value not found.\n");
            return 0;
        }
        else{
            count++;
        }
    }
    // If the next is pointing to itself that means it is the only node so setting first pointer to null.
    if (current->next == current){
        this->first = NULL;
    }
    else{
        // Setting previous nodes next pointer to the next node of the current node.
        current->prev->next = current->next;
        // Setting next nodes prev pointer to the previous node of the current node.
        current->next->prev = current->prev;
        // Checking if current was the first node and setting the next node to the first node.
        if(current == this->first){
            this->first = current->next;
        }
    }
    free(current);
    this->total--;
    return 1;
}

// 15:12 - 16:25
// Deletes the node at the specified position.
int deleteNodePosition(ListTP this, int position){
    NodeTP current;
    int count = 0;
    
    // Checking if list is empty.
    if (this->first == NULL){
        printf("The list is empty.\n");
        return 0;
    }
    // If the postion is greater than the total number addded then the index is out of range. Also if negative.
    if (position >= this->total || position < 0){
        printf("Position is out of range.\n");
        return 0;
    }
    // Loop till count reaches position or till postion reaches total.
    for (current = this->first; count != position; current = current->next){
        if (count >= this->total){
            printf("Position not found.");
            return 0;
        }
        else{
            count++;
        }
    }
    // If the next is pointing to itself that means it is the only node so setting first pointer to null.
    if (current->next == current){
        this->first = NULL;
    }
    else{
        // Setting previous nodes next pointer to the next node of the current node.
        current->prev->next = current->next;
        // Setting next nodes prev pointer to the previous node of the current node.
        current->next->prev = current->prev;
        // Checking if current was the first node and setting the next node to the first node.
        if(current == this->first){
            this->first = current->next;
        }
    }
    free(current);
    this->total--;
    return 1;
}

// 22:08 - 22:14
// Prints Circular Doubly Linked List.
int printList(ListTP this){
    NodeTP node, current;
    int count = 0;
    
    // Check to see if the list is empty.
    if(this->first == NULL){
        printf("The list is empty.\n");
        return 0;
    }
    
    node = this->first;
    
    // Print all nodes from start to end.
    printf("The list is:\n");
    for (current = node; count < this->total; current = current->next){
        printf("%d\n", current->x);
        count++;
    }
    return 1;
    
}

// 22:08 - 22:18
// Prints the reverse of the Circular Doubly Linked List.
int printListReverse(ListTP this){
    NodeTP node, current;
    int count = 0;
    
    // Check to see if the list is empty.
    if(this->first == NULL){
        printf("The list is empty.\n");
        return 0;
    }
    
    node = this->first->prev;
    
    // Print all nodes from end to start
    printf("The reversed list is:\n");
    for (current = node; count < this->total; current = current->prev){
        printf("%d\n", current->x);
        count++;
    }
    return 1;
}

// 22:18 - 16:25
int main(void){
    char option;
    int value, position;
    ListT list1;
    list1.first = NULL;
    
    while(1){
        printf("a) Add Node to the end of the list.\n");
        printf("b) Add Node to specific position.\n");
        printf("c) Delete Node with specific value.\n");
        printf("d) Delete Node from specific position.\n");
        printf("e) Print Circular Doubly Linked list.\n");
        printf("f) Print reverse of Circular Doubly Linked list.\n");
        printf("g) Quit.\n");
        printf("Enter choice:- ");
        scanf(" %c", &option);
        
        if (option == 'a'){
            printf("Enter value you want to add to the end of the list:- ");
            if (scanf("%d", &value) != 1){
                printf("Invalid Input\n");
                exit(EXIT_FAILURE);
            }
            addNode(&list1, value);
        }
        else if(option == 'b'){
            printf("Enter value you want to add:- ");
            if (scanf("%d", &value) != 1){
                printf("Invalid Input\n");
                exit(EXIT_FAILURE);
            }
            printf("Enter position you want to add '%d' to:- ", value);
            if (scanf("%d", &position) != 1){
                printf("Invalid Input\n");
                exit(EXIT_FAILURE);
            }
            addNodePosition(&list1, value, position);
        }
        else if(option == 'c'){
            printf("Enter value you want to delete:- ");
            if (scanf("%d", &value) != 1){
                printf("Invalid Input\n");
                exit(EXIT_FAILURE);
            }
            deleteNode(&list1, value);
        }
        else if(option == 'd'){
            printf("Enter position you want to delete value from:- ");
            if (scanf("%d", &position) != 1){
                printf("Invalid Input\n");
                exit(EXIT_FAILURE);
            }
            deleteNodePosition(&list1, position);
        }
        else if(option == 'e'){
            printList(&list1);
        }
        else if(option == 'f'){
            printListReverse(&list1);
        }
        else if(option == 'g'){
            exit(EXIT_SUCCESS);
        }
        else{
            printf("Invalid choice entered.\n");
            exit(EXIT_FAILURE);
        }
        
        
    }
    
}
