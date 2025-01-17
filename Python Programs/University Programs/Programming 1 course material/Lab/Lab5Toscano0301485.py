######################### 
# Course: COMP 1113 FA01, 2022 
# Lab 5
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/10/12
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

count1 = 0
count2 = 0
count3 = 0

for count1 in range(1,6):
    count1 += 1
    if (count1 % 2 == 0):
        print("Stay positive \n")
        for count2 in range(0,3):
            count2 +=1
            print("This too shall pass \n")
    else:
        print("Keep on truckin' \n")
        for count3 in range(0,3):
            count3 +=1
            print("This too shall pass \n")

print("What a wonderful world")