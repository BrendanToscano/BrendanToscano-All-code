import sys

#########################
# Course: COMP 2113 FA01, 2023
# Assignment 5, Question 1
# Author: Brendan Toscano
# Student ID: 0301485t
# email address: 0301485t@acadiau.ca
# Date: 2023-10-26
# I certify that this code is my own.
# I have not broken any rules concerning Academic Dishonesty.
#########################
# What does this program do?
# There are 3 algorithms that can be called to sort a txt file given by the user in the command line.
# if the user calls 1 it will sort the txt file using selection sort
# If the user calls 2 it will sort the txt file using insertion sort
# If the user calls 3 it will sort the txt file using bubble sort
# In the command line the user should enter a number 1-3 to call the sorting algorithm with the txt file after.
#########################
# Checks implemented:
# Should print list is empty for empty lists
# Any error will be caught and the program should gracefully tells the the user and end.
#########################

# Selection sort function that takes in a list of nums.
def selectionSort(nums):
    # Checking to see if list is empty.
    if(len(nums) == 0):
        print("List is empty")
    else:
        # Setting starting position.
        for i in range(len(nums) - 1):
            minPos = i
            # Getting the posiiton of the min number.
            for j in range(i+1, len(nums)):
                if nums[minPos] > nums[j]:
                    minPos = j
            # Swapping the min num with the starting position.
            num = nums[i]
            nums[i] = nums[minPos]
            nums[minPos] = num
        # Printing the list.
        for i in nums:
            print(i)
 
# Insertion sort function that takes in a list of nums.
def insertionSort(nums):
    # Checking to see if list is empty.
    if(len(nums) == 0):
        print("List is empty")
    else:
        # Setting n to i starting from pos 1
        for i in range(1, len(nums)):
            n = i
            while True:
                # If n element is smaller than n-1 element then we swap and decrement n adn redo till n = 0.
                if n > 0 and nums[n] < nums[n-1]:
                    num = nums[n]
                    nums[n] = nums[n-1]
                    nums[n-1] = num
                    n -= 1
                else:
                    break
        # Printing the list
        for i in nums:
            print(i)

# Bubble sort function that takes in a list of nums
def bubbleSort(nums):
    # Checking to see if list is empty
    if(len(nums) == 0):
        print("List is empty")
    else:
        # Will keep swap cycle till no swaps are done.
        while True:
            n = 0
            # Will repeat till end of the list.
            for j in range(len(nums) - 1):
                # Comparing the j and j+1 elements and swaping if j element > j+1 element.
                if(nums[j] > nums[j+1]):
                    num = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = num
                    # If swapped will set value to n = 1 to start loop again.
                    n = 1
            # If no swaps done i.e. n != 1 then breaks the loop.
            if n == 0:
                break
        # Printing the list
        for i in nums:
            print(i)

# Checks to see if 3 arguments are int he command line. If less or more instructs user.
if len(sys.argv) != 3:
    print("User Instructions: python3 sorting.py \"1-3 to choose sorting algorithm\" \"file.txt\" ")
else:
    nums = []
    # Catch any errors from invalid file to any error in the above functions and gracefully fails.
    try:
        # Opening the file
        file = open(sys.argv[2], "r")
        for num in file:
            nums.append(int(num))
        # Closing the file
        file.close()
        if sys.argv[1] == "1":
            selectionSort(nums)
        elif sys.argv[1] == "2":
            insertionSort(nums)
        elif sys.argv[1] == "3":
            bubbleSort(nums)
        else:
            print("User Instructions: python3 sorting.py \"1-3 to choose sorting algorithm\" \"file.txt\" ")
            
    except Exception as e:
        print(f"{e}")
        print("User Instructions: python3 sorting.py \"1-3 to choose sorting algorithm\" \"file.txt\" ")
        
