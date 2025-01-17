/*
 * Course: COMP 2103 FA01, 2023
 * Assignment 6, Question 1
 * Author: Brendan Toscano
 * Student ID: 0301485t
 * email address: 0301485t@acadiau.ca
 * Date: 2023-11-20
 * I certify that this code is my own.
 * I have not broken any rules concenring Academic Dishonesty.
*/

/* What does this program do?
 This program will take the file name fromt eh command line and open it with error checking.
 The wordcount function will count the number of words in the file basically it will check for
 whitespaces after every word.
 The chracter Frequency should counts every character of the 255ASCII values in the file. It will
 display the countof each characters.
 The subString Search will ask the user for a sub string then look through the file and find all
 occurances it will then tell the user how many times it occures in the file.
 The word reversal will get a word (similar to the wordcount working) and will reverse it then display it
 The palindromic word will use a similar working to the word reversal but will store and compare but the normal
 and reversed word. If both match it should be a palindromic word so it will display the word.
 */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// 21th November 3:51 - 4:07
// Function to count words from the file and display count.
void wordCount(FILE *file){
    int count = 0, c, prevC;
    // To reset the pointer to the start of the file.
    rewind(file);
    // Will run till the end of the file and get each character.
    while ((c = fgetc(file)) != EOF){
        // Checking if the char is a whitespace and if the character before it is a alphanumeric character.
        if (isspace(c) && isalpha(prevC)){
            // The end of the word and beginning of whitespace means 1 word is counted.
            count ++;
        }
        // Setting the prev char to current char to be used again on top.
        prevC = c;
    }
    // Since if the last place might not have a space it will count it indiviually.
    if (isalpha(prevC)){
        count ++;
    }
    printf("Word count of the file is %d\n", count);
}

// 4:35 - 4:58
// Function to count each character size and display the character with the size.
void characterFrequency(FILE *file){
    int *chars, *count, c;
    // Initallizing 2 arrays settign size to 255 as there are 255ASCII values.
    if((chars = malloc(255 * sizeof(int))) == NULL)
        exit(EXIT_FAILURE);
    if((count = malloc(255 * sizeof(int))) == NULL)
        exit(EXIT_FAILURE);
    
    // Setting every postion to -1111 which in our case is treated like none.
    for (int i = 0; i < 255; i++){
        chars[i] = -1111;
        count[i] = 0;
    }
    // To reset the pointer to the start of the file.
    rewind(file);
    // Will run till the end of the file and get each character.
    while ((c = fgetc(file)) != EOF){
        for (int i = 0; i < 255; i++){
            // Checking for empty positions say if position 0 is filled then it will go to else if and check that
            if (chars[i] == -1111){
                chars[i] = tolower(c);
                count[i] = 1;
                break;
            }
            // Checking if the array already has the element and incrementing that count in the second array.
            else if (chars[i] == tolower(c)){
                count[i]++;
                break;
            }
        }
    }
    // Printing out the data
    for (int i = 0; i < 255 && (chars[i] != -1111); i++){
        printf("The character '%c' has a count of %d\n",chars[i], count[i]);
    }
    // Deallocating memory
    free(chars);
    free(count);
}

// 7:43 - 8:07
// Function will ask user for substring to check with file and will display the number of times it occurs.
void substringSearch(FILE *file){
    int index = 0, count = 0, c;
    char *subString, *list;
    if((subString = malloc(1000 * sizeof(char))) == NULL)
        exit(EXIT_FAILURE);
    if((list = malloc(1000 * sizeof(char))) == NULL)
        exit(EXIT_FAILURE);
    
    printf("Enter the substring you want to find (999 character limit): ");
    fgets(subString, 1000, stdin);
    subString[strcspn(subString, "\n")] = '\0';
    
    // To reset the pointer to the start of the file.
    rewind(file);
    // Will run till the end of the file and get each character.
    while ((c = fgetc(file)) != EOF){
        // Checking if the chars from the substring are the same as the character.
        if (subString[index] == c){
            list[index] = c;
            // Setting the last position of the string.
            list[index + 1] = '\0';
            // Comparing both the sub string and list if they are the same then incrementing count and reseting index.
            if (strcmp(subString,list) == 0){
                count++;
                index = 0;
                continue;
            }
            index++;
        }
        // If the characters dont match restting the index.
        else{
            index = 0;
        }
    }
    printf("The substring '%s' has apperead %d in the file\n", subString, count);
    // Deallocating memory
    free(subString);
    free(list);
}

