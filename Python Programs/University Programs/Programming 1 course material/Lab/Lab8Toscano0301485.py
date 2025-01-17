######################### 
# Course: COMP 1113 FA01, 2022 
# Lab 8
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/11/14
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################
def firstMiddleLast(string_val):
    first_val = string_val[0]
    last_val = string_val[-1]
    str_len = len(string_val)
    if (len(string_val) % 2) == 0:
        middle_val = (string_val[(str_len//2)-1] + string_val[(str_len//2)])
    else:
        middle_val = (string_val[str_len // 2])

    return first_val + middle_val + last_val

entry1 = (input("Please enter a word that is at least 5 characters long: "))
while (True):
    if (len(entry1) >= 5):
        print(firstMiddleLast(entry1))
        break
    else:
        entry1 = (input("That word is too short, try again: "))

