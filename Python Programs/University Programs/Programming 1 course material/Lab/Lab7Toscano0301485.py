######################### 
# Course: COMP 1113 FA01, 2022 
# Lab 7
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/11/08
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

def doubleRemainder(num1 , num2):
    '''Takes 2 arguments and  returns twice the remainder'''
    twiceRemainder = 2*(num1 % num2)
    return twiceRemainder

def quiz():
    '''Prints 4 choice lines'''
    print("A) divedend/divisor")
    print("B) divedent%divisor")
    print("C) (dividend%divisor)*2")
    print("D) just some magic")

dividend = (int(input("Please provide a divedend ")))
divisor = (int(input("Please provide a divisor ")))

value = doubleRemainder(dividend , divisor)
print(f"I've transformed these to {value}")

while (True):
    quiz()
    input1 = (input("What do you think I did to your numbers? "))

    if ((input1 == "c") or (input1 == "C")):
        print("Correct!\n",end="="*50)
        break
    else:
        print("Try again \n")
