######################### 
# Course: COMP 1113 FA01, 2022 
# Lab 9
# Author: Brendan Toscano
# Student ID: 0301485
# email address: 0301485t@acadiau.ca
# Date: 2022/11/20
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty. 
#########################
def printDictionary(dictionary):
    for value in dictionary:
        print(f"{value}: {dictionary[value]}")
def lookForE(dictionary):
    for value in dictionary:
        if ("e" in dictionary[value].lower()):
            dictionary[value] = "Not telling"
    return dictionary

fav_games = {"Favourite":"Flames", "Like":"Oilers", "Kinda Like":"Wild", "Ok":"Jets"}
printDictionary(fav_games)
print("")
fav_games["Like"] = "Senators"
fav_games["Dislike"] = "Leafs"
printDictionary(fav_games)
print("")
printDictionary(lookForE(fav_games))



