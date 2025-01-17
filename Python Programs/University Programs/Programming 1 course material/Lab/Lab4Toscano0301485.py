######################### 
# Course: COMP 1113 FA01, 2022 
# Lab 4
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/10/04
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

print("I am pretty repetitive \n")

loop1 = 0
y = 0
while (loop1 == 0):
    input1 = input("Do you want to talk? (y/n) ")
    print("")
    if (input1 == "y"):
        y += 1
    elif (input1 == "n") and (y == 0 ):
        print("But why not? \n")
        print("Safe travels \n" )
        print(end = "================")
        break
    elif (input1 == "n") and (y < 4 ):
        print("But why not? \n")
        print("Thanks for chatting \n")
        print(end = "================")
        break
    elif (input1 == "n") and (y >= 4 ):
        print("But why not? \n")
        print("That was fun \n")
        print(end = "================")
        break
    else:
        print("This is an ambiguous answer")
    
