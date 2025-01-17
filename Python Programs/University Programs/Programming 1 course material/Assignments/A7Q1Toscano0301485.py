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
    for row in range(size):
        temp_list = []
        for column in range(size):
            temp_list.append(r.randint(0,1))
        card.append(temp_list)

    printCard(card)

def printCard(card):
    '''Prints a 2D list'''
    for row in card:
        for column in row:
            print(column, end=' ')
        print('')

def processCard(card):
    '''Replaces the 0's and 1's from the 2D list with True and False'''
    
    i = -1
    for row in range(len(card)):
        i += 1
        j = -1
        for column in range(len(card)):
            j += 1
            if (card[i][j] == 0):
                card[i][j] = False
            elif (card[i][j] == 1):
                card[i][j] = True
                

    printCard(card)

card = []
generateCard(card, 5)
print("")
processCard(card)


    
