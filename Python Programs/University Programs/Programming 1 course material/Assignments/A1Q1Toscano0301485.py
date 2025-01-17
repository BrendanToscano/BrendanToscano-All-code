######################### 
# Course: COMP 1113 FA01, 2022 
# Assignment 1, Question 1 
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/09/21
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

bigNum = int(input("Input Big Number ")) 
smallNum = int(input("Input Small Number "))

big_div_small = bigNum / smallNum

print(bigNum , "/"  , smallNum , "=" , big_div_small)

big_floor_small = bigNum // smallNum
big_power_small = bigNum ** smallNum
big_power_4_small = smallNum ** ((1/4) * bigNum)
big_modulus_small = bigNum % smallNum

print(big_floor_small , big_power_small , big_power_4_small , big_modulus_small , sep = "\n")


float_no1 = float(input("Enter a float number "))
word1 = input("Enter a word ")

print(float_no1 , float_no1 * 2 , "The word is " + word1 , sep = "\n")
