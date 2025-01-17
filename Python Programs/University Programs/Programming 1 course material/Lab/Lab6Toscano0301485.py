######################### 
# Course: COMP 1113 FA01, 2022 
# Lab 6
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/10/25
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################
import random
def goodAdvice():
    print("Go to class")
    print("Write many programs")
    return

def badAdvice():
    print("Skip class")
    print("Cram in December")
    return

choice1 = (input("Would you like good advice or bad advice(g/b): "))

if (choice1 == "g"):
    goodAdvice()
elif (choice1 == "b"):
    badAdvice()
else:
    a = random.randrange(1,4)
    if (a == 1):
        goodAdvice()
    else:
        badAdvice()