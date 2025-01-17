#########################
# Course: COMP 2113 FA01, 2023
# Assignment 9, Question 1
# Author: Brendan Toscano
# Student ID: 0301485t
# email address: 0301485t@acadiau.ca
# Date: 2023-12-03
# I certify that this code is my own.
# I have not broken any rules concerning Academic Dishonesty.
#########################
# What does this program do?
# The program is an implementation of skip list.
# It has 3 main function.
# First function to insert the value in the skip list.
# The second function to delete the value from the skip list.
# The third function to print all the values of the skip list.
# The program has a menu that will call these three functions.
# The program also takes in a CSV file from the command line and uses it to insert values into the skip list
#########################
import random
import sys

# 2:27 - 2:35pm
# Node class for skiplist
class Node:
    def __init__(self, value, level):
        self.value = value
        self.next = [None] * level

# 3rd Decmeber 2:35pm - 5th december 11:40pm
class skipList:
    # Setting default maxLevel to 10.
    def __init__(self, maxLevel = 10):
        self.maxLevel = maxLevel
        self.head = Node(None, maxLevel)
        self.numOfLevels = 1
    # 3rd december 2:27
    # Returns number of levels.
    def coinFlip(self):
        count = 1
        while random.randint(1,2) == 1:
            if count >= self.maxLevel:
                break;
            count += 1
        return count
    # 3rd December 4:00pm - 5:26pm 4th December 9:21pm - 10:36pm 20th December 5:14 - 8:07
    # Add element to the skip list
    def addToList(self, value):
        pointers = [None]*(self.maxLevel)
        current = self.head

        for i in range(self.numOfLevels, -1, -1):
            while current.next[i] and current.next[i].value < value:
                current = current.next[i]
            pointers[i] = current

        current = current.next[0]
        if current is None or current.value != value:
            count = self.coinFlip()

            if count > self.numOfLevels:
                for i in range(self.numOfLevels + 1, count + 1):
                    pointers[i] = self.head
                self.numOfLevels = count

            newNode = Node(value, count)

            for i in range(count):
                newNode.next[i] = pointers[i].next[i]
                pointers[i].next[i] = newNode

    # 20th December 8:07 - 9:36
    # Delete element from the skip list
    def deleteFromList(self, value):
        pointers = [None] * (self.maxLevel)
        current = self.head

        for i in range(self.numOfLevels, -1, -1):
            while current.next[i] and current.next[i].value < value:
                current = current.next[i]
            pointers[i] = current

        current = current.next[0]
        if current is None or current.value != value:
            pass
        else:
            for i in range(self.numOfLevels + 1):
                if pointers[i].next[i] != current:
                    break
                pointers[i].next[i] = current.next[i]

            while(self.numOfLevels > 1 and self.head.next[self.numOfLevels - 1] is None):
                self.numOfLevels -= 1

    # 10:29 - 11:40
    # print skip list
    def printList(self):
        #list = []
        #for i in range(self.numOfLevels):
        #    current = self.head
        #    while current.next[i]:
        #        list.append(current.next[i].value)
        #        current = current.next[i]
        #
        #for i in range(self.numOfLevels):
        #    current = self.head
        #    j = 0
        #    while current.next[i]:
        #        if j < len(list) and current.next[i].value == list[j]:
        #            print(current.next[i].value, end=' ')
        #            j += 1
        #        else:
        #            print(" ", end=' ')
        #        current = current.next[i]
        #    print()

        for i in range(self.numOfLevels):
            current = self.head.next[i]
            while current:
                print(current.value, end=' ')
                current = current.next[i]
            print()


# 3rd 1:30 - 1:44pm
skipList = skipList()
try:
    # Opening and reading file from command line.
    with open(sys.argv[1], "r") as file:
        for line in file:
            values = line.split(",")
            for value in values:
                # Removing whitespaces before inserting into skipList.
                skipList.addToList(int(value.strip()))
except Exception as e:
    # Catches any errors that occur here and prints them to the user and gracefully exits the program.
    print(f"{e}")
    sys.exit()

# 1:44 - 2:27pm
# Menu
while True:
    print("a) Insert value to the skip list.")
    print("b) Remove value from the skip list.")
    print("c) Print the skip list.")
    print("d) Exit.")
    option = input("Enter an option:- ")

    if (option == 'a'):
        value = int(input("Enter the value to insert:- "))
        skipList.addToList(value)
    elif (option == 'b'):
        value = int(input("Enter the value to insert:- "))
        skipList.deleteFromList(value)
    elif (option == 'c'):
        skipList.printList()
    elif (option == 'd'):
        sys.exit()
    else:
        print("Invalid option entered, try again")


