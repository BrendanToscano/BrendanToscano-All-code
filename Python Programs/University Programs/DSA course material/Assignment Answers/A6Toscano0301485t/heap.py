#########################
# Course: COMP 2113 FA01, 2023
# Assignment , Question 1
# Author: Brendan Toscano
# Student ID: 0301485t
# email address: 0301485t@acadiau.ca
# Date: 2023-11-14
# I certify that this code is my own.
# I have not broken any rules concerning Academic Dishonesty.
#########################
# What does this program do?
# It reads a file from the use and inserts the numbers into the list.
# heapify() function that will convert the list/array into a heap.
# getMax() function that will return the value from the root of the heap.
# removeMax() function that will remove the root from the heap and return the value.
# pushDown() function that can be used to "fix" the heap once you remove the root value.
# bubbleUp() function that can be used when adding a new value to the heap.
# function that allows you to add a new value to the heap.
#########################

# Function to open file, read the numbers from it and append it to a list
def openFile():
    # Keeps running till a valid file is entered
    while True:
        # Asking user for file name
        file = str(input("Enter file: "))
        numsList = []
        # Catching error while opening or reading file
        try:
            with open(file, "r") as nums:
                for num in nums:
                    number = int(num)
                    numsList.append(number)
            return numsList
        except Exception as e:
            print(f"{e}")
            print("Enter file name again. Example:- file.txt")

# Converts list to max heap
def heapify(list):
    index = len(list) - 1
    # Will run till index is 0
    while index >= 0:
        # Replaced this with pushDown
        pushDown(list, index)
        index -= 1

# Getting the max element.
def getMax(list):
    if len(list) == 0:
        print("Heap is empty")
    else:
        # Prints the max element of the list.
        max = list[0]
        print("The max element of the heap is:", max)

# Removing max element and calling push down.
def removeMax(list):
    if len(list) == 0:
        print("Heap is empty")
    else:
        # Removes the first element of the list and uses pushdown to fix the list.
        print("The popped element is:", list.pop(0))
        num = list.pop()
        list.insert(0, num)
        pushDown(list, 0)

# Using to fix the list.
def pushDown(list, index):
    while index < len(list):
        # Setting the left and right nodes and largest
        largestElementIndex = index
        leftNode = 2 * index + 1
        rightNode = 2 * index + 2

        # Checking if left node is greater than the parent node. If yes then setting the largest node to the left node.
        if leftNode < len(list) and list[leftNode] > list[largestElementIndex]:
            largestElementIndex = leftNode
        # Checking if right node is greater than parent node. If yes then setting the largest to the right node.
        if rightNode < len(list) and list[rightNode] > list[largestElementIndex]:
            largestElementIndex = rightNode

        # If largest node was changed then swapping the parent.
        if largestElementIndex != index:
            temp = list[largestElementIndex]
            list[largestElementIndex] = list[index]
            list[index] = temp
            # Setting the new index.
            index = largestElementIndex
        else:
            break

# Pushing up from the bottom of the heap.
def bubbleUp(list):
    index = len(list) - 1
    while index > 0:
        parent = (index - 1) // 2
        # If parent is bigger than added node than swap. Setting the index to the swapped ndoe.
        if list[parent] < list[index]:
            temp = list[parent]
            list[parent] = list[index]
            list[index] = temp
            index = parent
        else:
            break

# Adding value to the heap.
def addValue(list, element):
    # Adding element to the end of the list.
    list.append(element)
    # Bubble up does the same thing so I assume this is fine.
    bubbleUp(list)

# Displaying values of the heap
def display(list):
    for i in enumerate(list):
        print(i)
    print("")


list = openFile()

print("The list: ")
display(list)

print("The Max heap is: ")
heapify(list)
display(list)

getMax(list)

print("Heap after removing root: ")
removeMax(list)
display(list)

print("Add element to the heap using bubble up:")
addValue(list, 10)
display(list)