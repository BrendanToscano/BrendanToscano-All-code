#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
/*
 * Course: COMP 2103 FA01, 2023
 * Assignment 2, Question 1
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-10-08
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.

The program takes a file in from the command line
and reads each character inside the txt file.
It will check for digits, chracters, punctuations
and other characters.
It will also count the total number of character in the txt file.
It will then neatly display all of them with their count
*/

int main(int argc, char *argv[]) {
	int c;
	int numOfDigits = 0;
	int numOfCharacters = 0;
	int numOfPunctuations = 0;
	int numOfOthers = 0;
	int numOfTotal = 0;
	

	// Creating a loop that will stop once it reaches the end of the file.
	while((c = getchar()) != EOF){	
		// Checking if digits and incrementing the variable numOfDigits.
		if(isdigit(c))
			numOfDigits++;
		// Checking if characters/alphabets and incrementing the variable numOfcharacters.
		else if(isalpha(c))
			numOfCharacters++;
		// Checking if puncctuations and incrementing the variable numOfPunctuations.
		else if(ispunct(c))
			numOfPunctuations++;
		// Checking for every other type of character/input.
		else
			numOfOthers++;
		numOfTotal++;
	}
	
	// Neatly printing the number of digits, characters, punctuations, other characters and total.
	printf("Number of Digits           : %d\n", numOfDigits);
	printf("Number of Characters       : %d\n", numOfCharacters);
	printf("Number of Punctuations     : %d\n", numOfPunctuations);
	printf("Number of other characters : %d\n", numOfOthers);
	printf("Total number of chracters  : %d\n", numOfTotal);

}
