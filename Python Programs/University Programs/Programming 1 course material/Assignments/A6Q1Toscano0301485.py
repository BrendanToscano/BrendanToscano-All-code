######################### 
# Course: COMP 1113 FA01, 2022 
# Assignment 6 Question 1
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/11/17
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################
def listCompare(list1 , list2):
    '''Checks which list is bigger and returns the percentage of the smaller list to that of the bigger list'''
    count = 0
    # Checks if either list is empty and prints a statement saying the lists are 0% equal. If one list is empty and the other has element an since we are comparing the smaller list to the bigger list it will also print 0%.
    if (len(list1) == 0) or (len(list2) == 0):
        return "The lists are 0.0% equal"
    # Checks if length of list 1 is greater or equal to the length of list 2
    elif (len(list1)) >= (len(list2)):
        n = len(list1)
    # Checks if the length of list 2 is greater than the the length of list 1
    elif (len(list1)) < (len(list2)):
        n = len(list2)
    for value1 in range(n):
        # Checks if the values in the lists are a string and then converts them to lower case. Hence making sure the program is not case sensitive.
        if (isinstance(list1[value1] , str) == True) and (isinstance(list2[value1] , str) == True):
            # If both strings are equal then it adds 1 to count
            if (list1[value1].lower() == list2[value1].lower()):
                count += 1
        # If value in list1 is equal to value in list 2 then it adds 1 to count
        elif (list1[value1] == list2[value1]):
            count += 1
        # If value in list1 is not equal to value in list 2 then it breaks the code/ends the code
        elif (list1[value1] != list2[value1]):
            break
    # Calculates the percentage and then returns value
    value = "The lists are "+str((count/n)*100)+"%"+" equal"
    return value

# All lists
list1 = [1,2.0,3,"fred"]
list2 = [1,2,3,"Fred"]
list3 = [1,2,"3",3,4,5,6,5,6,7]
list4 = []
list5 = [2,3,4,5,5]
# Compares list1 and list2
print(listCompare(list1 , list2))
# Compares list2 and list3
print(listCompare(list2 , list3))
# Compares list4 and list5
print(listCompare(list4 , list5))



