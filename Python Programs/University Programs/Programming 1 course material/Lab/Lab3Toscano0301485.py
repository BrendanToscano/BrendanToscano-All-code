######################### 
# Course: COMP 1113 FA01, 2022 
# Lab 3
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/09/26
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

user_name = input("What is your name? ")
fav_num = int(input(user_name + " please tell me your favourite number: "))
least_fav_num = int(input(user_name + " please tell me your least favourite number: "))

if (fav_num > least_fav_num):
    print(user_name , "your favourite number is bigger than your least favourite number")
elif (fav_num < least_fav_num):
    print(user_name , "they say if your least favourite number is greater than your \
favourite number, you're lucky. Guess you're lucky")
else:
    print(user_name , "wait your favourite number and your least favourite number are the same?")