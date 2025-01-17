######################### 
# Course: COMP 1113 FA01, 2022 
# Assignment 2, Question 1 
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/09/26
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

#Asking user his/her name
user_name = input("What is your name? ")
#Asking if the user has a fever
fever = input("Do you have a fever? (i.e. chills/sweats)(y/n) ")
#Asking if the user has a cough
cough = input("Do you have cough? (new or worsening)(y/n) ")

#if user replies with y or yes for any one they are asked to stay at home and schedule a test
if (fever == "y" or cough == "y" or fever == "yes" or cough == "yes"):
    print(user_name + ", you should stay home and schedule a test ")
#if the user replies with n or no for both then they are asked a floowing set of question   
elif (fever == "n" and cough == "n") or (fever =="no" and cough == "no"):
    headache = input("Do you have a headache? (y/n) ")
    sore_throat = input("Do you have a sore throat? (y/n) ")
    congestion = input("Do you have runny nosr / nasal congestion? (y/n) ")
    breath = input("Do you have shortness of breath? (y/n) ")
    #creating a list for all inputs
    input1 = [headache , sore_throat , congestion , breath]
    #counting all y inputs in list
    no_of_y = input1.count("y")
    #if all questions asked result in a n then the user is asked to come to class
    if (headache == "n" and sore_throat == "n" and congestion == "n" and breath == "n"):
        print(user_name + ", you should come to class")
    #if the user replies for y for one question they are required to stay at home
    elif (no_of_y == 1) :
        print(user_name + ", you should stay at home")
    #if the user replies with y for more than 1 question they are required to stay at home and call 811
    elif (no_of_y > 1) :
        print(user_name + ", you should stay home and call 811")
    else:
        print("The answer to the question is invalid. Please try again using only y or n")
else:
    print("The answer to the question is invalid. Please try again using only y or n")