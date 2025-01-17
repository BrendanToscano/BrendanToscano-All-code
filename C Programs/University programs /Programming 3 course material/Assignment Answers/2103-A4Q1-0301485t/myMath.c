#include <stdio.h>

/* What does this program do?
This program contains 4 functions add(), subtract(), multiply() annd divide().
All of them take in a pair of integers and returns an integer except divide()
which returns a double.
*/

// Adds 2 integers and return an integer
int add(int num1, int num2){
    int tNums = num1 + num2;
    return tNums;
}
// Subtracts 2 integers and returns an integer
int subtract(int num1, int num2){
    int tNums = num1 - num2;
    return tNums;
}
// Multiplies 2 integers and returns an integer
int multiply(int num1, int num2){
    int tNums = num1 * num2;
    return tNums;
}
// Divides 2 integers and returns a double
double divide(int num1, int num2){
    // Checking if num2 is 0 and telling user can't divide by 0.
    if (num2 == 0){
        printf("Division by 0 not possible\n");
        return 0;
    }
    double tNums = (double)(num1)/(num2);
    return tNums;
}

