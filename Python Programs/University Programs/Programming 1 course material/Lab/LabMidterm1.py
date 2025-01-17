#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:52:23 2022

@author: brendan
"""

numrounds = (int(input("Please enter number of rounds: ")))
numOutputlines = (int(input("Please enter the number of output lines: ")))
x = 0
currentround = 0
for x in range(numrounds):
    currentround += 1
    if (currentround == 2):
        print("ROUND 2 IS THE BEST")
        charc1 = (input("What's your character: "))
        for x in range(numOutputlines):
            print("**"+charc1+"**")
    elif (currentround == numrounds):
        print("Almost done")
        charc2 = (input("What's your character: "))
        for x in range(numOutputlines):
            print("**"+charc2+"**")
    else:
        print("Just another round")
        charc3 = (input("What's your character: "))
        for x in range(numOutputlines):
            print("**"+charc3+"**")
print("Thanks for participating")