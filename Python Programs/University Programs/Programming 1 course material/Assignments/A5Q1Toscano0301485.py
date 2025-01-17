######################### 
# Course: COMP 1113 FA01, 2022 
# Assignment 1 Question 1
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/11/07
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################
from statistics import mean

def number_type(*args):
    ''' Checks whether the number in the list is an int or float '''
    intvalues = []
    floatvalues = []
    for number in args:
        if isinstance(number , int):
            intvalues.append(number)
        elif isinstance(number, float):
            floatvalues.append(number)
    intNumbers = len(intvalues)
    floatNumbers = len(floatvalues)

    global avg_int
    global avg_float
# If list is empty
    if (intNumbers == 0) and (floatNumbers == 0):
        return 0
# If list contains only ints
    elif (intNumbers != 0) and (floatNumbers == 0):
        avg_int = mean(intvalues)
        return 1
# If list contains only floats
    elif (intNumbers == 0) and (floatNumbers != 0):
        avg_float = mean(floatvalues)
        return 2
# If list contains a mix of ints or floats
    elif (intNumbers != 0) and (floatNumbers != 0):
        avg_int = mean(intvalues)
        avg_float = mean(floatvalues)
        return 3

def sol_list(x):
    '''To print the type of values of given values'''
    if (x == 0):
        print("There are no values in the list")
    elif (x == 1):
        print(f"The list contained ints, and the average is {avg_int}")
    elif (x == 2):
        print(f"The list contained floats, and the average is {avg_float}")
    elif (x == 3):
        print(f"The list contained a mix of ints and floats. The average of the ints was {avg_int}, and the average of the floats was {avg_float}")

sol_list(number_type(1,4,5,6,2,10,5,7))
sol_list(number_type(2.4,5.6,5.2,4.9,6.2,5.71))
sol_list(number_type(2,3,3,5.4,2,6.7,8.9))
sol_list(number_type())

