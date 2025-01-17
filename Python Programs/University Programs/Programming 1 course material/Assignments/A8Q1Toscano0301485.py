######################### 
# Course: COMP 1113 FA01, 2022 
# Assignment 8 Question 1
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/11/27
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################
import random as r
import statistics as s
def createSet(set_size , max_num):
    set0 = set()
    for non in range(set_size):
        random_number = r.randint(0,max_num)
        set0.update({random_number})
    return set0
def intersectionSize(target_size , set_size , max_num):
    num_of_runs = 0
    while (True):
        set1 = createSet(set_size , max_num)
        set2 = createSet(set_size , max_num)
        intersection = set1.intersection(set2)
        if len(intersection) >= target_size:
            print(intersection)
            return num_of_runs
        else:
            num_of_runs += 1

list1 = []
for x in range(0,5):
    list1.append(intersectionSize(12, 20 ,100))
print(f"Average number of iterations {s.mean(list1)}")

# The code takes a longer period to run when the target_size is 11 compared to when the target size is 10
# The code takes an even longer period to run when the target_size is 12 compared to when the target size is 11
