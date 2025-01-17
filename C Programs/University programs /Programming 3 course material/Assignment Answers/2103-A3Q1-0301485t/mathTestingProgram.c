/*
 * Course: COMP 2103 FA01, 2023
 * Assignment 3, Question 1
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-10-17
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.
*/
/*
 What does the program do?
 There are 4 methods (add, subtract, multiply and divide) each method display 2 numbers to the user asking them to either add, subtract, multiply or divide depending on the method. In each method, it will check if the user entered -1111 and return -1 or if the users answer is correct it will return 1 or incorrect it will return 0. In the main program if -1 gets returned it will break out of the loop and display the number of correct and incorrect answers by the user. If 1 gets returned it will increment the num of correct answers and contine to ask the user questions. If 0 is returned it will increment the num of incorrect answers and continue to ask the user questions.
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Creating add
int add(void){
    // Generating 2 random numbers and adding them
	int num1 = rand() % 12;
	int num2 = rand() % 12;
	int total = num1 + num2;
	
    // Display the 2 numbers to user
	printf("%d + %d\n", num1, num2);
    
	int userAddTotal;
    // Asking user the answer and checking if it is an integer
	if(scanf("%d", &userAddTotal) != 1){
		printf("Input was not an integer\n");
		exit(EXIT_FAILURE);
	}
    // Clearing input buffer just incase.
	while((getchar()) != '\n');
    
    // If user enters -1111 returns -1
	if(userAddTotal == -1111){
		return -1;
	}
    // If user answer matches the total
	else if(userAddTotal == total){
		printf("Correct\n");
		return 1;
	}
	else{
		printf("Incorrect\n");
		printf("Answer is %d\n", total);
		return 0;
	}
}

int subtract(void){
    // Generating 2 random numbers and subtracting them
	int num1 = rand() % 12;
	int num2 = rand() % 12;
	int total = num1 - num2;

    // Display the 2 numbers to user
	printf("%d - %d\n", num1, num2);

	int userSubtractTotal;
    // Asking user the answer and checking if it is an integer
	if(scanf("%d", &userSubtractTotal) != 1){
		printf("Input was not an integer\n");
		exit(EXIT_FAILURE);
	}
    // Clearing input buffer just incase.
	while((getchar()) != '\n');
    
    // If user enters -1111 returns -1
	if(userSubtractTotal == -1111){
		return -1;
	}
    // If user answer matches the total
	else if(userSubtractTotal == total){
		printf("Correct\n");
		return 1;
	}
	else{
		printf("Incorrect\n");
		printf("Answer is %d\n", total);
		return 0;
	}
}

int multiple(void){
    // Generating 2 random numbers and multiplying them
	int num1 = rand() % 12;
	int num2 = rand() % 12;
	int total = num1 * num2;
    
    // Display the 2 numbers to user
	printf("%d x %d\n", num1, num2);
    
	int userMultiplyTotal;
    // Asking user the answer and checking if it is an integer
	if(scanf("%d", &userMultiplyTotal) != 1){
		printf("Input was not an integer\n");
		exit(EXIT_FAILURE);
	}
    // Clearing input buffer just incase.
	while((getchar()) != '\n');
    
    // If user enters -1111 returns -1
	if(userMultiplyTotal == -1111){
		return -1;
	}
    // If user answer matches the total
	else if(userMultiplyTotal == total){
		printf("Correct\n");
		return 1;
	}
	else{
		printf("Incorrect\n");
		printf("Answer is %d\n", total);
		return 0;
	}
}

int divide(void){
    // Generating a random numbers
	int num1 = rand() % 12;
	int num2;
    // Generating another random number checking if it is smaller than num1
	do{
        // Making sure we dont get a 0
		num2 = (rand() % 12) + 1;
	}while(num1 < num2);
	double total = (double)num1/num2;
    // To get the first 2 digits
	total = (int)(total*100)/(double)100;
	
    // Display the 2 numbers to user
	printf("%d / %d\n", num1, num2);
	double userDivisionTotal;
    // Asking user the answer and checking if it is an integer or decimal.
	if(scanf("%lf", &userDivisionTotal) != 1){
		printf("Input was not a decimal\n");
		exit(EXIT_FAILURE);	
	}
    // Clearing input buffer just incase.
	while((getchar()) != '\n');
	if(userDivisionTotal == -1111){
		return -1;
	}
    // If user answer matches the total
	else if(userDivisionTotal == total){
		printf("Correct\n");
		return 1;
	}
	else{
		printf("Incorrect\n");
		printf("Answer is %lf\n", total);
		return 0;
	}
}

int main(void){
	srand(time(NULL));
	int input, choice, correct = 0, incorrect = 0;
    // Infinite loop to run any one of the methods till -1 is returned.
	while(1){
		choice = (rand() % 4) + 1;
		if(choice == 1){
			printf("Two number have been added enter your guess of the total\n");
			input = add();
		}
		else if(choice == 2){
			printf("Two number have been subtracted enter your guess of the total\n");
			input = subtract();
		}
		else if(choice == 3){
			printf("Two number have been multiplied enter your guess of the total\n");
			input = multiple();
		}
		else if(choice == 4){
			printf("Two numbers have been divided enter your guess of the total(Enter a decimal number of 2 digits)\n");
			input = divide();
		}
		else{
			printf("Something failed\n");
			exit(EXIT_FAILURE);
		}
		if(input == -1){
			printf("You got %d answers correct\n", correct);
			printf("You got %d answers wrong\n", incorrect);
			break;
		}
		else if(input == 0){
			incorrect++;
		}
		else if(input == 1){
			correct++;
		}
	}


}