// 4:48 - 5:01
// Fucntion will get a word and then reverse it then display it.
void wordReversal(FILE *file){
    int index = 0, c, prevC;
    char *word;
    if((word = malloc(150 * sizeof(char))) == NULL)
        exit(EXIT_FAILURE);
    
    // To reset the pointer to the start of the file.
    rewind(file);
    // Will run till the end of the file and get each character.
    while ((c = fgetc(file)) != EOF){
        // Checking if the char is a whitespace and if the character before it is a alphanumeric character.
        if (isspace(c) && isalpha(prevC)){
            word[index] = '\0';
            // Will count backwards.
            for (int i = index - 1; i >= 0; i--){
                printf("%c",word[i]);
            }
            printf(" ");
            index = 0;
        }
        else{
            // Will create the word then use it above and so on
            word[index] = tolower(c);
            index++;
        }
        prevC = c;
    }
    // Since the last space might not get counted if it doesnt end with whitespace so Im addding this one indiviudal one outside.
    if (index > 0){
        word[index] = '\0';
        for (int i = index - 1; i >= 0; i--){
            printf("%c",word[i]);
        }
        printf(" ");
    }
    printf("\n");
    // Deallocating memory
    free(word);
}

// 5:01 - 5:13
// Will get botht the normal and reverse word then will compare them if they match they are palindromic.
void palindromicWords(FILE *file){
    int index = 0, c, prevC;
    char *word, *revWord;
    // Creating array of size 150 each to store the word and its reverse
    if((word = malloc(150 * sizeof(char))) == NULL)
        exit(EXIT_FAILURE);
    if((revWord = malloc(150 * sizeof(char))) == NULL)
        exit(EXIT_FAILURE);
    
    // To reset the pointer to the start of the file.
    rewind(file);
    // Will run till the end of the file and get each character.
    while ((c = fgetc(file)) != EOF){
        // Checking if the char is a whitespace and if the character before it is a alphanumeric character.
        if (isspace(c) && isalpha(prevC)){
            word[index] = '\0';
            // Will count backwards.
            for (int i = index - 1; i >= 0; i--){
                revWord[i] = word[index - i - 1];
            }
            revWord[index] = '\0';
            // Comparing both the sub string and list if they are the same then incrementing count and reseting index.
            if (strcmp(revWord, word) == 0){
                printf("%s is a palindromic word\n", word);
            }
            index = 0;
        }
        else{
            word[index] = tolower(c);
            index++;
        }
        prevC = c;
    }
    // Since the last space might not get counted if it doesnt end with whitespace so Im addding this one indiviudal one outside.
    if (index > 0){
        word[index] = '\0';
        for (int i = index - 1; i >= 0; i--){
            revWord[i] = word[index - i - 1];
        }
        revWord[index] = '\0';
        if (strcmp(revWord, word) == 0){
            printf("%s is a palindromic word\n", word);
        }
    }
    // Deallocating memory
    free(word);
    free(revWord);
}

// 21th November 3:48 - 3:51
int main(int argc, char *argv[]){
    FILE *file;

    if (argc != 2){
        printf("User Instructions: ./textAnalysis file.txt\n");
        return EXIT_FAILURE;
    }
    if((file = fopen(argv[1], "r")) == NULL){
        fprintf(stderr, "Error opening file.\n");
        return EXIT_FAILURE;
    }
    
    wordCount(file);
    characterFrequency(file);
    substringSearch(file);
    wordReversal(file);
    palindromicWords(file);
    
    if(fclose(file) == EOF){
        fprintf(stderr, "File close failed.\n");
        return EXIT_FAILURE;
    }
    
}
