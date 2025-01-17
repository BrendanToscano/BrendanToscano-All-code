#include <stdio.h>
#include <stdlib.h>
/*
 * Course: COMP 2103 FA01, 2023
 * Assignment 2, Question 2
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-10-08
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.

Program will ask user for 4 options:-  To enter two integers,
To enter two decimals, To enter one integer and one decimal or to Quit.
The program will keep asking the user to select an option
 till they select option (Quit).

All test cases have been addressed here.
If the user enters anything other than the 4 options it
will quit the program.
If the user enters anything other than an integer or deimal where required
then the program will again prompt the user and quit. The program works like
expected.
*/

int main(){
    char option;
    int int1;
    int int2;
    double double1;
    double double2;
    // Creating infinite loop.
    while(1){
        // Asking the user 1 of 4 options (a,b,c,d)
        printf("Select one of the four options (a, b, c, d):\n");
        printf("a) Enter two integers\n");
        printf("b) Enter two decimals\n");
        printf("c) Enter one integer and one decimal\n");
        printf("d) Quit\n");
        printf("Enter a, b, c, d: ");
        scanf(" %c", &option);
        // If user enters option a
        if(option == 'a'){
            // Asks for 1st integer
            printf("Enter the first integer: ");
            // error handling if user enter anyhting other than expected intput will prompt user.
            if(scanf("%d", &int1) != 1){
                printf("Try again, input was invalid\n");
				exit(EXIT_FAILURE);
            }
            // Asks for 2nd integer
            printf("Enter the second integer: ");
            // error handling if user enter anyhting other than expected intput will prompt user.
            if(scanf("%d", &int2) != 1){
                printf("Try again, input was invalid\n");
                exit(EXIT_FAILURE);
			}
            // Adds both integer
            int output = int1 + int2;
            printf("%d + %d = %d\n", int1, int2, output);
        }
        // If user enters option b
        else if(option == 'b'){
            // Ask for 1st Decimal
            printf("Enter the first Decimal: ");
            // error handling if user enter anyhting other than expected intput will prompt user.
            if(scanf("%lf", &double1) != 1){
                printf("Try again, input was invalid\n");
                exit(EXIT_FAILURE);
            }
            // Ask for 2nd Decimal
            printf("Enter the second Decimal: ");
            // error handling if user enter anyhting other than expected intput will prompt user.
            if(scanf("%lf", &double2) != 1){
                printf("Try again, input was invalid\n");
                exit(EXIT_FAILURE);
            }
            // Adds the Decimals
            double output = double1 + double2;
            printf("%.2lf + %.2lf = %.2lf\n", double1, double2, output);
        }
        // If user enters option c
        else if(option == 'c'){
            // Ask for integer
            printf("Enter an integer: ");
            // error handling if user enter anyhting other than expected intput will prompt user.
            if(scanf("%d", &int1) != 1){
                printf("Try again, input was invalid\n");
                exit(EXIT_FAILURE);
			}
            // Ask for Decimal
            printf("Enter a Decimal: ");
            // error handling if user enter anyhting other than expected intput will prompt user.
            if(scanf("%lf", &double1) != 1){
                printf("Try again, input was invalid\n");
                exit(EXIT_FAILURE);
            }
            // Adds the int and decimal and gives decimal.
            double output1 = int1 + double1;
            // Adds the int and decimal and gives integer
            int output2 = int1 + double1;
            printf("%d + %.2lf = %.2lf\n", int1, double1, output1);
            printf("Output where float is casted to int: \n");
            printf("%d + %.2lf = %d\n" , int1, double1, output2);
        }
        // If user enters option d
        else if(option == 'd'){
            // Close Scanner
            
            // Will end program
            exit(EXIT_SUCCESS);
        }
        // For every other case (If user doesn't enter a, b, c or d)
        else{
            // Will end program
            exit(EXIT_FAILURE);
        }
    }
}

