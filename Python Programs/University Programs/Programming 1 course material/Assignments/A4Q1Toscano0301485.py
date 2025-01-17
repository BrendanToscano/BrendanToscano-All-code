######################### 
# Course: COMP 1113 FA01, 2022 
# Assignment 4, Question 1 
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/10/23
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

import statistics

bag_size = []
bag_cost = []

while (True):
    bagSize = (float(input("Enter the size of the bag of the vegetables purchased (in grams): ")))
    bagCost = (float(input("Enter the cost of that bag (in $): ")))
    print(f"The cost of a bag per 100g is {((bagCost / bagSize) * 100):.3f}$/100g")
    toContinue = (input("To end program type 'end' or -1. To continue press enter \n"))
    bag_size.append(bagSize)
    bag_cost.append(bagCost)
    if ((toContinue == "-1") or (toContinue == "end")):
        break
    else:
        continue

overall_cost = (sum(bag_cost))
overall_weight = (sum(bag_size))

print(f'''Overall cost of bags: ${overall_cost}
Overall weight of bags: {overall_weight}g
Overall cost per 100g: {((overall_cost/overall_weight)*100)}$/100g
The mean/average cost per bag: ${statistics.mean(bag_cost)}
The median cost per bag: ${statistics.median(bag_cost)}
Max cost of bag: ${max(bag_cost)}
Min cost of bag: ${min(bag_cost)}
Max size of bag: {max(bag_size)}g
Min size of bag: {min(bag_size)}g''')