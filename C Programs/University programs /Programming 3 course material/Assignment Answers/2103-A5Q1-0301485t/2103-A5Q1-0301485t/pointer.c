/*
 * Course: COMP 2103 FA01, 2023
 * Assignment 5, Question 1
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-11-12
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.
*/

// Program started at 9:53am 11th November 2023
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

/* What does this program do?
 It creates a user specified size array and dynamically allocates memory.
 It randomly populates the array with numbers from -50 to 49.
 It can also ask user input for each element in the array instead.
 There is also a function that can be used to display the array.
 There is a function that finds the min, max, avg and sum of the array
 There is also a function that returns the reverse of the array using pointer manupilation
 A function to deallocate memory and the main function that runs all the lines of code.
 */

// 9:53
// Creates array and takes user specified size.
int* arrayCreation(int arraySize){
    int *array;
    if((array = malloc(arraySize * sizeof(int))) == NULL)
        exit(EXIT_FAILURE);
    
    return array;
}

// 10:04
// Fills array with user specified values.
void arrayPopulate(int arraySize, int *array){
    int tempNum;
    for(int i = 0; i < arraySize; i++){
        // Asking user for inputs
        printf("Enter an integer: ");
        if(scanf("%d", &tempNum) != 1){
            printf("Number entered is not an int.\n");
            exit(EXIT_FAILURE);
        }
        (*(array + i)) = tempNum;
    }
}

// 12th November 5:02
// Randomally generates values in arrays.
void arrayRandomPopulate(int arraySize, int *array){
    srand(time(NULL));
    for(int i = 0; i < arraySize; i++){
        (*(array + i)) = (rand() % 100) - 50;
    }
}

// 10:07
// Displays array.
void arrayDisplay(int arraySize, int *array){
    for(int i = 0; i < arraySize; i++){
        printf("%d\n", (*(array + i)));
    }
}

// 10:08
// Find max value of the array.
int maxVal(int arraySize, int *array){
    int maxVal = (*(array + 0));
    for(int i = 0; i < arraySize; i++){
        if(maxVal < (*(array + i)))
            maxVal = (*(array + i));
    }
    return maxVal;

}

// 10:08
// Find min value of the array.
int minVal(int arraySize, int *array){
    int minVal = (*(array + 0));
    for(int i = 0; i < arraySize; i++){
        if(minVal > (*(array + i)))
            minVal = (*(array + i));
    }
    return minVal;
}

// 10:13
// Find sum of all elements in array.
int sumOfArray(int arraySize, int *array){
    int total = 0;
    for(int i = 0; i < arraySize; i++){
        total += (*(array + i));
    }
    return total;
}

// 10:14
// Find average of all elements of array.
double avgOfArray(int arraySize, int *array){
    double avg = ((sumOfArray(arraySize, array)) / (double)arraySize);
    return avg;
}

// Debugging and changing the indexing part etc approx 10:30 on novemeber 11th then stopped

// 5:27
// Deallocate memory
void deallocateMemory(int **array){
    free(*array);
    *array = NULL;
}

// Reverse array using pointer logic
int* reverseArray(int arraySize, int *array){
    int *reverseArray = arrayCreation(arraySize);
    for(int i = 0; i < arraySize; i++){
        memmove(reverseArray + (arraySize - 1 - i), array + i, sizeof(int));
    }
    memmove(array, reverseArray, arraySize * sizeof(int));
    arrayDisplay(arraySize, array);
    deallocateMemory(&reverseArray);
    return array;
}

// 9:53
int main(void){
    int arraySize;
    printf("Enter array size: ");
    if(scanf("%d", &arraySize) != 1){
        printf("Number entered is not an int.\n");
        exit(EXIT_FAILURE);
    }
    int *array = arrayCreation(arraySize);
    arrayRandomPopulate(arraySize, array);
    arrayDisplay(arraySize, array);
    printf("max Value of array is %d\n", maxVal(arraySize, array));
    printf("min Value of array is %d\n", minVal(arraySize, array));
    printf("Sum of array is %d\n", sumOfArray(arraySize, array));
    printf("Average of the array is %lf\n", avgOfArray(arraySize, array));
    array = reverseArray(arraySize, array);
    deallocateMemory(&array);
}
