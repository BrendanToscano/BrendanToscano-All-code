######################### 
# Course: COMP 1113 FA01, 2022 
# Assignment 7 Question 1
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/11/20
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################
import random as r
def generateCard(card, size):
    '''Generates a 2D list of size x size in the form of a matrix with random 0's and 1's'''
    size -= 1
    count1 = 0
    while (True):
       if (count1 <= size):
           count1 += 1
           card1 = []
           count2 = 0
           while (True):
               if (count2 <= size):
                   randomNumber = r.randint(0,1)
                   card1.append(randomNumber)
                   count2 += 1
               else:
                   break
           card.append(card1)
       else:
           break

    printCard(card)

def printCard(card):
    '''Prints a 2D list'''
    for row in card:
        for column in row:
            print(column, end=' ')
        print('')

def processCard(card):
    '''Replaces the 0's and 1's from the 2D list with True and False'''
    for i, row in enumerate(card):
        for j, column in enumerate(row):
            if (card[i][j] == 0):
                card[i][j] = False
            elif (card[i][j] == 1):
                card[i][j] = True

    printCard(card)

card = []
generateCard(card, 5)
print("")
processCard(card)