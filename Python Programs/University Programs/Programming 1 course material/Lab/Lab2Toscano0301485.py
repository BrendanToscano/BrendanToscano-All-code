######################### 
# Course: COMP 1113 FA01, 2022 
# Lab 2, Question 1 
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/09/21
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################

l1 = 10
b1 = 5

l2 = 11
b2 = 3

area1 = int(l1 * b1)
area2 = int(l2 * b2)

per1 = 2*(l1 + b1)
per2 = 2*(l2 + b2)

diff_area = abs(area1 - area2)

print("Rectangle 1's perimeter is", per1)
print("Rectangle 1's area is", area1)

print("Rectangle 2's perimeter is", per2)
print("Rectangle 2's area is", area2)

print("The difference in area is", diff_area)