##################################
# This file is not to be corrected.
##################################
import string
import sys

#18th November 2:02 - 2:19
# Asking user for file name
#file = sys.argv[1]
file = 'test.txt'
wordBucket = []
# Catching error while opening or reading file
try:
    with open(file, "r") as lines:
        for line in lines:
            for punctuation in string.punctuation:
                line = line.replace(punctuation, '')
            for word in line.split():
                # Appending word to the list but converting it to lowercase before doing so
                wordBucket.append(word.lower())
except Exception as e:
    print(f"{e}")
    print("User Instructions:- python3 HashTables.py file.txt")
    sys.exit()

# 4:34 -4:40
def checkIndex(index):
    while True:
        if wordBucketList[index][0] is None:
            return index
        else:
            if index == len(wordBucketList) - 1:
                index = 0
            else:
                index += 1

# 4:27 -4:34
def getIndex(word):
    totalAscii = 0
    for i in word:
        totalAscii += ord(i)
    index = totalAscii % len(wordBucketList)
    return checkIndex(index)

# This took me a long time to figure out.
# You can't use something like wordBucketList = [[None, 1]] * len(wordBucket) because python
# Will change all elements of the list.
wordBucketList = []
for i in range(len(wordBucket)):
    wordBucketList.append([None, 1])

# 4:13 - 4:27 4:40-4:41
for word in wordBucket:
    check = False
    for index in range(len(wordBucketList)):
        if word == wordBucketList[index][0]:
            num = wordBucketList[index][1]
            num += 1
            wordBucketList[index][1] = num
            check = True
            break
    if check:
        continue
    else:
        index = getIndex(word)
        wordBucketList[index][0] = word

# For both function and bottom userInput part 6:35 - 6:42
def printData():
    for word in enumerate(wordBucketList):
        print(word)

def findWordCount():
    word = str(input("Please enter the word you want to find the count of: "))

    for index in range(len(wordBucketList)):
        if word == wordBucketList[index][0]:
            print(f"The word count for word '{wordBucketList[index][0]}' is {wordBucketList[index][1]}")
            return
    print("Sorry, word not found")
    return

while True:
    userInput = input("1. Find the count of a word. \n2. Print all data \n3. Quit \nEnter option 1, 2 or 3: ")

    if userInput == "1":
        findWordCount()
    elif userInput == "2":
        printData()
    elif userInput == "3":
        break
    else:
        print("Invalid input, Try again")