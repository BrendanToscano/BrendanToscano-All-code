######################### 
# Course: COMP 1113 FA01, 2022 
# Lab 10
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/11/28
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################
import random as r
def randomLetter(value):
    random_num = r.randint(0,len(value)-1)
    return value[random_num]
word = input("Please supply a word: ")
print(f"My random letter is {randomLetter(word)}")
x = 1
while (True):
    word = input("Another word please: ")
    print(f"My random letter is {randomLetter(word)}")
    x += 1
    if (x%5 == 0) and (x%10 != 0):
        print("Are you having fun yet?!?!")
    elif (x%10 == 0):
        print("Are you having fun yet?!?!")
        input1 = input("Would you like me to tell you how to get out of this endless loop? ")
        if (input1.lower()) == "yes":
            print("Try telling me to stop")
        elif (input1.lower()) == "no":
            print("Then let's enjoy the ride")
    elif (word.lower()) == "stop":
        print("All done")
        break



