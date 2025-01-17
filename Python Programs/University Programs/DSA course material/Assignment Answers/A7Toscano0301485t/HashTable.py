#########################
# Course: COMP 2113 FA01, 2023
# Assignment 7, Question 1
# Author: Brendan Toscano
# Student ID: 0301485t
# email address: 0301485t@acadiau.ca
# Date: 2023-11-18
# I certify that this code is my own.
# I have not broken any rules concerning Academic Dishonesty.
#########################
# What does this program do?
# The program is an implementation of Hash tables in Python.
# The program will get the file name off the command line. It will open the file and read the text in the file.
# Each word is then hashed from the file into the bucket. If the word exists it will increment the count.
# If not then it will add the word to the bucket with a default count of 1.
# The program uses a dynamic array that will be doubled in size everything its load factor passes 0.8.
# The same process is then done again for the new list with double the size.
# The program is using open addressing instead of seperate chaining.
# To make sure no elements overlap we are using linear probing.
# This program will also keep asking the user if they want to print the entire list or find the count of the word.
# or quit out of the program. If the user chooses to quit the program then program will quit. Else will keep asking user
#########################
import string
import sys

# 4:27 -4:34 #4:34 - 4:40
# To get index of the word by adding the ascii values and dividing by the length of the hash table. After getting that
#value it will keep incrementing till it find an empty position once it reaches the end of the list without finding
#a poation it will reset the index to 0 and continue checking.
def getIndex(word, wordBucketList):
    totalAscii = 0
    for i in word:
        totalAscii += ord(i)
    index = totalAscii % len(wordBucketList)
    while True:
        if wordBucketList[index][0] is None:
            return index
        else:
            if index == len(wordBucketList) - 1:
                index = 0
            else:
                index += 1

# 4:13 - 4:27 4:40-4:41
# Will check if word is already in the table and will increment its count. We have a check value to see it a value was
#changed or not.
def addToBucket(word, wordBucketList):
    # Check is set to false if the count is changed will be set to true
    check = False
    # Going through entire list and checking if the word is in the bucket. If it is will increment count of word.
    for index in range(len(wordBucketList)):
        if word == wordBucketList[index][0]:
            num = wordBucketList[index][1]
            num += 1
            wordBucketList[index][1] = num
            check = True
            break
    return check

# Will create a new list twice the size of the whole list. Will then redo the entire adding to the hash table process using
#the length of the new list.
def resizeList(wordBucketList):
    wordBucket = []
    # Creating a new list double the size.
    for i in range(len(wordBucketList) * 2):
        wordBucket.append([None, 1])
    # Reading all words to the new bucket with new size.
    for word in wordBucketList:
        word = word[0]
        check = addToBucket(word, wordBucket)
        # If word count was not increased thn will add the word to the bucket.
        if check:
            continue
        else:
            index = getIndex(word, wordBucket)
            wordBucket[index][0] = word
    return wordBucket

# For both function and bottom userInput part 6:35 - 6:42
# Will print all data of the hash table with the index on the left and value on the right.
def printData(wordBucketList):
    for word in enumerate(wordBucketList):
        print(word)

# Will ask the user for the word they want the count of then it will check for the word through the hash table
#If word is found will diaplay the word and count of the word. If not it will tell the user the word was not found.
def findWordCount(wordBucketList):
    word = str(input("Please enter the word you want to find the count of: "))

    # Finding count of word. If word doestn exist telling user.
    for index in range(len(wordBucketList)):
        if word == wordBucketList[index][0]:
            print(f"The word count for word '{wordBucketList[index][0]}' is {wordBucketList[index][1]}")
            return
    print("Sorry, word not found")
    return

# This program will open the file read the file and remove punctuations it will also convert the word read to lowercase.
#It will then check for load factor and if it is more than 0.8 it will call the resizeList function. The fucntion should
#return a new list with all previously added values. The function also call the check if in list fucntion depending on
#what value is returned(true or false) it will continue or add the word to the list.
#Once the whole process is done it will return the final list.
#Any errors during this entire process will be caught and returned to the user the program will exit as well.
def openFile():
    wordBucketList = []
    noOfItemsAdded = 0
    for i in range(10):
        wordBucketList.append([None, 1])
    #18th November 2:02 - 2:19
    try:
        # Getting file name from command line.
        file = sys.argv[1]
        # Catching error while opening or reading file

        with open(file, "r") as lines:
            for line in lines:
                # Replacing punctuations with nothing
                for punctuation in string.punctuation:
                    line = line.replace(punctuation, '')
                    line = line.replace('…', '')
                    line = line.replace('—', '')
                # Finding whitespaces and splitting the whole thing into words.
                for word in line.split():
                    # Coverting all words to lowercase
                    word = word.lower()
                    # Checking if load factor is more than 0.8. If it is then calling the rezise fucntion.
                    if noOfItemsAdded / len(wordBucketList) > 0.8:
                        wordBucketList = resizeList(wordBucketList)
                    # Appending word to the list but converting it to lowercase before doing so
                    check = addToBucket(word, wordBucketList)
                    if check:
                        continue
                    else:
                        noOfItemsAdded += 1
                        index = getIndex(word, wordBucketList)
                        wordBucketList[index][0] = word
        return wordBucketList
    # Catching all errors and displaying them to the user. Also giving user instructions and gracefully exiting.
    except Exception as e:
        print(f"{e}")
        print("User Instructions:- python3 HashTables.py file.txt")
        sys.exit()

# Calling the above function and setting the returned list to another variable so we can use it below
wordBucketList = openFile()
# Asks user what input the enter 1,2 or 3. If the user enters anyhting  else then the user will be asked again.
while True:
    userInput = input("1. Find the count of a word. \n2. Print all data \n3. Quit \nEnter option 1, 2 or 3: ")

    if userInput == "1":
        findWordCount(wordBucketList)
    elif userInput == "2":
        printData(wordBucketList)
    elif userInput == "3":
        break
    else:
        print("Invalid input, Try again")