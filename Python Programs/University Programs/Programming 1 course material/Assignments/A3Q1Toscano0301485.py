######################### 
# Course: COMP 1113 FA01, 2022 
# Assignment 3, Question 1 
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/10/04
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

#Importing the ranrange library
from random import randrange

#Defineing values
count1 = 0
count2 = 0

loop1 = 0
loop2 = 0

#for running the program 4 times
for loop1 in range(0,4):
    #Random number from 0-10
    x = randrange(10)
    # To print which round the player is playing
    print("Round", loop1 + 1)
    #Creating a loop
    while (loop2 == 0):
        #Asking user to enter guess from 0-10
        guess1 = int(input("Enter a guess from 0-9: "))
        #Adding 1 to count every time the program runs
        count1 = count1 + 1
        #Condition to check if the guess is correct
        if (guess1 == x):
            print("You got the right number")
            print("The number was", x)
            break
        #Condition to check if the guess was too low
        elif (guess1 < x):
            print("The number you entered is too low, try again") 
        #Condition to check if the guess was too high
        else:
            print("The number you entered is too high, try again")
            
#To print the average number of guesses in the 4 runs
print("Average number of guesses =", ((count1)/4))

