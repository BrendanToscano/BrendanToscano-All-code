#include <stdio.h>
#include <stdlib.h>
#include "myMath.h"

/*
 * Course: COMP 2113 FA01, 2023
 * Assignment 4, Question 1
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-10-28
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.
*/

/*What does this program do?
It first asks the user to enter a number from 1-5. If the user enters 1 then the program
will ask the user 2 numbers and add them using the add function from the .h file.
If the user enters 2 it will again ask the user for 2 numbers and subtract them using the subreact
function. If the user enters 3 it will again ask the user for 2 numbers and multiply them using the
multiply function. In the above 3 cases all functions from the .h file return an integer which will be
printed to the users screen. If the user enters 4 then it will ask the user for 2 numbers and divide
them using the divide function. The divide function will give an error from division by 0 and will
return a double instead of an integer. IF the user enters 5 the program will exit succesfully. For
every other input the program will fail and exit.
*/

int main(void){
    int choice, num1, num2;
    while(1){
        // Asking user for an input from 1-5.
        printf("Enter 1(add), 2(subtract), 3(multiply), 4(divide), 5(Quit): ");
        // If user enters anything other than an integers.
        if(scanf("%d", &choice) != 1){
            printf("Input was not an integer\n");
            exit(EXIT_FAILURE);
        }
        // If user enters 5 will exit program.
        if(choice == 5)
            exit(EXIT_SUCCESS);
        
        // Asking user for first number.
        printf("Enter first number: ");
        // If user enters anything other than an integers.
        if(scanf("%d", &num1) != 1){
            printf("Input was not an integer\n");
            exit(EXIT_FAILURE);
        }
        // Asking user for second number.
        printf("Enter second number: ");
        // If user enters anything other than an integers.
        if(scanf("%d", &num2) != 1){
            printf("Input was not an integer\n");
            exit(EXIT_FAILURE);
        }
        // If user enters 1 will use the add function from the myMath.h and print what it returns.
        if(choice == 1)
            printf("%d\n", add(num1, num2));
        // If user enters 2 will use the subtract function from the myMath.h and print what it returns.
        else if(choice == 2)
            printf("%d\n", subtract(num1, num2));
        // If user enters 3 will use the multiply function from the myMath.h and print what it returns.
        else if(choice == 3)
            printf("%d\n", multiply(num1, num2));
        // If user enters 4 will use the divide function from the myMath.h and print what it returns.
        else if(choice == 4)
            printf("%lf\n", divide(num1, num2));
        // If user enters anything other than numbers 1-5.
        else{
            printf("Unknown input");
            printf("User Instructions: Enter 1(add), 2(subtract), 3(multiply), 4(divide), 5(Quit)\n");
            exit(EXIT_FAILURE);
        }
    }
}
